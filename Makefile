.PHONY: apollo

define SENSORS_MIGRATION_SCRIPT
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    t1 PYDECIMAL,
    t2 PYDECIMAL,
    t3 PYDECIMAL,
    t4 PYDECIMAL,
    t5 PYDECIMAL,
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

update-display:
	./main.py --action=update-display