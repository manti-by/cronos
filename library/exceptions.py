class SensorNotReadyException(Exception):
    """Raise when sensor not ready."""


class SensorReadErrorException(Exception):
    """Raise when sensor not readable."""


class SensorNotFoundException(Exception):
    """Raise when sensor not connected."""


class BadSensorDataException(Exception):
    """Raise when sensor data not parsable."""
