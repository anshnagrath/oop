class Leg:
    pass

class Back:
    pass

class Chair:
    def __init__(self, num_legs):
        self.Legs  = [Leg() for leg in range(num_legs)]
        self.back  = Back()
    def __repr__(self):
        return 'I have {} legs and one back'.format(len(self.Legs)) 

print(Chair(5))
           