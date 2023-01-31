import logging
from decimal import Decimal
from pathlib import Path

logger = logging.getLogger(__name__)


class DS18B20:
    read_attempts = 3

    def __init__(self, address: str):
        self.address = address
        self.value = None

    @property
    def path(self) -> Path:
        return Path(f"/sys/bus/w1/devices/{self.address}/temperature")

    def read(self) -> Decimal | None:
        self.value = None
        for _ in range(self.read_attempts):
            try:
                with self.path.open("r") as f:
                    self.value = f.readline().strip()
                    if self.value:
                        return Decimal(self.value)
            except IOError:
                logger.error(f"Error reading sensor {self.address}")
