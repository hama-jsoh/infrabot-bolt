from infrabot.elements.sections import Button, MarkDown, Fields
from infrabot.elements.actions import TimePicker, DatePicker
from infrabot.elements.inputs import CheckBoxInput, RadioButtonInput, StaticSelectInput, PlainTextInput
from infrabot.elements.header import Header
from infrabot.elements.view import Modal
from infrabot.elements import Blocks


if __name__ == "__main__":
    view = Modal(
        "My App",
        Blocks(
            StaticSelectInput("Repository", ['project-admin', 'project-web', 'project-api'], "repo"),
            StaticSelectInput("Branch", ['master', 'develop', 'beta'], "branch"),
            RadioButtonInput("Type", ['prod', 'dev'], "type", optional=True),
            CheckBoxInput("Stage", ['CodeBuild', 'CodeDeploy'], "stage", optional=True),
            CheckBoxInput("Auto Scaling Group", ['Exist'], "asg", optional=True),
            PlainTextInput("ASG or EC2 Name", multiline=True, optional=True),
            MarkDown("*Due*"),
            DatePicker("Select a date"),
            TimePicker("Select time"),
            PlainTextInput("Anything else you want to tell us?")
        )
    )
    import pdb;pdb.set_trace();
    print(view.body)
