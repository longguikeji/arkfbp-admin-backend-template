from siteapi.v1.user.create_user.nodes.node2 import Node2
from siteapi.v1.user.create_user.nodes.serializer_data import SerializerData
from siteapi.v1.user.create_user.nodes.node1 import Node1
from arkfbp.flow import ViewFlow
from arkfbp.node import StartNode, StopNode


class Main(ViewFlow):
    debug = False

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
            'next': 'serializer_data',
            'x': 0.0,
            'y': 0.0
        }, {
            'cls': SerializerData,
            'id': 'serializer_data',
            'next': 'node2',
            'x': 0.0,
            'y': 0.0
        }, {
            'cls': Node2,
            'id': 'node2',
            'next': 'stop',
            'x': 0.0,
            'y': 0.0
        }, {
            'cls': StopNode,
            'id': 'stop',
            'next': None,
            'x': None,
            'y': None
        }]
