import logging

from config import TEMP_SENSORS
from library.database import Database
from library.ds18b20 import DS18B20

database = Database()
logger = logging.getLogger(__name__)


def update_sensors():
    logger.info("Run sensors update")
    for address in TEMP_SENSORS:
        sensor = DS18B20(address)
        sensor.update()
        if sensor.temperature:
            database.insert(sensor.address, sensor.temperature)
        logger.info(f"{address} - {sensor.temperature}")
