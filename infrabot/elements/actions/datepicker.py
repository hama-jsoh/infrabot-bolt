from datetime import datetime
from ._action import Actions


class DatePicker(Actions):
    def __init__(self, text):
        super(DatePicker, self).__init__()
        _nowdate = f"{self.current_date()}"
        _placeholder = dict(type="plain_text", text="Select a date", emoji=True)
        _elements = [
            dict(
                type="datepicker",
                initial_date=_nowdate,
                placeholder=_placeholder,
                action_id=f"datepicker-0",
            ),
            dict(
                type="datepicker",
                initial_date=_nowdate,
                placeholder=_placeholder,
                action_id=f"datepicker-1",
            ),
        ]
        self.body = dict(type=self.type, elements=_elements)

    def current_date(self):
        now = datetime.now()
        return now.date()
