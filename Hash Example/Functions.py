'''Variables for Information'''
Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase = 'abcdefghijklmnopqrstuvwxyz'
Specials = "`~@#$%^&*+={}|\\<>"
Punctuations = ".,:;?()[]\"\'!_-/"
Vowels = "aeiouAEIOU"
Consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
Digits = "0123456789"
HexLetter = "0123456789abcdef"
digraphs = ['ai', 'al', 'an', 'ar', 'as', 'at', 'au', 'aw', 'ay', 'bl', 'ch', 'ck', 'cl', 'cr', 'dr', 'ea', 'ed', 'ee', 'ei', 'en', 'er', 'es', 'et', 'eu', 'ew', 'ey', 'fl', 'fr', 'gh', 'gl', 'gr', 'ha', 'he', 'ie', 'in', 'is', 'it', 'nd', 'ng', 'nt', 'of', 'oi', 'on', 'oo', 'or', 'ou', 'ow', 'oy', 'ph', 'pl', 'pr', 'qu', 're', 'sc', 'se', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'te', 'th', 'ti', 'to', 'tr', 'tw', 'wh', 'wr']
trigrahs = ['nth', 'sch', 'scr', 'shr', 'spl', 'spr', 'squ', 'str', 'thr', 'the', 'and', 'ing', 'ent', 'ion', 'her', 'for', 'tha', 'int', 'ere', 'tio', 'ter', 'est', 'ers', 'ati', 'hat', 'ate', 'all', 'eth', 'hes', 'ver', 'his', 'oft', 'ith', 'fth', 'sth', 'oth', 'res', 'ont']
multiplier = 0
messageLength = 0

'''Dictionaries'''
Numbers = dict()
Punctuations_Chars = dict()
Special_Chars = dict()
Lower_Letters = dict()
Upper_Letters = dict()
Hex_Letters = dict()
  
for x in range(len(Uppercase)):
        Upper_Letters[Uppercase[x]] = 0

for x in range(len(Lowercase)):
        Lower_Letters[Lowercase[x]] = 0

for x in range(len(Specials)):
        Special_Chars[Specials[x]] = 0

for x in range(len(Punctuations)):
        Punctuations_Chars[Punctuations[x]] = 0

for x in range(len(Digits)):
        Numbers[Digits[x]] = 0

for x in range(len(HexLetter)):
        Hex_Letters[HexLetter[x]] = 0

'''
Functions to Add for Hash
        [- mod of 128 of total length to use as multiplier]
        - converting certain certain amount of letters to numbers or numbers to letters based on either constant or exponential based on number
        - Add to cound number of sentences

        - Method to count similar letter combinations like i before e, i before c, qu, etc.
        [- Method to restart the dictionaries for a new hash]
        - method to create string for hash
        - method/lookup table for has converstions (unchangeable/unmovable set)
'''
'''Might Consider condensing some functions that do similar things'''

'''
        Goal is to eventually return the list to another function
        The getUppercase and getLowercase have to be called
        first for some of the other functions to work properly
        because they fill up the letters needed
'''
def restart():
        global multiplier 
        global messageLength

        for x in range(len(Uppercase)):
                Upper_Letters[Uppercase[x]] = 0

        for x in range(len(Lowercase)):
                Lower_Letters[Lowercase[x]] = 0

        for x in range(len(Specials)):
                Special_Chars[Specials[x]] = 0

        for x in range(len(Punctuations)):
                Punctuations_Chars[Punctuations[x]] = 0

        for x in range(len(Digits)):
                Numbers[Digits[x]] = 0

        for x in range(len(HexLetter)):
                Hex_Letters[HexLetter[x]] = 0

        multiplier = 0
        messageLength = 0

