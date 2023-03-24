from ._input import Input


class RadioButtonInput(Input):
    def __init__(
        self, title: str, radiobtn_texts: list, opt_value: str, optional: bool = True
    ) -> None:
        super(RadioButtonInput, self).__init__()
        _type = "radio_buttons"
        self.radiobuttons = radiobtn_texts
        _options = self.get_opts(opt_value)
        _element = dict(type=_type, options=_options, action_id="radiobutton-action")
        _label = dict(type="plain_text", text=title, emoji=True)

        if not optional:
            self.body = dict(type=self.type, element=_element, label=_lable)
        else:
            self.body = dict(
                type=self.type, element=_element, label=_lable, optional=optional
            )

    def get_opts(self, value: str) -> list:
        option_list = [
            dict(
                text=dict(type="plain_text", text=radiobutton, emoji=True),
                value=f"{value}-{idx}",
            )
            for idx, radiobutton in enumerate(self.radiobuttons)
        ]
        return option_list
