from arkfbp.flow import Flow
from arkfbp.node import StartNode, StopNode
from .nodes.node1 import Node1


class Main(Flow):
    def create_nodes(self):
        return [{
            'cls': StartNode,
            'id': 'start',
            'next': 'node1',
            'x': None,
            'y': None
        }, {
            'cls': Node1,
            'id': 'node1',
            'next': 'stop',
            'x': None,
            'y': None
        }, {
            'cls': StopNode,
            'id': 'stop',
            'next': None,
            'x': None,
            'y': None
        }]
