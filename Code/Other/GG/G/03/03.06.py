from typing import List


class AnimalShelf:

    def __init__(self):
        self.stackCat = []
        self.stackDog = []

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.stackCat.append(animal)
        else:
            self.stackDog.append(animal)

    def dequeueAny(self) -> List[int]:
        if not self.stackCat and not self.stackDog:
            return [-1, -1]
        elif not self.stackCat:
            return self.stackDog.pop(0)
        elif not self.stackDog:
            return self.stackCat.pop(0)
        else:
            return self.stackCat.pop(0) if self.stackCat[0][0] < self.stackDog[0][0] else self.stackDog.pop(0)

    def dequeueDog(self) -> List[int]:
        return self.stackDog.pop(0) if self.stackDog else [-1, -1]

    def dequeueCat(self) -> List[int]:
        return self.stackCat.pop(0) if self.stackCat else [-1, -1]
