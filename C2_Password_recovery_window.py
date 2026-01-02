from collections import Counter

def min_window(log: str, pattern: str)-> str:
    if not log or not pattern:
        return ""

  # requiredcounts for character
    need = Counter(pattern)          
   #window coiunt
    have = {}      
     # numbers of distinct character needed                  
    required = len(need)          
    # HOW MANY distinct char are satisfied
    formed = 0                       

    min_len = float("inf")
    min_l = 0

    l = 0
    for r, ch in enumerate(log):
        # expanding
        have[ch] = have.get(ch, 0) + 1

        if ch in need and have[ch] == need[ch]:
            formed += 1

        # contracting
        while formed == required:
            window_len = r - l + 1
            if window_len < min_len:
                min_len = window_len
                min_l = l

            left_ch = log[l]
            have[left_ch] -=1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -=1
            l= l+ 1

    if min_len == float("inf"):
        return ""
    return log[min_l:min_l + min_len]



