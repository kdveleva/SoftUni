# from project_gym.customer import Customer
#
# customer1 = Customer("John", "Maple Street", "john.smith@gmail.com")
# customer2 = Customer("Ivan", "Down Street", "ivan.ivanov@gmail.com")
# customer3 = Customer("Petur", "Up Street", "petur.ivanov@gmail.com")
# print(customer1)
# print(customer2)
# print(customer3)
#
#
# from project_gym.equipment import Equipment
#
# equipment1 = Equipment("Treadmill")
# equipment2 = Equipment("Rope")
# equipment3 = Equipment("Ball")
# print(equipment1)
# print(equipment2)
# print(equipment3)
#
# from project_gym.exercise_plan import ExercisePlan
#
# plan = ExercisePlan(1, 1, 20)
# plan2 = ExercisePlan.from_hours(2,2,1)
# plan3 = ExercisePlan(1, 1, 5)
# print(plan)
# print(plan2)
# print(plan3)
#
# from project_gym.subscription import Subscription
#
# subscription = Subscription("14.05.2020", 1, 1, 1)
# subscription2 = Subscription("01.05.2021", 2, 2, 2)
# subscription3 = Subscription("03.12.2020", 3, 3, 3)
# print(subscription)
# print(subscription2)
# print(subscription3)
#
# from project_gym.trainer import Trainer
#
# trainer1 = Trainer("Peter")
# trainer2 = Trainer("Zorba")
# trainer3 = Trainer("Mark")
# print(trainer1)
# print(trainer2)
# print(trainer3)
#
# from project_gym.gym import Gym
# gym = Gym()
# gym.add_customer(customer1)
# gym.add_customer(customer2)
# gym.add_customer(customer3)
#
# gym.add_equipment(equipment1)
# gym.add_trainer(trainer1)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
# gym.add_subscription(subscription2)
#
# print(gym.subscription_info(2))


from project_gym.customer import Customer
from project_gym.equipment import Equipment
from project_gym.exercise_plan import ExercisePlan
from project_gym.gym import Gym
from project_gym.subscription import Subscription
from project_gym.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
