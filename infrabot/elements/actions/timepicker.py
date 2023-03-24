from datetime import datetime
from ._action import Actions


class TimePicker(Actions):
    def __init__(self, text):
        super(TimePicker, self).__init__()
        _nowtime = f"{self.current_time()}"
        _timevalue = datetime.now().strftime("%H-%M")
        _placeholder = dict(type="plain_text", text="Select time", emoji=True)
        _elements = [
            dict(
                type="timepicker",
                initial_time=_nowtime,
                placeholder=_placeholder,
                action_id=f"timepicker-{_timevalue}",
            ),
            dict(
                type="button",
                text=dict(type="plain_text", text="미선택시 날짜 기준으로 작업", emoji=True),
                value=f"click_me_{_timevalue}",
                action_id=f"actionId_{_timevalue}",
            ),
        ]
        self.body = dict(type=self.type, elements=_elements)

    def current_time(self):
        now = datetime.now()
        return now.strftime("%H:%M")
