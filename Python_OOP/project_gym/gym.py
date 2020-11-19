from typing import List

from project_gym.customer import Customer
from project_gym.equipment import Equipment
from project_gym.exercise_plan import ExercisePlan
from project_gym.subscription import Subscription
from project_gym.trainer import Trainer


class Gym:
    customers: List[Customer] = []
    trainers: List[Trainer] = []
    equipment: List[Equipment] = []
    plans: List[ExercisePlan] = []
    subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [x for x in self.subscriptions if x.id == subscription_id][0]
        customer = f"{[x for x in self.customers if x.id == subscription.customer_id][0]}\n"
        trainer = f"{[x for x in self.trainers if x.id == subscription.trainer_id][0]}\n"
        plan = [x for x in self.plans if x.id == subscription.exercise_id][0]
        equipment = f"{[x for x in self.equipment if x.id == plan.equipment_id][0]}\n"

        return "".join(str(subscription) + "\n" + customer + trainer + equipment + plan.__repr__())
