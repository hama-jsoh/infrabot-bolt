from ._element import Element


class Blocks(Element):
	def __init__(self, *blocks) -> None:
		super(Blocks, self).__init__()
		_block = [block.body for block in blocks]
		self.body = dict(blocks=_block)
