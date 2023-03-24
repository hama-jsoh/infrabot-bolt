import json


class Element(metaclass=ABCMeta):
    def __init__(self) -> None:
        if type(self) is Element:
            raise Exception(
                "Element is an abstract class and cannot be instantiated directly"
            )

	@property
	def to_dict(self) -> dict:
		return self.body

	@property
	def pretty(self) -> None:
		return print(
			json.dumps(
				self.body, ensure_ascii=False, indent=4
			)
		)
