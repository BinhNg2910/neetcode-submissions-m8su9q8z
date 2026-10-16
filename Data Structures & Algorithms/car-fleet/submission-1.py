class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        t1 = 7/3 = 2.3 t2 = 5
        Idea: calculate the completion time to the destinaton of each car 
        - sort the car with position
        TC: O(n + nlogn + n) = O(nlogn)
        SC: O(n)
        """
        n = len(position) # number of car
        positionTime = [(position[i], (target - position[i]) / speed[i]) for i in range(n)]
        # print(positionTime)
        positionTime.sort(key = lambda x:x[0])
        # print(positionTime)
        
        carFleet = 1
        trapCar = positionTime[-1][1]
        for i in range(n-2, -1, -1):
            if positionTime[i][1] > trapCar:
                carFleet += 1
                trapCar = positionTime[i][1]
        return carFleet
            