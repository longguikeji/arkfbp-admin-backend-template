from arkfbp.node import FunctionNode


# Editor your node here.
class Node1(FunctionNode):

    def run(self, *args, **kwargs):
        print('Hello, Permission Node for Admin!')
        return True
