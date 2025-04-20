class MixinInfoClass:

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.description}'," f" {self.price}, {self.quantity})"

    # def __init__(self):
    #     print(self.__repr__())
