from sys import argv

script, filename = argv

print("were about to truncate a file")
print("unsure then hit ctrl-c")
print("else hit ret")

input("?")

print(f"openin {filename}..")
target = open(filename, "w")

print("truncatin it..")
target.truncate()

print("now put three new lines for the file")
line1=input("line1>")
line2= input("line2>")
line3= input("line3>")

print(f"writin them to {filename}")

target.write(line1)
target.write(line2)
target.write(line3)

target.close()

target = open(filename)
print("checkin contents again..")
print(target.read())

