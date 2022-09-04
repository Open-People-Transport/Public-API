from typing import Generic, TypeVar
from uuid import UUID

import strawberry

from opt_public_server.common import core
from opt_public_server.common.utils import ModelInfo


@strawberry.interface(description=ModelInfo(core.Node).gqldescription)
class Node:
    id: UUID


NodeType = TypeVar("NodeType", bound=Node)


@strawberry.type
class Edge(Generic[NodeType]):
    node: NodeType


@strawberry.type
class Connection(Generic[NodeType]):
    count: int
    nodes: list[NodeType]
    edges: list[Edge[NodeType]]
