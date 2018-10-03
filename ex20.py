from sys import argv

script, filein = argv

def printall(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def printaline(linenum, f):
    print(linenum, f.readline(), end="")
            
print("ok openin a file")

fileinn = open(filein)

#readin it all
printall(fileinn)

#rewind
rewind(fileinn)

curline = 1
printaline(curline, fileinn)
curline += 1
printaline(curline, fileinn)
curline += 1
printaline(curline, fileinn)
