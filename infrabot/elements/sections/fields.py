import json
from ._section import Section


class Fields(Section):
    def __init__(self, text_list: list) -> None:
        super(Fields, self).__init__()
        _fields = []
        for text in text_list:
            _field = dict(type="plain_text", emoji=True)
            _field['text'] = text
            _fields.append(_field)
        self.body = dict(type=self.type, fields=_fields)

    def json(self):
        return json.dumps(self.body)
