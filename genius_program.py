# Part 1: Design Your Own Class (The `Inventor` Class)

class Inventor:
    """
    A base class representing an inventor.
    """
    def __init__(self, name, famous_for):
        self.name = name
        self.famous_for = famous_for

    def display_contribution(self):
        """Prints the inventor's name and contribution."""
        print(f"{self.name} is renowned for their work on {self.famous_for}.")

    def innovate(self):
        """A generic method for the act of innovation."""
        print(f"{self.name} is currently innovating...")

# Part 2: Polymorphism Challenge (Inheritance and `create()` method)

class Einstein(Inventor):
    """
    A class representing Albert Einstein, inheriting from Inventor.
    Demonstrates polymorphism through the create() method.
    """
    def __init__(self, name, famous_for):
        super().__init__(name, famous_for)
        self.theory = "Theory of Relativity"

    def innovate(self):
        """Overridden method to represent Einstein's innovation."""
        print(f"{self.name} is developing new theories on physics.")

    def create(self):
        """Specific polymorphic method for Einstein."""
        print(f"[{self.name}] is formulating the {self.theory}!")

class Oppenheimer(Inventor):
    """
    A class representing J. Robert Oppenheimer.
    Demonstrates polymorphism through the create() method.
    """
    def __init__(self, name, famous_for):
        super().__init__(name, famous_for)
        self.project = "The Manhattan Project"

    def innovate(self):
        """Overridden method for Oppenheimer's innovation."""
        print(f"{self.name} is leading a team of brilliant minds.")

    def create(self):
        """Specific polymorphic method for Oppenheimer."""
        print(f"[{self.name}] is building a new scientific device for {self.project}.")


class Tesla(Inventor):
    """
    A class representing Nikola Tesla.
    Demonstrates polymorphism through the create() method.
    """
    def __init__(self, name, famous_for):
        super().__init__(name, famous_for)
        self.invention = "AC electricity"

    def innovate(self):
        """Overridden method for Tesla's innovation."""
        print(f"{self.name} is experimenting with electrical currents.")

    def create(self):
        """Specific polymorphic method for Tesla."""
        print(f"[{self.name}] is demonstrating the power of {self.invention}.")


# Main program to demonstrate polymorphism
if __name__ == "__main__":
    # Create a list of different inventor objects
    renowned_scholars = [
        Einstein("Albert Einstein", "the Theory of Relativity"),
        Oppenheimer("J. Robert Oppenheimer", "the Manhattan Project"),
        Tesla("Nikola Tesla", "AC electricity and wireless power")
    ]

    # Iterate through the list and call the same method (`create()`)
    # on each object. The behavior is different for each object,
    # showcasing polymorphism.
    for scholar in renowned_scholars:
        scholar.display_contribution()
        scholar.innovate()  # Demonstrate overridden method
        scholar.create()    # Demonstrate polymorphism
        print("-" * 30)