#!/usr/bin/env python
import argparse
from logging import config

from config import LOGGING

parser = argparse.ArgumentParser(description="Deploy commands")
parser.add_argument(
    "--action", type=str, choices=("update-sensors",), help="Action to run"
)
args = parser.parse_args()

config.dictConfig(LOGGING)


if __name__ == "__main__":
    if args.action == "update-sensors":
        from library.services import update_sensors

        update_sensors()
        exit(0)
    parser.print_help()