def makeHash(message):
        print("\nGenerating Hash...", message)
        prehash = ""
        length = Total_Length(message)
        multiplier = get_Multiplier()
        coder = isEncoder(message)
        master = masterString(message)
        if multiplier % 2 == 0:
                multiplier += 1

        # print(multiplier)
        #print(length)
        '''
                Need to figure out how to add individual numbers to prehash string
        '''
        
        letters = getLowercase(message)
        lowers = letters
        letters = int(ASCIIConverter(letters))

        temp = getUppercase(message)
        uppers = temp
        temp = int(ASCIIConverter(temp))

        b1 = letters | temp
        lethash = str(b1)

        numbers = getNumbers(message)
        numbers = int(ASCIIConverter(numbers))

        b1 = b1 | numbers
        lethash += str(b1)

        symbols = getSpecialChars(message)
        symbols = int(ASCIIConverter(symbols))
        
        temp = getPunctuations(message)
        temp = int(ASCIIConverter(temp))

        b2 = symbols | temp
        b1 = b1 | b2
        lethash += str(b1)
        '''
                Call Converter
                Save results in symbols
        '''

        temp = getDigraphs(message)*getTrigraphs(message)     
        temp = int(ASCIIConverter(str(temp)))

        lethash += str(temp)
        

        prehash += str(num_of_Letters())
        prehash += str(num_of_UpperCase())
        prehash += str(num_of_LowerCase())
        prehash += str(num_of_Vowels(message))
        prehash += str(num_of_Consonants(message))
        prehash += str(num_of_Articles(message))
        prehash += str(num_of_Non_Letters(message))
        prehash += str(num_of_Numbers())
        prehash += str(num_of_Spaces(message))
        prehash += str(num_of_Newlines(message))
        prehash += str(num_of_Sentences(message))
        
        letters = uppers + lowers
        letters = ASCIIConverter(letters)
        coder = str(int(coder)* int(letters))

        # print("Letters: ", letters)
        # print("Coder: ", coder)
        
        prehash = str(int(prehash)*maxHexMultiplier(hex(int(master))))
        
        # print(lethash)
        # print(prehash)

        HASH =  lethash + coder + prehash
        HASH = int(HASH)
        multiplier *= length
        HASH *= multiplier

        HASH = hex(HASH)
        length = len(HASH)
        HASH = HASH[2:length]
        print("Pre 128: ", HASH, "\tLenth: ", len(HASH))
        
        HASH = shuffle(make_128(HASH))

        print("The hash is " + HASH + " Which is ", len(HASH), " in length.")
        restart()
        
        return HASH

def ASCIIConverter(string):
        if string == "":
               return 0
        newString = ""
        for x in string:
                newString += str(ord(x))
        return newString

def isEncoder(message):
        string = ""
        seen = ""

        for x in message:
                seen += x        
                if x.isalnum():
                                string +="1"
                                if x.isalpha(): 
                                        string += "2"
                                        if x.isupper(): string += "4"
                                        elif x.islower(): string += "5"
                                elif x.isdigit(): string += "3"
                elif x.isspace(): string += "0"
        
        # print("Coder: ", string)
        return string

def Total_Length(message):
    global messageLength
    messageLength = len(message)
    return messageLength

def masterString(message):
        Master = Uppercase + Lowercase + Digits +  " "
        string = ""
        for x in message:
                if x.isspace(): string += " "
                elif x in Master and x not in string:
                        string += x
        return ASCIIConverter(string)

def get_Multiplier():
        global multiplier
        global messageLength
        multiplier = messageLength % 128
        return multiplier
    
def getPunctuations(message):
        string = ""
        for x in message:
                if x in Punctuations_Chars:
                        Punctuations_Chars[x] += 1
        for x in Punctuations_Chars:
                if Punctuations_Chars[x] > 0:
                        string += x
     
        return string

def getSpecialChars(message):
        string = ""
        for x in message:
                if x in Special_Chars:
                        Special_Chars[x] += 1
        for x in Special_Chars:
                if Special_Chars[x] > 0:
                        string += x

        return string

def getNumbers(message):
        string = ""
        for x in message:
                if x in Numbers:
                        Numbers[x] += 1
        for x in Numbers:
                if Numbers[x] > 0:
                        string += x
     
        return string

def getUppercase(message):
        string = ""
        for x in message:
                if x in Uppercase and x not in string:
                        string += x
        
        for x in message:
                if x in Upper_Letters:
                        Upper_Letters[x] += 1
        for x in Upper_Letters:
                if Upper_Letters[x] > 0:
                        string += x
        return string
        
def getLowercase(message):
        string = ""
        for x in message:
                if x in Lowercase and x not in string:
                        string += x

        for x in message:
                if x in Lower_Letters:
                        Lower_Letters[x] += 1

        for x in Lower_Letters:
                if Lower_Letters[x] > 0:
                        string += x
        return string

def getDigraphs(message):
        total = 0
        message = message.lower()
        for x in digraphs:
                total += message.count(x)

        return total

def getTrigraphs(message):
        total = 0
        message = message.lower()
        for x in trigrahs:
                total += message.count(x)

        return total

