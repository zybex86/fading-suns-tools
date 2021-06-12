#!/bin/sh -e

yes_if_defined() {
    [ "$1" ] && printf "yes" || printf "no"
}

no_if_defined() {
    [ "$1" ] && printf "no" || printf "yes"
}

start_time="$(date +%s)"
# Get directory where this script lives, needed for running other scripts
BASE_DIR="$(realpath $(dirname $0))"
# Colors
. "$BASE_DIR"/colors.sh

extra_pytest_args=""
[ -z "$CI" ] && extra_pytest_args="$extra_pytest_args -vv"
[ -z "$NO_COVERAGE" ] && extra_pytest_args="$extra_pytest_args --cov=fst"
[ -z "$POSTGRES_TESTS" ] && extra_pytest_args="$extra_pytest_args -m \"not postgresql\""

echo_info "Running pytest."
echo_info "Checking code coverage: $(no_if_defined $NO_COVERAGE)."
echo_info "Running with CI: $(yes_if_defined $CI)."
echo_info "Running integration tests: $(yes_if_defined $INTEGRATION_TESTS)."
[ "$DJANGO_SETTINGS_MODULE" ] && \
    echo_info "Using settings from $DJANGO_SETTINGS_MODULE." || \
    echo_info "Settings module not overriden by environment."
# Eval is required so that extra_pytest_args is properly expanded into arguments.
eval pytest $extra_pytest_args --color=yes tests "$@"
out=$?
echo_info "Pytest execution time: $(($(date +%s)-$start_time))s."
exit $out
