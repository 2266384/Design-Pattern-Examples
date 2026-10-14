from dataclasses import dataclass, field
from typing import Self

# Create a custom Duck class with a set of default attributes
@dataclass
class Duck:
    name: str
    colour: str = "white"
    sound: str = "quack"
    can_fly: bool = True
    accessories: list[str] = field(default_factory=list)

    # Describe method that returns the details of the duck object
    def describe(self) -> str:
        return (
            f"{self.name} is {self.colour}, "
            f"says '{self.sound}', "
            f"can fly: {self.can_fly}, "
            f"accessories: {self.accessories}"
        )

# Define the RubberDuck class which extends the basic Duck class
@dataclass
class RubberDuck(Duck):
    floats: bool = True
    squeak_volume: int = 5



# Define the core DuckBuilder and its default attributes
class DuckBuilder:
    def __init__(self, name: str):
        self._name = name
        self._colour = "white"
        self._sound = "quack"
        self._can_fly = True
        self._accessories = []

    # Functions that allow the attributes to be set individually for each Duck object
    def colour(self, colour: str) -> "DuckBuilder":
        self._colour = colour
        return self

    def sound(self, sound: str) -> "DuckBuilder":
        self._sound = sound
        return self

    def can_fly(self, can_fly: bool) -> "DuckBuilder":
        self._can_fly = can_fly
        return self

    def add_accessory(self, accessory: str) -> "DuckBuilder":
        self._accessories.append(accessory)
        return self

    def _core_attributes(self) -> dict:
        return {
            "name": self._name,
            "colour": self._colour,
            "sound": self._sound,
            "can_fly": self._can_fly,
            "accessories": self._accessories.copy(),
        }

    def build(self) -> Duck:
        return Duck(**self._core_attributes())



# Extended builder for RubberDuck class
class RubberDuckBuilder(DuckBuilder):
    def __init__(self, name: str):
        super().__init__(name)      # Inherits the features and functions from the superclass
        self._floats = True
        self._squeak_volume = 5

    def floats(self, floats: bool) -> Self:
        self._floats = floats
        return self

    def squeak_volume(self, volume: int) -> Self:
        if not 0 <= volume <= 10:
            raise ValueError("Volume must be between 0 and 10")
        self._squeak_volume = volume
        return self

    def build(self) -> RubberDuck:
        return RubberDuck(
            **self._core_attributes(),
            floats=self._floats,
            squeak_volume=self._squeak_volume,
        )



# Build a standard duck.
standard_duck = DuckBuilder("Donald").build()


# Build a customised duck.
fancy_duck = (
    DuckBuilder("Daisy")
    .colour("pink")
    .sound("squeak")
    .can_fly(False)
    .add_accessory("hat")
    .add_accessory("bow")
    .build()
)


# Build a rubber duck
rubber_duck = (
    RubberDuckBuilder("Scrooge")
    .colour("yellow")
    .sound("ack")
    .can_fly(False)
    .add_accessory("hat")
    .add_accessory("cane")
    .add_accessory("money bin")
    .floats(True)
    .squeak_volume(8)
    .build()
)


# Print the details of the duck objects to the screen
print(standard_duck.describe())
print(fancy_duck.describe())
print(rubber_duck.describe())
