from typing import List

def team_impact(contributions:List[int])->List[int]:
    n=len(contributions)
    impact=[1]*n

# Left products
    left_prod = 1
    for i in range(n):
        impact[i] = left_prod
        left_prod *= contributions[i]

# Right products
    right_prod = 1
    for i in range(n-1,-1,-1):
        impact[i] *= right_prod
        right_prod *= contributions[i]

    return impact
