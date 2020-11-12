from typing import List
from project_Zoo.animal_base import AnimalBase
from project_Zoo.caretaker import Caretaker
from project_Zoo.cheetah import Cheetah
from project_Zoo.keeper import Keeper
from project_Zoo.staff_base import StaffBase
from project_Zoo.lion import Lion
from project_Zoo.tiger import Tiger
from project_Zoo.vet import Vet


class Zoo:
    __animal_capacity: int
    __workers_capacity: int
    __budget: int
    name: str
    animals: List
    workers: List

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: AnimalBase, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__animal_capacity >= len(self.animals) and self.__budget < price:
            return f"Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: StaffBase) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        if worker_name in [x.name for x in self.workers]:
            self.workers = [x for x in self.workers if x.name != worker_name]
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([x.salary for x in self.workers])
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_needs = sum([x.get_needs() for x in self.animals])
        if total_needs <= self.__budget:
            self.__budget -= total_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [x for x in self.animals if isinstance(x, Lion)]
        tigers = [x for x in self.animals if isinstance(x, Tiger)]
        cheetahs = [x for x in self.animals if isinstance(x, Cheetah)]
        NEW_LINE = "\n"
        return f"""You have {len(self.animals)} animals
----- {len(lions)} Lions:
{NEW_LINE.join(str(x) for x in lions)}
----- {len(tigers)} Tigers:
{NEW_LINE.join(str(x) for x  in tigers)}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(str(x) for x in cheetahs)}"""

    def workers_status(self):
        keepers = [x for x in self.workers if isinstance(x, Keeper)]
        caretakers = [x for x in self.workers if isinstance(x, Caretaker)]
        vets = [x for x in self.workers if isinstance(x, Vet)]
        NEW_LINE = "\n"
        return f"""You have {len(self.workers)} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(str(x) for x in keepers)}
----- {len(caretakers)} Caretakers:
{NEW_LINE.join(str(x) for x in caretakers)}
----- {len(vets)} Vets:
{NEW_LINE.join(str(x) for x in vets)}"""