def num_of_UpperCase():
        total = 0
        for x in Upper_Letters:
                total += Upper_Letters[x]
        return total

def num_of_LowerCase():
        total = 0
        for x in Lower_Letters:
                total += Lower_Letters[x]
        return total

def num_of_Letters():
    total = 0
    for x in Upper_Letters:
        total += Upper_Letters[x]
    for x in Lower_Letters:
        total += Lower_Letters[x]
    return total

def num_of_Numbers():
        total = 0
        for x in Numbers:
                total += Numbers[x]
        return total

def num_of_Sentences(message):
        total = 0
        total += Punctuations_Chars["."]
        total += Punctuations_Chars["?"]
        total += Punctuations_Chars["!"]

        if total == 0:
                return 1
        else:
                return total

def num_of_Non_Letters(message):
    total = Total_Length(message) - num_of_Letters()
    if total < 0:
        total *= -1
    return total

def num_of_Consonants(message):
        consts = 0
        for x in message:
                if x in Consonants:        
                        consts += 1
        return consts

def num_of_Vowels(message):
        vowel = 0
        for x in message:
                if x in Vowels:
                        vowel += 1
        return vowel

def num_of_Newlines(message):
        newLine = 0
        for x in message:
                if x == "\n":
                        newLine += 1
        return newLine 
  
def num_of_Spaces(message):
        spaces = 0
        for x in message:
                if x == " ":
                        spaces += 1
        return spaces

def num_of_Articles(message):
    total = 0

    total += message.count(" A ")
    total += message.count(" a ")
    total += message.count(" An ")
    total += message.count(" an ")
    total += message.count(" The ")
    total += message.count(" the ")

    return total

def hexcount(message):
        count = 0
        for x in message:
                if x in HexLetter:
                        Hex_Letters[x] += 1
                        
        for x in Hex_Letters:
                count += Hex_Letters[x]

        # print(Hex_Letters, count)

def maxHexMultiplier(message):  
        maxLet = ""
        maxNum = 0
        
        hexcount(message)

        for x, y in Hex_Letters.items():
                if y >= maxNum:
                        maxNum = y
                        maxLet = x
        if ord(maxLet) >= 97: maxLet = ord(maxLet)-87
        
        for x in Hex_Letters:
                Hex_Letters[x] = 0
        # print("MaxLet: ", maxLet, " MaxNum: ", maxNum)
        return int(maxLet)*maxNum

def maxHexes(message):
        maxNum = 0
        maxLet = ""

        hexcount(message)

        for x, y in Hex_Letters.items():
                if y > maxNum:
                        maxNum = y
                        maxLet = x

        for x in Hex_Letters:
                Hex_Letters[x] = 0
        
        a = [maxLet, maxNum]

        return a

# This shuffle method moves things from front to back
def shuffleReverse(hlist):
        length = len(hlist) - 1

        for x in range(int((length + 1)/2)): 
                temp = hlist[x]
                hlist[x] = hlist[length - x]
                hlist[length - x] = temp
        
        return hlist

#This shuffle method moves the even numbers around from front to back
def shuffleEvens(hlist):
        length = len(hlist) - 1
        y = 0

        for x in range(int((length + 1)/2)):
                if x%2 == 1: continue
                temp = hlist[x]
                hlist[x] = hlist[length - x]
                hlist[length - x] = temp
        
        return hlist

#This shuffle method moves the odd numbers around from front to back
def shuffleOdds(hlist):
        length = len(hlist) - 1
        y = 0

        for x in range(int((length + 1)/2)):
                if x%2 == 0: continue
                temp = hlist[x]
                hlist[x] = hlist[length - x]
                hlist[length - x] = temp
        
        return hlist

#This concatenation will join the first and last items and work inwards pairing them
# I.E.: 1n, 2n-1, ... n+1/2 n-1/2
def concatFB(hlist):
        length = len(hlist) - 1
        y = 0

        for x in range(int((length + 1)/2)):
                hlist[x] = hlist[y] + hlist[length - y]
                y+= 1

        length += 1

        length = int(length / 2)
        
        
        hlist = hlist[0:length]
        
        return hlist

#This method joins pairs each pair of items moving forward in the list
# I.E.: 12, 34, 56,..., n-1n
def concatNF(hlist):
        length = len(hlist) - 1
        y = 0

        for x in range(int((length + 1)/2)):
                hlist[x] = hlist[y] + hlist[y+1]
                y+= 2

        length += 1

        length = int(length / 2)
        
        hlist = hlist[0:length]
        
        return hlist

