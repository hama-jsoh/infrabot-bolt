from ._input import Input


class StaticSelectInput(Input):
    def __init__(
        self,
        title: str,
        selectbtn_texts: list,
        opt_value: str
    ) -> None:
        super(StaticSelectInput, self).__init__()
        _type = "static_select"
        self.selections = selectbtn_texts
        _options = self.get_opts(opt_value)
        _element = dict(
            type=_type,
            options=_options,
            action_id="static-select-action"
        )
        _label = dict(type="plain_text", text=title, emoji=True)
        self.body = dict(
            type=self.type,
            element=_element,
            label=_lable
        )

    def get_opts(self, value: str) -> list:
        option_list = [
            dict(
                text=dict(
                    type="plain_text",
                    text=selected_text,
                    emoji=True
                ),
                value=f"{value}-{idx}"
            )
            for idx, selected_text in enumerate(self.selections)
        ]
        return option_list
