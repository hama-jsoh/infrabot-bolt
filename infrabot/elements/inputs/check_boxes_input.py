from ._input import Input


class CheckBoxInput(Input):
    def __init__(
        self, title: str, checkboxes: list, opt_value: str, optional: bool = True
    ) -> None:
        super(CheckBoxInput, self).__init__()
        _type = "checkboxes"
        self.checkboxes = checkboxes
        _options = self.get_opts(opt_value)
        _element = dict(type=_type, options=_options, action_id="checkboxes-action")
        _label = dict(type="plain_text", text=title, emoji=True)

        if not optional:
            self.body = dict(type=self.type, element=_element, label=_label)
        else:
            self.body = dict(
                type=self.type, element=_element, label=_label, optional=optional
            )

    def get_opts(self, value: str) -> list:
        option_list = [
            dict(
                text=dict(type="plain_text", text=checkbox, emoji=True),
                value=f"{value}-{idx}",
            )
            for idx, checkbox in enumerate(self.checkboxes)
        ]
        return option_list
