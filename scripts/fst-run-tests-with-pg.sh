#!/bin/sh -e
start_time="$(date +%s)"

POSTGRES_TIMEOUT="${POSTGRES_TIMEOUT:-30}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-fst-test}"
POSTGRES_USER="${POSTGRES_USER:-fst-test}"
POSTGRES_DB="${POSTGRES_DB:-fst-test}"
POSTGRES_INTERNAL_PORT="${POSTGRES_INTERNAL_PORT:-5432}"
POSTGRES_IMAGE="${POSTGRES_IMAGE:-postgres:13-alpine}"
POSTGRES_EXTERNAL_PORT="${POSTGRES_EXTERNAL_PORT:-9999}"
POSTGRES_NAME="${POSTGRES_NAME:-postgres-test-fst}"

export ERL_CRASH_DUMP="${ERL_CRASH_DUMP:-/tmp}"
# Get directory where this script lives, needed for running other scripts
BASE_DIR="$(realpath $(dirname $0))"
# Colors
. "$BASE_DIR"/colors.sh

POSTGRES_PORT_MAP="127.0.0.1:$POSTGRES_EXTERNAL_PORT:$POSTGRES_INTERNAL_PORT"
[ -z "$CI" ] && \
    POSTGRES_HOST="127.0.0.1" POSTGRES_PORT="$POSTGRES_EXTERNAL_PORT" ||
    POSTGRES_HOST="postgres" POSTGRES_PORT="$POSTGRES_INTERNAL_PORT"

echo_debug "Configuration:"
echo_debug "POSTGRES_TIMEOUT: $POSTGRES_TIMEOUT"
echo_debug "POSTGRES_PASSWORD: $POSTGRES_PASSWORD"
echo_debug "POSTGRES_USER: $POSTGRES_USER"
echo_debug "POSTGRES_DB: $POSTGRES_DB"
echo_debug "POSTGRES_INTERNAL_PORT: $POSTGRES_INTERNAL_PORT"
echo_debug "POSTGRES_IMAGE: $POSTGRES_IMAGE"
echo_debug "POSTGRES_EXTERNAL_PORT: $POSTGRES_EXTERNAL_PORT"
echo_debug "POSTGRES_NAME: $POSTGRES_NAME"
echo_debug "POSTGRES_HOST: $POSTGRES_HOST"
echo_debug "POSTGRES_PORT: $POSTGRES_PORT"
# Set this explicitly or it'll be overriden in fst-run-tests.sh otherwise...
[ -z "$FST_DB_ENGINE"] && export FST_DB_ENGINE='django.db.backends.postgresql'

# Export variables so they are caught inside the container
export DJANGO_SETTINGS_MODULE CI \
       POSTGRES_PASSWORD POSTGRES_USER POSTGRES_DB \
       POSTGRES_HOST POSTGRES_PORT \
       INTEGRATION_TESTS \
       POSTGRES_TESTS=1
# Add hook that tries to kill the container runnint at exit or in case of sigint.
# First arg set to anything means sigint handling.
end() {
    out=$?
    trap - EXIT
    echo_info "Running exit handler."
    if [ $1 ]
    then
        echo_error "Caught SIGINT/Ctrl+C"
        out=1
    fi
    [ $out -ne 0 ] && echo_error "Tests failed."
    [ $POSTGRES_CONTAINER_STARTED ] && \
        echo_info "Trying to stop and remove PostgreSQL container." && \
        docker rm -f "$POSTGRES_NAME" > /dev/null || true
    echo_info "PostgreSQL tests execution time: $(($(date +%s)-$start_time))s."
    exit $out
}
trap end EXIT
trap "end 1" INT
# Only run the container if not ran by CI, as CI provides postgresql container.
if [ -z "$CI" ]
then
    set +e
    out=$(docker ps -a -q -f name"$POSTGRES_NAME" 2>&1)
    code=$?
    set -e
    [ $code != 0 ] && \
        echo_error "Can't check if container running. Maybe docker is not working? Docker ps output:" && \
        echo_error "$out" && \
        exit 1
    if [ -z "$out" ];
    then
        echo_info "PostgreSQL not running. Trying to start it in a docker container."
        set +e
        out=$(docker run \
                        --name "$POSTGRES_NAME" \
                        -e "POSTGRES_PASSWORD" \
                        -e "POSTGRES_USER" \
                        -e "POSTGRES_DB" \
                        -p "$POSTGRES_PORT_MAP" \
                        -d "$POSTGRES_IMAGE" \
                        2>&1)
        code=$?
        set -e
        if [ $code = 0 ]
        then
            POSTGRESQL_CONTAINER_STARTED=1
            echo_info "Container started."
        else
            echo_error "Can't start the container. Docker run output:"
            echo_error "$out"
            exit 1
        fi
    else
        echo_error "Can't start container for PostgreSQL, as a container with the name"
        echo_error "$POSTGRES_NAME already exists. Possibly it was ran by previous invocation"
        echo_error "of this script. If you're sure you don't need it, you can stop/remove it"
        echo_error "with: docker rm -f $POSTGRES_NAME"
        exit 1
    fi
else
    echo_warn "I think I'm running within CI."
    echo_warn "If that's not true, please remove the 'CI' variable"
    echo_warn "form my environment, e.g. by running: unset CI, "
    echo_warn "and re-run."
fi
echo_info "Waiting $POSTGRES_TIMEOUT seconds for PostgreSQL."
"$BASE_DIR"/fst-wait-for-postgresql.py --timeout "$POSTGRES_TIMEOUT" "$POSTGRES_DB" "$POSTGRES_USER" \
            "$POSTGRES_PASSWORD" "$POSTGRES_HOST" "$POSTGRES_PORT"
echo_info "Running tests against PostgreSQL with coverage."
"$BASE_DIR"/sts-run-tests.sh "$@"
