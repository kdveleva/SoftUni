class ExercisePlan:
    trainer_id: int
    equipment_id: int
    duration: int
    auto_incremented_id: int = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int ):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.auto_incremented_id
        ExercisePlan.auto_incremented_id += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        hours = hours * 60
        return cls(trainer_id, equipment_id, hours) # Note it may have to be converted in mins

    @staticmethod
    def get_next_id():
        return ExercisePlan.auto_incremented_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
