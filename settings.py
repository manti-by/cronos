import os
from decimal import Decimal
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DB_PATH = os.environ.get("DB_PATH", BASE_DIR / "db.sqlite")

TEMP_SENSORS = {
    "t1": {
        "title": "Main tank",
        "address": "28-000007162e15",
        "value": None,
        "warning": Decimal("80"),
        "critical": Decimal("90"),
    },
    "t2": {
        "title": "Stillhead",
        "address": "28-000007173569",
        "value": None,
        "warning": Decimal("90"),
        "critical": Decimal("95"),
    },
    "t3": {
        "title": "Main cooler",
        "address": "28-0000071766e4",
        "value": None,
        "warning": Decimal("30"),
        "critical": Decimal("50"),
    },
    "t4": {
        "title": "Secondary cooler",
        "address": "28-000007176e41",
        "value": None,
        "warning": Decimal("30"),
        "critical": Decimal("50"),
    },
    "t5": {
        "title": "Receiver",
        "address": "28-000007177269",
        "value": None,
        "warning": Decimal("20"),
        "critical": Decimal("30"),
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)-8s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "filesystem": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": os.environ.get("LOG_PATH", BASE_DIR / "app.log"),
            "formatter": "standard",
        },
    },
    "loggers": {"": {"handlers": ["console"], "level": "DEBUG", "propagate": True}},
}
