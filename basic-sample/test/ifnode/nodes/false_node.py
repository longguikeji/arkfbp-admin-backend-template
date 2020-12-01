from arkfbp.node import IFNode

class FalseNode(IFNode):

  def expression(self):
    print('false node')
    return False