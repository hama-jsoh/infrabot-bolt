from .._element import Element


class Header(Element):
    def __init__(self, text: str) -> None:
        super(Header, self).__init__()
        _type = "header"
        _text = dict(type="plain_text", text=text, emoji=True)
        self.body = dict(type=_type, text=_text)
