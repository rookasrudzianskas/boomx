class CogError(Exception):
    """Base class for all BoomX errors."""


class ConfigDoesNotExist(CogError):
    """Exception raised when a boomx.yaml does not exist."""


class PredictorNotSet(CogError):
    """Exception raised when 'predict' is not set in boomx.yaml when it needs to be."""
