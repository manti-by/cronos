import logging
from decimal import Decimal

import RPi.GPIO as GPIO
from time import sleep

logger = logging.getLogger(__name__)


class YFS201:
    def __init__(self, address: str):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(address, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(address, GPIO.FALLING, callback=self.counter_callback)

        self.address = address
        self.counter = 0
        self.is_active = False
        self.value = None

    def counter_callback(self, *args, **kwargs):
        if self.is_active:
            self.value += 1

    def update(self):
        self.value = 0
        self.is_active = True
        sleep(1)
        self.is_active = False

    @property
    def litres_per_hour(self) -> Decimal | None:
        """Return Litres per Hour."""
        return Decimal(self.value / 7.5 * 60) if self.value else None
