import json
from ._section import Section


class MarkDown(Section):
    def __init__(self, msg: str, option=None) -> None:
        super(MarkDown, self).__init__()
        _type = "mrkdwn"
        _text = dict(type=_type, text=msg)
        self.body = dict(type=self.type, text=_text)
        if option is not None:
            self.body["accessory"] = option.body

    def json(self):
        return json.dumps(self.body)
