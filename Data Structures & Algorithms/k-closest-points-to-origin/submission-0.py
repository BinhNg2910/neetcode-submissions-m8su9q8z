class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Idea: bruteforce solution calculate all distance then sort by distance and get the k smallest distance
        TC:
        SC:
        """
        pointsDist = [[point, pow(point[0], 2) + pow(point[1], 2)] for point in points]
        # print(pointsDist)
        pointsDist.sort(key=lambda x: x[1]) # sort by distance
        # print(pointsDist)
        # print([pointsDist[i][0] for i in range(k)])
        return [pointsDist[i][0] for i in range(k)]