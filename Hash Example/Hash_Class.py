import Functions

class HashClass:
    message = ""
    hash = ""

    def __init__(self, message = "_BLANK_", hash = "ERROR"):
        self.message = message
        self.hash = hash

    def setMessage(self, message):
        self.message = message
    
    def computeHash(self):
        "Place all computes here"


def hexcount(mem):
    hexes = "0123456789abcdef"
    hexDict = dict()

    for x in hexes:
        hexDict[x] = 0

    for x in mem:
        hexDict[x] += 1

    for x, y in hexDict.items():
        print(x, " - ", y, "\t", end=" ")
    return hexDict
'''m1 = "This little lite of mine"
h1 = "k32kago3in2"
HC = HashClass()'''


'''print("\nEqual") if(a == 'a') else print("\nNot Equal")'''

'''
print(HC.message)
print(HC.hash)

'HC.setHash(h1)'
'HC.setMessage(m1)'

HC = HashClass(m1, h1)

print(HC.message)
print(HC.hash)
'''


'''mem = "\nJevin Evans\n J3v1n 3van5\n  Jev1^ Ev@n$\n   J3v1^ 3V@^$"'''
mem = "Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string."
Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
azList = dict()
count = 0


####################Test 1
# matches = list()
# for x in range(len(Uppercase)):
#     m = Functions.makeHash(Uppercase[x])
#     if m not in matches:
#         # print(m)
#         matches.append(m)
#     else:
#         print("Dupilcated Found")
# print()
# for x in matches:
#     print(x)
# print(len(matches))
###############

# ##### Code for length test
for x in range(len(Uppercase)):
    # if Uppercase[0:x] == "": continue
    azList[Uppercase[0:x+1]] = Functions.makeHash(Uppercase[0:x+1])

print(count)
azHashes = list()

for x, y in azList.items():
    print(x, y)
    azHashes.append(y)
#####

hexlist = list("0123456789abcdef")
print(hexlist)
for x in azHashes:
   hdic = hexcount(x)
   print("\n\n")
# ############################    

Functions.makeHash("Rendall!") 
Functions.makeHash("!lladneR") 

m = Functions.shuffle("35f8dde010ad03116c5fa4a46cf5d91b")
print(m , len(m))
# temp = Functions.makeHash(" Jevin Evans ")
# temp = Functions.makeHash(" Jevin Evans")
# temp = Functions.makeHash(" Evans Jevin ")
# temp = Functions.makeHash(" EJveavnisn ")
# temp = Functions.makeHash("  EJveavnisn  ")
# qbf = Functions.makeHash("The quick fox jumps over the lazy brown dog")
# Functions.makeHash(mem)

'''
for x in azList:
    Functions.getLowercase(azList[x])
    Functions.getNumbers(azList[x])
    print(Functions.num_of_LowerCase())
    print(Functions.num_of_Numbers())
    Functions.restart()
'''
'''
Fix Letters recognition. If the same letters are sent the same hash is produced

add trigraph and digraphs functions

 Work on make_128()
    Greater than part
        - contains a lot of F's for some reason, possibly fix that
        - does not work well with the shuffle because of the F's either change way that the shuffle work or rework bit operations
    
    Less than part
        - the added part is too short and have to find some way to expand or permutate the less than part
'''