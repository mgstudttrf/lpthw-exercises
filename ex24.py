print("nlahblah\\ \tblah")
print('blah\\\\\tblah\'')

poem = """
rose r red
violets blue
blah\n blah
"""

print("-------")
print(poem)
print("----------")

five = 2+3-4/4*5+5

print(f"this shud be five {five}")

def randomformula(start):
    a = 12 * start
    b = 3 + start
    c = 34 % start
    return a, b, c

r1, r2, r3 = randomformula(100)

print("with start eq {}".format(100))
print(f"this yields {r1}, {r2}, {r3}")

form  = randomformula(10)
print("with 10. it yields {}, {}, {}".format(*form))

