import sys
from unittest.mock import MagicMock

mock_pydantic = MagicMock()
class MockBaseModel:
    model_config = {}
    def __init__(self, **kwargs):
        # Apply defaults that Pydantic would usually apply
        if not hasattr(self.__class__, '__annotations__'):
            self.__class__.__annotations__ = {}
            for k in dir(self.__class__):
                if not k.startswith('_') and not callable(getattr(self.__class__, k)):
                    self.__class__.__annotations__[k] = type(getattr(self.__class__, k))

        for k, default_val in self.__class__.__dict__.items():
            if not k.startswith('_') and not callable(default_val) and not isinstance(default_val, classmethod):
                if isinstance(default_val, MagicMock): # Field default
                    pass # We will handle Fields differently or assume they are passed
                else:
                    setattr(self, k, default_val)

        for k, v in kwargs.items():
            setattr(self, k, v)

mock_pydantic.BaseModel = MockBaseModel
def mock_field(*args, **kwargs):
    if 'default' in kwargs:
        return kwargs['default']
    return MagicMock()
mock_pydantic.Field = mock_field
sys.modules['pydantic'] = mock_pydantic
