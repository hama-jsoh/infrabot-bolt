import json
from .._element import Element


class Input(Element):
    def __init__(self) -> None:
		super(Input, self).__init__()
        self.type = "input"
