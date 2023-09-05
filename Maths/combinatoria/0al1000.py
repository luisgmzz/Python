nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def tienen_en_comun(n: str, m: str)->bool:
    for i in n:
        if i in m:
            return True
    return False

for i in range(9, 100):
    for j in nums:
        if not (a:=tienen_en_comun(str(i), str(j))):
            nums.append(i)
        

print(nums)

