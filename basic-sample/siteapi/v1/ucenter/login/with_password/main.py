from siteapi.v1.ucenter.login.with_password.nodes.node1 import Node1
from siteapi.v1.ucenter.login.with_password.nodes.verify_password import VerifyPassword
from arkfbp.flow import ViewFlow
from arkfbp.node import StartNode, StopNode
from django.views.decorators.csrf import csrf_exempt


class Main(ViewFlow):
    def create_nodes(self):
        return [{
            'cls': StartNode,
            'id': 'start',
            'next': 'verify_password',
            'x': None,
            'y': None
        }, {
            'cls': VerifyPassword,
            'id': 'verify_password',
            'next': 'node1',
            'x': 0.0,
            'y': 0.0
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

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(Main, self).dispatch(request, *args, **kwargs)

    @csrf_exempt
    def before_execute(self, inputs, *args, **kwargs):
        self.state.commit({'request': inputs})