# This method joins the items with its forward neighbor then itself
# I.E.: 21, 43, 65, ... n n-1
def concatNS(hlist):
        length = len(hlist) - 1
        y = 0

        for x in range(int((length + 1)/2)):
                hlist[x] = hlist[y+1] + hlist[y]
                y+= 2

        length += 1

        length = int(length / 2)
        
        hlist = hlist[0:length]

        return hlist

def shuffle(message):
        hlist = list(message)
        # print(hlist, len(hlist))

        while len(hlist) != 4:
                hlist = concatFB(shuffleReverse(hlist))
                # print(hlist, len(hlist))
                if len(hlist) == 4: break
                hlist = concatNF(shuffleOdds(hlist))
                # print(hlist, len(hlist))
                if len(hlist) == 4: break
                hlist = concatNS(shuffleEvens(hlist))
                # print(hlist, len(hlist))
       

        return FOIL(hlist)

def FOIL(hlist):
        first = hlist[0]
        middle = hlist[2] + hlist[1]
        last = hlist[3]

        final = last + middle[::-1]+ first
        
        return final



def make_128(message):
        # print(message)
        hlength = len(message)
        sublen = 0
        # print(hlength)

        if hlength > 128:
                sublen = hlength % 128
                temp = message[hlength - sublen:hlength]
                temp2 = message[sublen:sublen+sublen]
                # print(len(temp), len(temp2), sep="\n")
                
                rtemp = temp[::-1]
                rtemp2 = temp2[::-1]

                temp = int(temp, 16)
                temp2 = int(temp2, 16)        
                b1 = int(temp | temp2)
                b2 = int(temp & temp2)
                temp = int(b1 ^ b2)
                # temp = temp[2:len(temp)]
                # print(temp, "\n", len(temp))

                rtemp = int(rtemp, 16)
                rtemp2 = int(rtemp2, 16)        
                b1 = int(rtemp | rtemp2)
                b2 = int(rtemp & rtemp2)
                rtemp = int(b1 ^ b2)
                # rtemp = rtemp[2:len(rtemp)]
                # print(rtemp, "\n", len(rtemp))

                a = maxHexMultiplier(hex(temp & rtemp))
                b = maxHexMultiplier(hex(temp | rtemp))
                c = maxHexMultiplier(hex(temp ^ rtemp))

                if len(hex(temp & rtemp)) < sublen:
                        a = 0 
                if len(hex(temp | rtemp)) < sublen: 
                        b = 0
                if len(hex(temp & rtemp)) < sublen:
                        c = 0
                #AND
                if a < b and a > c: temp = hex(temp & rtemp); #choice = "AND"
                #OR
                elif b > a and b > c: temp = hex(temp | rtemp); #choice = "OR"
                #XOR
                elif c > b and c > b: temp = hex(temp ^ rtemp); #choice = "XOR"

                # print(choice)
                
                temp = temp[2:len(temp)]
                temp2 = message[0:128-sublen]
                message = temp+temp2
                
        elif hlength < 128:
                temp = ""
                rep = 0
                for x in message:
                        if x not in temp:
                                temp += x
                        else:
                                rep += 1

                coder = isEncoder(temp)
                sum = 0
                for x in range(len(coder)):
                        sum += int(coder[x])

                multiplier = maxHexMultiplier(temp)
                temp = int(temp, 16)
                temp2 = temp * multiplier
                temp *= sum

                if len(str(temp)) > len(str(temp2)):
                        temp = makeEqual(str(temp), str(temp2))
                elif len(str(temp)) < len(str(temp2)):
                        temp2 = makeEqual(str(temp2), str(temp))
                        
                # print("TRUE") if len(str(temp)) == len(str(temp2)) else print("FALSE")

                # print(temp, temp2)
                # print("Temp: ", len(str(temp)))
                # print("Temp2: ", len(str(temp2)))

                a = int(message, 16) & temp
                b = int(message, 16) | temp2
                c = a | b
                # print(a, len(str(a)), hex(a), len(hex(a)))
                # print(b, len(str(b)), hex(b), len(hex(b)))
                # print(c, len(str(c)), hex(c), len(hex(c)))
                # print()
                # print()
                temp = hex(c)
                message += temp[2:len(str(temp))]

        if len(message) != 128: message = make_128(message)
        
        return message  
def makeEqual(num1, num2):
       return int(num1[0:len(num2)])

                
