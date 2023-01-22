.PHONY: apollo

define SENSORS_MIGRATION_SCRIPT
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor TEXT,
    value PYDECIMAL,
    datetime DATETIME DEFAULT CURRENT_TIMESTAMP
);
endef

export SENSORS_MIGRATION_SCRIPT
migrate:
	sqlite3 db.sqlite "$$SENSORS_MIGRATION_SCRIPT"

check:
	black .
	flake8 .

update-sensors:
	./main.py --action=update-sensors
