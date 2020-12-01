from arkfbp.node import IFNode

class TrueNode(IFNode):

  def expression(self):
    print('true node')
    return True