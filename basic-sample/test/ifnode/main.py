from arkfbp.flow import ViewFlow
from arkfbp.node import StartNode, StopNode
from .nodes import TrueNode, FalseNode, Error

# Editor your flow here.
class Main(ViewFlow):

    def create_nodes(self):
        return [
            {
                'cls': StartNode,
                'id': 'start',
                'next': 'truenode',
                'x': None,
                'y': None
            },
            {
                'cls': TrueNode,
                'id': 'truenode',
                'positive_next': 'falsenode',
                'negative_next': 'error',
                'x': None,
                'y': None
            },
            {
                'cls': FalseNode,
                'id': 'falsenode',
                'positive_next': 'error',
                'negative_next': 'stop',
                'x': None,
                'y': None
            },
            {
                'cls': Error,
                'id': 'error',
                'next': 'stop',
                'x': None,
                'y': None
            },
            {
                'cls': StopNode,
                'id': 'stop',
                'next': None,
                'x': None,
                'y': None
            }
        ]
