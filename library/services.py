import logging

from settings import TEMP_SENSORS
from library.database import Database
from library.imager import Imager
from library.ds18b20 import DS18B20
from library.ili9341 import ILI9341

database = Database()
logger = logging.getLogger(__name__)


def update_sensors():
    logger.info("Run sensors update")

    for name, data in TEMP_SENSORS.items():
        sensor = DS18B20(data["address"])
        data["value"] = sensor.read()
        logger.info(f"{name} - {data['value']}")

    database.insert(*[data["value"] for _, data in TEMP_SENSORS.items()])


def update_display():
    logger.info("Run display update")

    result = {}
    db_data = database.latest()
    for name, data in TEMP_SENSORS.items():
        data["value"] = db_data[name]
        result[name] = data

    imager = Imager(result)
    image = imager.generate()

    display = ILI9341(image)
    display.update()
