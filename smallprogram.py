
numbers = list(range(1, 101))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


output = []
for num in reversed(numbers):
    if is_prime(num):
        continue 
    if num % 3 == 0 and num % 5 == 0:
        output.append("FooBar")
    elif num % 3 == 0:
        output.append("Foo")
    elif num % 5 == 0:
        output.append("Bar")
    else:
        output.append(str(num))

output_string = ", ".join(output)
print(output_string+", %")
