class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [[target - position[i], speed[i]] for i in range(n)]
        cars.sort(key=lambda car: car[0])
        fleets = 1
        time = cars[0][0] / cars[0][1]
        for j in range(1, n):
            if cars[j][0] / cars[j][1] > time:
                time = cars[j][0] / cars[j][1]
                fleets += 1
        return fleets