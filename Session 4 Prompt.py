class Dolphin:

    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length      
        self.leg_length = leg_length      
        self.num_eyes = num_eyes          
        self.has_tail = has_tail          
        self.is_furry = is_furry          

    def describe(self):
        print(f"Dolphin Characteristics:")
        print(f"Arm (Fin) Length: {self.arm_length} meters")
        print(f"Leg Length: {self.leg_length} meters")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has a Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")

def main():
    my_dolphin = Dolphin(arm_length=0.5, leg_length=0.0, num_eyes=2, has_tail=True, is_furry=False)
    
    my_dolphin.describe()

main()