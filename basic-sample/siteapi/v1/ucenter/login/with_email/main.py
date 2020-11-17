from arkfbp.flow import ViewFlow
from arkfbp.node import StartNode, StopNode


# Editor your flow here.
class Main(ViewFlow):

    def create_nodes(self):
        return [
            {
                'cls': StartNode,
                'id': 'start',
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
