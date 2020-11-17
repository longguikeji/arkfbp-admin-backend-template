from arkfbp.node import FunctionNode


# Editor your node here.
class Node2(FunctionNode):

    def run(self, *args, **kwargs):
        print(f'Hello, Node2!')
        return {'success': 'validated'}
