class Sheep:
    
    def __init__(self, arm_length, leg_length, eye_count, has_tail, is_furry):
       
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.eye_count = eye_count
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe_animal(self):
        
        tail_status = "has a tail" if self.has_tail else "does not have a tail"
        fur_status = "is furry" if self.is_furry else "is not furry"

        print("-Sheep-")
        print(f"Arm length: {self.arm_length} inches")
        print(f"Leg length: {self.leg_length} inches")
        print(f"Number of eyes: {self.eye_count}")
        print(f"This animal {tail_status}.")
        print(f"This animal {fur_status}.")


my_sheep = Sheep(arm_length=6.0, leg_length=6.0, eye_count=2, has_tail=True, is_furry=True)


my_sheep.describe_animal()