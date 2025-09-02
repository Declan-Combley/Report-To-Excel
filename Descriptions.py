class Descriptor:
    def __init__(self, value: str, action: str, colour: str) -> None:
        self.value: str = value
        self.action: str = action
        self.colour: str = colour


class Default(Descriptor):
    def __init__(self) -> None:
        super().__init__("Default", "Default", "Default")

class Bad(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "red")

class Poor(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "yellow")

class Good(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "lightgreen")

class VeryGood(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "green")

class Excellent(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "darkgreen")

