from infrabot.elements import Blocks
from infrabot.elements.view import Modal
from infrabot.elements.sections import MarkDown
from infrabot.elements.inputs import (
    CheckBoxInput,
    RadioButtonInput,
    StaticSelectInput,
    PlainTextInput,
)
from infrabot.elements.actions import DatePicker, TimePicker


if __name__ == "__main__":
    modal = Modal(
        "My App",
        Blocks(
            StaticSelectInput(
                title="Repository",
                text="Select a repo",
                selectbtn_texts=["project-admin", "project-web", "project-api"],
                opt_value="repo",
            ),
            StaticSelectInput(
                title="Branch",
                text="Select a branch",
                selectbtn_texts=["master", "develop", "beta"],
                opt_value="branch"
            ),
            RadioButtonInput(
                title="Type",
                radiobtn_texts=["prod", "dev"],
                opt_value="type",
                optional=True
            ),
            CheckBoxInput(
                title="Stage",
                checkboxes=["CodeBuild", "CodeDeploy"],
                opt_value="stage",
                optional=True
            ),
            CheckBoxInput(
                title="Auto Scaling Group",
                checkboxes=["Exist"],
                opt_value="asg",
                optional=True
            ),
            PlainTextInput("ASG or EC2 Name", multiline=True, optional=True),
            MarkDown("*Due*"),
            DatePicker("Select a date"),
            TimePicker("Select time"),
            PlainTextInput("Anything else you want to tell us?"),
        ),
    )

    modal.pretty
    print(modal.to_dict)
