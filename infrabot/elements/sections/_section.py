from .._element import Element


class Section(Element):
    def __init__(self) -> None:
		super(Section, self).__init__()
        self.type = "section"
