if __name__ == "__main__":
    class Animal:
        def __init__(self, name: str, species: str):
            """
            name: имя животного
            :param species: вид животного
            """
            self.name = name
            self.species = species

        def __str__(self):

            return f"{self.name} is a {self.species}"

        def __repr__(self):

            return f"Animal('{self.name}', '{self.species}')"


    class Lion(Animal):
        def __init__(self, name: str, species: str = "Lion", area: str = "Africa"):
            """
            name: Имя Льва
            species: Вид льва
            area: Место обитания льва
            """
            super().__init__(name, species)
            self._area = area

        def __str__(self):

            return f"{self.name} is a {self.species} from {self._area}"

        def __repr__(self):

            return f"Lion('{self.name}', '{self.species}', '{self._area}')"

        def roar(self) -> str:

            return "Roar!"

        def show_kingdom(self) -> str:

            return self._area
    pass
