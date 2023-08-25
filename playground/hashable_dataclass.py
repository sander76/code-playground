from dataclasses import dataclass


@dataclass
class Node:
    identity: int
    value: int

    def __hash__(self) -> int:
        return self.identity

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Node):
            if __value.identity == self.identity:
                return True
        return False


node_1 = Node(identity=10, value=20)
node_2 = Node(identity=10, value=21)

print(node_1 == node_2)

nodes = set()
nodes.add(node_1)
nodes.add(node_2)
print(nodes)
