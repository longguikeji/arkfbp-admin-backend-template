from arkfbp.node import FunctionNode

class Error(FunctionNode):
  
  def run(self, *args, **kwargs):
    return {'result':'error'}