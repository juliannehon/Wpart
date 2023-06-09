from _typeshed import Incomplete
from typing import Any

import psycopg2

class PoolError(psycopg2.Error): ...

class AbstractConnectionPool:
    minconn: Any
    maxconn: Any
    closed: bool
    def __init__(self, minconn, maxconn, *args, **kwargs) -> None: ...
    # getconn, putconn and closeall are officially documented as methods of the
    # abstract base class, but in reality, they only exist on the children classes
    def getconn(self, key: Incomplete | None = ...): ...
    def putconn(self, conn: Any, key: Incomplete | None = ..., close: bool = ...) -> None: ...
    def closeall(self) -> None: ...

class SimpleConnectionPool(AbstractConnectionPool): ...

class ThreadedConnectionPool(AbstractConnectionPool):
    # This subclass has a default value for conn which doesn't exist
    # in the SimpleConnectionPool class, nor in the documentation
    def putconn(self, conn: Incomplete | None = None, key: Incomplete | None = None, close: bool = False) -> None: ...
