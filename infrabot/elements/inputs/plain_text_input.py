from ._input import Input


class PlainTextInput(Input):
    def __init__(
        self, title: str, text: list[str], multiline: bool = True, optional: bool = True
    ) -> None:
        super(PlainTextInput, self).__init__()
        _type = "plaintext"
        _label = dict(type="plain_text", text=title, emoji=True)
        self.plaintext = text

        if not multiline:
            _element = dict(type=_type, action_id="plaintext-action")
        else:
            _element = dict(type=_type, multiline=multiline)

        if not optional:
            self.body = dict(type=self.type, element=_element, label=_lable)
        else:
            self.body = dict(
                type=self.type, element=_element, label=_lable, optional=optional
            )
