import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DB_PATH = os.environ.get("DB_PATH", BASE_DIR / "db.sqlite")

TEMP_SENSORS = [
    "28-000007162e15",
    "28-000007173569",
    "28-0000071766e4",
    "28-000007176e41",
    "28-000007177269",
]

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
