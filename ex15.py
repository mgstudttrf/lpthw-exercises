from sys import argv
script, filename = argv
txt = open(filename)

print(f"the contents of {filename} gile are")
print(txt.read())
print("now type that filename thyself")
filename2 = input(">")
txt2 = open(filename2)
print(f"u wanted to open {filename2} and here it is")

print(txt2.read())
txt.close()
txt2.close()
