from typing import List, Set

def remove_invalid_parentheses(expr: str) -> List[str]:
    # how many ( ) to remove
    remL = remR = 0
    for ch in expr:
        if ch == '(':
            remL += 1
        elif ch == ')':
            if remL > 0:
                remL -= 1
            else:
                remR += 1

    res: Set[str] = set()
    n = len(expr)

    def backtrack(i: int, cur: list, balance: int, remL: int, remR: int):
        # irepresents current index in expresssion and cur is list of chosen character
        if i == n:
            if balance == 0 and remL == 0 and remR == 0:
                res.add("".join(cur))
            return

        ch = expr[i]

        # Opt 1: remove this parenthesis if allowed
        if ch == '(' and remL > 0:
            backtrack(i + 1, cur, balance, remL - 1, remR)
        elif ch == ')' and remR > 0:
            backtrack(i + 1, cur, balance, remL, remR - 1)

        # Opt 2: keep this character
        if ch != '(' and ch != ')':
            cur.append(ch) # always keep letters
            backtrack(i + 1, cur, balance, remL, remR)
            cur.pop()
        elif ch == '(':
            cur.append(ch) # keep ( and increase the balance
            backtrack(i + 1, cur, balance + 1, remL, remR)
            cur.pop()
        else: 
            # can only keep ) if ( is ther
            if balance > 0:
                cur.append(ch)
                backtrack(i + 1, cur, balance - 1, remL, remR)
                cur.pop()

    backtrack(0, [], 0, remL, remR)
    return list(res) if res else [""]

# ... (your remove_invalid_parentheses function goes here) ...

def run_tests():
    test_cases = [
        # Case 1: Standard case with multiple solutions
        {
            "expr": "()())()",
            "desc": "Unbalanced closing parenthesis",
            "expected_examples": ["(())()", "()()()"]
        },
        # Case 2: Expression with letters (should be preserved)
        {
            "expr": "(a)())()",
            "desc": "Letters inside parentheses",
            "expected_examples": ["(a())()", "(a)()()"]
        },
        # Case 3: Completely invalid (Result should be empty string)
        {
            "expr": ")(",
            "desc": "Start with close, end with open",
            "expected_examples": [""]
        },
        # Case 4: Already valid
        {
            "expr": "((a))",
            "desc": "Already valid expression",
            "expected_examples": ["((a))"]
        },
        # Case 5: Empty string
        {
            "expr": "",
            "desc": "Empty input",
            "expected_examples": [""]
        }
    ]

    print(f"{'Description':<30} | {'Input':<15} | {'Result'}")
    print("-" * 80)

    for test in test_cases:
        result = remove_invalid_parentheses(test["expr"])
        
        # Sort for consistent display since set order is random
        result.sort()
        
        print(f"{test['desc']:<30} | {test['expr']:<15} | {result}")

if __name__ == "__main__":
    run_tests()