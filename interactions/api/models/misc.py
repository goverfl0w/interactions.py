from typing import Optional

# TODO: Reorganise these models based on which big obj uses little obj
# TODO: Potentially rename some model references to enums, if applicable
# TODO: Reorganise mixins to its own thing, currently placed here because circular import sucks.
# also, it should be serialiser* but idk, fl0w'd say something if I left it like that. /shrug


class DictSerializerMixin(object):
    """
    The purpose of this mixin is to be subclassed.

    ..note::

        On subclass, it:
            -- From kwargs (received from the Discord API response), add it to the `_json` attribute
            such that it can be reused by other libraries/extensions
            -- Aids in attributing the kwargs to actual model attributes, i.e. `User.id`

    ..warning::

        This does NOT convert them to its own data types, i.e. timestamps, or User within Member. This is left by
        the object that's using the mixin.
    """

    __slots__ = "_json"

    _json: dict

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        self._json = kwargs


class Overwrite(DictSerializerMixin):
    """This is used for the PermissionOverride obj"""

    __slots__ = ("_json", "id", "type", "allow", "deny")
    _json: dict
    id: int
    type: int
    allow: str
    deny: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ClientStatus(DictSerializerMixin):
    __slots__ = ("_json", "desktop", "mobile", "web")
    _json: dict
    desktop: Optional[str]
    mobile: Optional[str]
    web: Optional[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
