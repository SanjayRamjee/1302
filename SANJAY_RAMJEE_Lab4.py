def tribonacci(n, memory = {}):
    if n in memory:
        return memory[n]
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1 
    
    else:
        result = tribonacci(n-1,  memory) + tribonacci(n-2, memory) + tribonacci(n-3, memory)
        memory[n] = result
        return result

print(tribonacci(0))
print(tribonacci(1))
print(tribonacci(2))
print(tribonacci(6))
print(tribonacci(10))
print(tribonacci(33))
        
