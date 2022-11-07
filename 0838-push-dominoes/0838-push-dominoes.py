class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dists = [0] * len(dominoes)

        currDist = 0
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                currDist = len(dominoes)
            elif dominoes[i] == "L":
                currDist = 0
            else:
                currDist = max(currDist - 1, 0)
            dists[i] += currDist

        currDist = 0
        for i in reversed(range(len(dominoes))):
            if dominoes[i] == "L":
                currDist = len(dominoes)
            elif dominoes[i] == "R":
                currDist = 0
            else:
                currDist = max(currDist - 1, 0)
            dists[i] -= currDist

        res = []
        for dist in dists:
            if dist == 0:
                res.append(".")
            elif dist > 0:
                res.append("R")
            else:
                res.append("L")

        return "".join(res)