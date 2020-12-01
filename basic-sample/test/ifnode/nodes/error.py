from arkfbp.node import FunctionNode

class Error(FunctionNode):
  
  def run(self):
    return {'result':'error'}