#!/usr/bin/env python
import argparse
from logging import config

from settings import LOGGING

config.dictConfig(LOGGING)

parser = argparse.ArgumentParser(description="Deploy commands")
parser.add_argument(
    "--action",
    type=str,
    choices=("update-sensors", "update-display"),
    help="Action to run",
)
args = parser.parse_args()


if __name__ == "__main__":
    if args.action == "update-sensors":
        from library.services import update_sensors

        update_sensors()
        exit(0)

    if args.action == "update-display":
        from library.services import update_display

        update_display()
        exit(0)

    parser.print_help()
