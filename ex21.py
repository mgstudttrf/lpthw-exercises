def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

age = add(20,20)
height = sub(100,4)
weight = mul(3883, 3)
iq = div(10, 10)

print(f"{age} {height} {weight} {iq}")

what = add(age, sub(height, mul(weight, div(iq, 228))))

print(f"what is {what}")
