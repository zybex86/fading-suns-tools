#!/usr/bin/env python

# Script works for Python 2 & 3
import argparse
import psycopg2
import sys
import time


def is_postgresql_ready(args):
    try:
        connection = psycopg2.connect(
            dbname=args.db,
            user=args.user,
            password=args.password,
            host=args.host,
            port=args.port
        )
        connection.close()
        return True
    except Exception:
        return False


def main():
    def verbose_message(msg):
        if args.verbose:
            sys.stdout.write(msg)
            sys.stdout.flush()

    parser = argparse.ArgumentParser(
        description='Wait for PostgreSQL to load. ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("db", type=str, help="db name")
    parser.add_argument("user", type=str, help="db username")
    parser.add_argument("password", type=str, help="db password")
    parser.add_argument("host", type=str, help="address at which the deamon is available")
    parser.add_argument("port", type=str, help="port which the deamon listens at")
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="time to wait for deamon in seconds"
    )
    parser.add_argument(
        "--poll_interval",
        type=float,
        default=1.0,
        help="polling interval in seconds"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="be more verbose")
    args = parser.parse_args()

    start_time = time.time()
    verbose_message('Waiting for PostgreSQL - ')
    while (time.time() - start_time) < args.timeout:
        if is_postgresql_ready(args):
            verbose_message('Connected!\n')
            return 0
        else:
            verbose_message('.')
        time.sleep(args.poll_interval)
    verbose_message('timed out!\n')
    return 1


if __name__ == '__main__':
    exit(main())
