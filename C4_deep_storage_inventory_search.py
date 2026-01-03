from typing import List

def kth_smallest_binary(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    low, high = matrix[0][0], matrix[n - 1][n - 1]

    def count_leq(x: int) -> int:
        count = 0
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= x:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    while low < high:
        mid = (low + high) // 2
        if count_leq(mid) >= k:
            high = mid
        else:
            low = mid + 1

    return low
