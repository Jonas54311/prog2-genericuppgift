from typing import TypeVar, Generic
T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

class Stack(Generic[T]):
    def __init__(self):
        self.items = []

    def push(self, item: T):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class Weapon():
    def __init__(self, damage: int):
        self.damage = damage

class Potion():
    def __init__(self, heal_amount: int):
        self.heal_amount = heal_amount

class Backpack(Generic[T]):
    def __init__(self):
        self.items = []

    def add_item(self, item: T):
        self.items.append(item)

    def use_first_item(self) -> T:
        return self.items.pop(0)

class Character():
    def __init__(self, name: str):
        self.name = name

    def speak(self, phrase: str):
        print(phrase)

class Party(Generic[T]):
    def __init__(self):
        self.members = []

    def add_member(self, member: T):
        self.members.append(member)

    def get_leader(self) -> T:
        return self.members[0]