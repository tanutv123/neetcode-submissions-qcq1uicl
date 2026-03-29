class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            if gas[i] - cost[i] < 0:
                continue
            
            j = (i + 1) % n
            currentGas = gas[i] - cost[i]
            while j != i and currentGas >= 0:
                currentGas = currentGas + gas[j] - cost[j]
                j += 1
                j %= n
            if j == i and currentGas >= 0:
                return i

        return -1           