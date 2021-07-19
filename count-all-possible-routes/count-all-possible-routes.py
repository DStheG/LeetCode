class Solution:
    def __init__(self):
        self.result = 0

    def recurSol(self, locations: List[int], cur: int, dest: int, fuel: int) -> int:
        if (cur == dest):
            self.result += 1
        if (fuel == 0):
            return

        for i in range(len(locations)):
            if (i != cur):
                newFuel = fuel - abs(locations[i] - locations[cur])
                if (newFuel >= 0):
                    self.recurSol(locations, i, dest, newFuel)
        
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.recurSol(locations, start, finish, fuel)
        return self.result
    

        