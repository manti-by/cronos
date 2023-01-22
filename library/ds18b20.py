import logging
from decimal import Decimal
from pathlib import Path

from library.exceptions import SensorNotFoundException, BadSensorDataException

logger = logging.getLogger(__name__)


class DS18B20:
    read_attempts = 3

    def __init__(self, address: str):
        self.address = address
        self.temperature = None

    @property
    def path(self) -> Path:
        return Path(f"/sys/bus/w1/devices/{self.address}/temperature")

    def update(self):
        self.temperature = None
        for _ in range(self.read_attempts):
            try:
                self.temperature = self.read()
                if self.temperature:
                    break
            except SensorNotFoundException:
                continue

    def read(self) -> Decimal:
        try:
            with self.path.open("r") as f:
                temperature = f.readline().strip()
                return Decimal(f"{temperature[0:2]}.{temperature[3:5]}")
        except IOError:
            raise SensorNotFoundException(f"Could not find sensor {self.address}")
        except IndexError:
            raise BadSensorDataException(
                f"Could not parse sensor {self.address} data {temperature}"
            )
