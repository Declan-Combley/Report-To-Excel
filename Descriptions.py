EMPTY: str = ""

class Descriptor:
    def __init__(self, value: str = EMPTY, action: str = EMPTY, colour: str = EMPTY) -> None:
        self.value: str = value
        self.action: str = action
        self.colour: str = colour


class Default(Descriptor):
    def __init__(self) -> None:
        super().__init__(EMPTY, EMPTY, EMPTY)

class Bad(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "RED")

class Poor(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "YELLOW")

class Good(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "LIGHTGREEN")

class VeryGood(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "GREEN")

class Excellent(Descriptor):
    def __init__(self, value: str, action: str) -> None:
        super().__init__(value, action, "DARKGREEN")
