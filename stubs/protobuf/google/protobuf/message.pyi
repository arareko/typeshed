from collections.abc import Sequence
from typing import Any, TypeVar
from typing_extensions import Self

from .descriptor import Descriptor, FieldDescriptor
from .internal.extension_dict import _ExtensionDict, _ExtensionFieldDescriptor

class Error(Exception): ...
class DecodeError(Error): ...
class EncodeError(Error): ...

_M = TypeVar("_M", bound=Message)  # message type (of self)

class Message:
    DESCRIPTOR: Descriptor
    def __deepcopy__(self, memo: Any = None) -> Self: ...
    def __eq__(self, other_msg): ...
    def __ne__(self, other_msg): ...
    def MergeFrom(self, other_msg: Self) -> None: ...
    def CopyFrom(self, other_msg: Self) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: bytes) -> int: ...
    def ParseFromString(self, serialized: bytes) -> int: ...
    def SerializeToString(self, *, deterministic: bool = ...) -> bytes: ...
    def SerializePartialToString(self, *, deterministic: bool = ...) -> bytes: ...
    def ListFields(self) -> Sequence[tuple[FieldDescriptor, Any]]: ...
    # The TypeVar must be bound to `Message` or we get mypy errors, so we cannot use `Self` for `HasExtension` & `ClearExtension`
    def HasExtension(self: _M, field_descriptor: _ExtensionFieldDescriptor[_M, Any]) -> bool: ...
    def ClearExtension(self: _M, field_descriptor: _ExtensionFieldDescriptor[_M, Any]) -> None: ...
    # The TypeVar must be bound to `Message` or we get mypy errors, so we cannot use `Self` for `Extensions`
    @property
    def Extensions(self: _M) -> _ExtensionDict[_M]: ...
    def ByteSize(self) -> int: ...
    @classmethod
    def FromString(cls, s: bytes) -> Self: ...
    # Intentionally left out typing on these three methods, because they are
    # stringly typed and it is not useful to call them on a Message directly.
    # We prefer more specific typing on individual subclasses of Message
    # See https://github.com/dropbox/mypy-protobuf/issues/62 for details
    def HasField(self, field_name: Any) -> bool: ...
    def ClearField(self, field_name: Any) -> None: ...
    def WhichOneof(self, oneof_group: Any) -> Any: ...
    # TODO: check kwargs
    def __init__(self, *args, **kwargs) -> None: ...
