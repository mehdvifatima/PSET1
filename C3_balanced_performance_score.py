from typing import List

class Solution:
    def median_sort(self, scoresA: List[int], scoresB: List[int])-> float:
        m,n = len(scoresA), len(scoresB)
        total = m+n

        mid1 = (total - 1) // 2       
        mid2 = total // 2                

        i = j = 0
        #k represent the no. of elements being shwn
        k = 0                           
        mid_val1 = mid_val2 = 0

        while k <= mid2:
            if i < m and (j >= n or scoresA[i] <= scoresB[j]):
                val = scoresA[i]
                i += 1
            else:
                val = scoresB[j]
                j += 1

            if k == mid1:
                mid_val1 = val
            if k == mid2:
                mid_val2 = val
            k += 1
        if total % 2 == 1:
            return float(mid_val2)
        else:
            return (mid_val1 + mid_val2) / 2.0


solver = Solution()
result = solver.median_sort(scoresA=[1, 2], scoresB=[3, 4])
print(f"Median: {result}")       


