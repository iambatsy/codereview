class ThrusterController:
    def __init__(self):
        self.thrusters ={
            "thruster_1" :0,
            "thruster_2" :0,
            "thruster_3" :0,
            "thruster_4" :0,
        }
        self.directions = {
            "forward": ["thruster_1", "thruster_2"],
            "backward": ["thruster_3", "thruster_4"],
            "left": ["thruster_1", "thruster_3"],
            "right": ["thruster_2", "thruster_4"]
        }
    def set_power(self,thruster_x,power):
        if (power<0 or power>100):
            raise ValueError("power out of bounds")
        self.thrusters[thruster_x]=power
        print(f"{thruster_x} power is {power}%")
    def get_power(self,thruster_x):
        return self.thrusters[thruster_x]

    def set_all_thrusters(self,power):
        if (power<0 or power>100):
            raise ValueError("power out of bounds")
        for thruster_x in self.thrusters:
            self.thrusters[thruster_x]=power
            print(f"all thusters set to {power}")
    
    def set_directions(self,direction,power):
                for thruster_x in self.directions[direction]:
                    self.thrusters[thruster_x]=power
                    print(f"{thruster_x} set to {direction} at {power}")
    def stop(self):
        for thruster_x in self.thrusters:
            self.thrusters[thruster_x]=0
            print("all thrusters stopped")

    
if __name__ == "__main__":
    controller = ThrusterController()
    controller.set_power("thruster_1", 75)
    controller.set_all_thrusters(50)
    print(controller.get_power("thruster_2"))
    controller.set_directions("forward", 60)
    
    

    
   
        
        

