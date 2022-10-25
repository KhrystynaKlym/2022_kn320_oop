class Animal:
    def __init__(self, name:str, mass) -> None:
        assert name.isascii(), "Значення name повинно містити символи таблиці ASCII"
        self.name = name
        # Можна assert замінити на IF
        if isinstance(mass, float):
            self.mass = mass
        else:
            raise AssertionError("Маса має бути введена цифрами")

a = Animal("Monkey", 40.5)
print(a.name, a.mass)

def test_pass():
    pass