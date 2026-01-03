def toh(n: int, from_rod: str, to_rod: str, aux_rod: str):
    if n == 0:
        return
    
    toh(n - 1, from_rod, aux_rod, to_rod) #moving top disk to separate rod
    
    print(f"Disk {n} moved from {from_rod} to {to_rod}") #moving nth disk target rod
    toh(n - 1, aux_rod, to_rod, from_rod) #move n-1 disks from separate to target
#test cases are provided down
def run_test(n:int):
    print(f"\n=== Input: {n} ===")
    toh(n, 'A', 'C', 'B')
    print()

if __name__ == "__main__":
    run_test(2)
    run_test(3)
    run_test(4)
    run_test(1) 
