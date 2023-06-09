__all__ = ['KazooState', 'KazooClient', 'KazooRetry']

from kazoo.protocol.connection import ConnectionHandler
from kazoo.protocol.states import KazooState, WatchedEvent, ZnodeStat
from kazoo.handlers.threading import AsyncResult, SequentialThreadingHandler
from kazoo.retry import KazooRetry
from kazoo.security import ACL

from typing import Any, Callable, Optional, Tuple, List


class KazooClient:
    handler: SequentialThreadingHandler
    _state: str
    _connection: ConnectionHandler
    _session_timeout: int
    retry: Callable[..., Any]
    _retry: KazooRetry
    def __init__(self, hosts=..., timeout=..., client_id=..., handler=..., default_acl=..., auth_data=..., sasl_options=..., read_only=..., randomize_hosts=..., connection_retry=..., command_retry=..., logger=..., keyfile=..., keyfile_password=..., certfile=..., ca=..., use_ssl=..., verify_certs=..., **kwargs) -> None: ...
    @property
    def client_id(self) -> Optional[Tuple[Any]]: ...
    def add_listener(self, listener: Callable[[str], None]) -> None: ...
    def start(self, timeout: int = ...) -> None: ...
    def restart(self) -> None: ...
    def set_hosts(self, hosts: str, randomize_hosts: Optional[bool] = None) -> None: ...
    def create(self, path: str, value: bytes = b'', acl: Optional[ACL]=None, ephemeral: bool = False, sequence: bool = False, makepath: bool = False, include_data: bool = False) -> None: ...
    def create_async(self, path: str, value: bytes = b'', acl: Optional[ACL]=None, ephemeral: bool = False, sequence: bool = False, makepath: bool = False, include_data: bool = False) -> AsyncResult: ...
    def get(self, path: str, watch: Optional[Callable[[WatchedEvent], None]] = None) -> Tuple[bytes, ZnodeStat]: ...
    def get_children(self, path: str, watch: Optional[Callable[[WatchedEvent], None]] = None, include_data: bool = False) -> List[str]: ...
    def set(self, path: str, value: bytes, version: int = -1) -> ZnodeStat: ...
    def set_async(self, path: str, value: bytes, version: int = -1) -> AsyncResult: ...
    def delete(self, path: str, version: int = -1, recursive: bool = False) -> None: ...
    def delete_async(self, path: str, version: int = -1) -> AsyncResult: ...
    def _call(self, request: Tuple[Any], async_object: AsyncResult) -> Optional[bool]: ...
