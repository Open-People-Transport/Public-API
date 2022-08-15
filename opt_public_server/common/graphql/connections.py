from typing import Generic, TypeVar
from uuid import UUID

import strawberry

from opt_public_server.common.models.node import Node as NodeModel
from opt_public_server.common.utils import description


@strawberry.interface(description=description(NodeModel))
class Node:
    id: UUID


NodeType = TypeVar("NodeType", bound=Node)


@strawberry.type
class Edge(Generic[NodeType]):
    node: NodeType


@strawberry.type
class Connection(Generic[NodeType]):
    count: int
    edges: list[Edge[NodeType]]
