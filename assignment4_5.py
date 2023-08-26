def prime(no):
    if no <= 1:
        return False
    if no <= 3:
        return True
    if no % 2 == 0 or no % 3 == 0:
        return False
    i = 5
    while i * i <= no:
        if no % i == 0 or no % (i + 2) == 0:
            return False
        i = i + 6
    return True

def increase(no):
    return no * 2

def maximum(Arr):
    max_element = Arr[0]
    for i in range(1, len(Arr)):
        if Arr[i] > max_element:
            max_element = Arr[i]
        return max_element

def filterX(task, elements):
    result = []
    for no in elements:
        if task(no) == True:
            result.append(no)
    return result

def mapX(task, elements):
    result = []
    for no in elements:
        ret = task(no)
        result.append(ret)
    return result

def reduceX(Task,Elements):
    sum=0
    for no in Elements:
        sum=Task(sum,no)
    return sum

def main():
    a = []
    print("Enter the number of elements:", end="")
    size = int(input())
    print("Enter the numbers:")
    for i in range(size):
        num = int(input())
        a.append(num)
    
    output = list(filterX(prime, a))
    print("Filter:", output)
    output1 = list(mapX(increase, output))
    print("Map:", output1)
    output2 = reduceX(lambda x, y: x if x > y else y, output1)
    print("Reduce:", output2)

if __name__ == "__main__":
    main()
