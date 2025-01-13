from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            counter = 0
            for j, tempj in enumerate(temperatures[i:]):
                if tempj > temp:
                    days[i] = counter
                    break
                else:
                    counter += 1
        
        return days

        