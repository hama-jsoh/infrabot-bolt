import json
from ._section import Section


class Button(Section):
    def __init__(self, text: str, url: str = None) -> None:
        _type = "button"
        _text = dict(type="plain_text", text=text, emoji=True)
        _btn_url = url
        _action_id = "button-action"
        self.body = dict(
            type=_type, text=_text, value="TODO-FIX", url=_btn_url, action_id=_action_id
        )

    def json(self):
        return json.dumps(self.body)
