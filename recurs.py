def digit(f):
    counter = 0
    save = 0
    nums = str(f)
    while counter < len(nums):
        save += int(nums[counter])
        counter += 1
    print(save)

def add(n):
    answer = 0
    while n >= 0:
        answer+=n
        n-=1
    print(answer)

def pow(n, e):
    while e >= 0:
        n*=n
        e=-1
    print(n)
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)


digit(2962)
add(8)
pow(2,3)
print(factorial(4))
