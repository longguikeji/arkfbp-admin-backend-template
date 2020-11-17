from arkfbp.node import FunctionNode


# Editor your node here.
class Node1(FunctionNode):

    def run(self, *args, **kwargs):
        print(f'Hello, Node1!')
        if self.inputs:
            return {"username": self.flow.state.fetch()['request'].ds.get('username'),
                    "token": self.inputs}
        return {"detail": "valid username or password"}
