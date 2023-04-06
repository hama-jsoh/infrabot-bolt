from .._element import Element


class Modal(Element):
    def __init__(self, title, block) -> None:
        super(Modal, self).__init__()
        _type = "modal"
        _title = dict(type="plain_text", text=title, emoji=True)
        _submit = dict(type="plain_text", text="Submit", emoji=True)
        _close = dict(type="plain_text", text="Cancel", emoji=True)
        _blocks = list(block.body.values())[0]

        self.body = dict(
            type=_type, title=_title, submit=_submit, close=_close, blocks=_blocks
        )
