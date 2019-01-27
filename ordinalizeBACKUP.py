""" 
Update: Program takes numbers up to at least 10 ^ 600 (ish?). The web site I was using 
to test the output against using requests stopped allowing me to enter numbers that large
as a  preventative measure against buffer overflow attacks. Next step today is find 
another website that allows bigger numbers to be input or another way to check the output, 
which at this point is too big to painstakingly go through and check every word. I'm going 
to find a way to take this thing to infinity though. No question.

This program takes an integer input from the user and converts it into an ordinal number.
For example, if 1256 is input, the program outputs 'one thousand two hundred fifty-sixth'.
It will take numbers up to......
Next steps will be making it theoretically count up to infinity, tightening it up, getting 
rid of any unnecessary lines and making it object-oriented.

"""


global MilliasNumber
MilliasNumber = 0


nums1to19 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', \
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', \
        'sixteen', 'seventeen', 'eighteen', 'nineteen']

numsTens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', \
        'eighty', 'ninety']

placevalues1 = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', \
        'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']

placevalues2 = ['', 'un', 'duo', 'tre', 'quattuor', 'quin', 'sex', 'septen', 'octo', \
        'novem']

placevalues3 = ['', 'decillion', 'vigintillion', 'trigintillion', 'quadragintillion', \
        'quinquagintillion', 'sexagintillion', 'septuagintillion', 'octogintillion', \
        'nonagintillion']

placevalues4 = ['', 'cen', 'duocen', 'trecen', 'quadringen', 'quingen', 'sescen', \
        'septingen', 'octingen', 'nongen']

placevalues5 = ['', 'dec', 'vigin', 'trigin', 'quadragin', 'quinquagin', 'sexagin', \
        'septuagin', 'octogin', 'nonagin']

def getPostMilliaString(placevalue):
    milliasNumberLocal = 0

    while placevalue:
        relevantPlaceValue = placevalue % 1000
        if ( milliasNumberLocal == 0 ):
            string = get0to1000powerstring(relevantPlaceValue)
            placevalue = int(str(placevalue)[:-3])
            milliasNumberLocal += 1            
        else:
            string = placevalues4[relevantPlaceValue // 100] + \
                    placevalues2[relevantPlaceValue % 10] + \
                    placevalues5[(relevantPlaceValue % 100) // 10] + \
                    ("millia" * milliasNumberLocal) + string
            placevalue = int(str(placevalue[:-3]))
            milliasNumberLocal += 1
    return string


def makeOrdinal(numstr):
    if numstr[-3:] == 'one':
        numstr = numstr[:-3] + 'first'
    elif numstr[-3:] == 'two':
        numstr = numstr[:-3] + 'second'
    elif numstr[-5:] == 'three':
        numstr = numstr[:-5] + 'third'
    elif numstr[-4:] == 'four':
        numstr = numstr[:-4] + 'forth'
    elif numstr[-4:] == 'five':
        numstr = numstr[:-4] + 'fifth'
    elif numstr[-5:] == 'eight':
        numstr += 'h'
    elif numstr[-7:] == 'twelve':
        numstr = numstr[:-7] + 'twelfth'
    elif numstr[-2:] == 'ty':
        numstr = numstr[:-2] + 'tieth'
    else:
        numstr = numstr + 'th'
    return numstr

def get2DigNum (twodignum):
    if twodignum < 20:
        num = nums1to19[twodignum]
    else:
        num = numsTens[twodignum // 10]
        if (twodignum % 10 == 0):
            return num
        else:
            num += '-' + nums1to19[twodignum % 10]
    return num

def get3DigNum (threedignum):
    if threedignum < 100:
        num = get2DigNum(threedignum)
    else:
        if ( threedignum % 100 == 0 ):
            num = nums1to19[threedignum // 100] + ' hundred'
        else:
            num = nums1to19[threedignum // 100] + ' hundred ' + \
                    get2DigNum(threedignum % 100)
    return num

def get100to1000powerstr(placevalue):
    if (placevalue % 100 > 0) and (placevalue % 100 <= 10):
        string = placevalues4[(placevalue - 1) // 100] + \
                placevalues2[(placevalue - 1) % 10] + 'tillion'
    else:
        string = placevalues4[(placevalue - 1) // 100] + \
                placevalues2[(placevalue - 1) % 10] + \
                placevalues3[((placevalue - 1) % 100) // 10]
    return string

def get0to1000powerstr(placevalue):
    threeDigNumber = int(number[-3:])
        threeDigNumber = get3DigNum(threeDigNumber)
        if ( placevalposition > 0 ) and ( threeDigNumber == 'zero' ):
            threezeros = True
        elif ( placevalposition > 0 ) and ( placevalposition < 12 ):
            finalnumber = threeDigNumber + " " + placevalues1[placevalposition] + ' ' + \
                    finalnumber
        elif ( placevalposition > 0 ) and ( placevalposition < 101 ):
            finalnumber = threeDigNumber + " " + placevalues2[placevalposition % 10 - 1] + \
                    placevalues3[(placevalposition - 1 ) // 10] + ' ' + finalnumber
            print ("placevalposition: " + str(placevalposition) + ' -- ' + \
                    placevalues2[placevalposition % 10 - 1] + \
                    placevalues3[(placevalposition - 1) // 10])
        elif ( placevalposition > 0 ) and ( placevalposition < 1000 ):
            finalnumber = threeDigNumber + " " + get100to1000powerstr(placevalposition) + \
                    ' ' + finalnumber
            print("placevalposition: " + str(placevalposition) + ' -- ' + \
                    get100to1000powerstr(placevalposition))




def getordnum(number):
    placevalposition = 0
    finalnumber = ""
    while (number):
        #if placevalposition > 100:
         #   print("\nplacevalposition: " + str(placevalposition) + '\n')
        number = str(number)
        threeDigNumber = int(number[-3:])
        threeDigNumber = get3DigNum(threeDigNumber)
        if ( placevalposition > 0 ) and ( threeDigNumber == 'zero' ):
            threezeros = True
        elif ( placevalposition > 0 ) and ( placevalposition < 12 ):
            finalnumber = threeDigNumber + " " + placevalues1[placevalposition] + ' ' + \
                    finalnumber
        elif ( placevalposition > 0 ) and ( placevalposition < 101 ):
            finalnumber = threeDigNumber + " " + placevalues2[placevalposition % 10 - 1] + \
                    placevalues3[(placevalposition - 1 ) // 10] + ' ' + finalnumber
            print ("placevalposition: " + str(placevalposition) + ' -- ' + \
                    placevalues2[placevalposition % 10 - 1] + \
                    placevalues3[(placevalposition - 1) // 10])
        elif ( placevalposition > 0 ) and ( placevalposition < 1000 ):
            finalnumber = threeDigNumber + " " + get100to1000powerstr(placevalposition) + \
                    ' ' + finalnumber
            print("placevalposition: " + str(placevalposition) + ' -- ' + \
                    get100to1000powerstr(placevalposition))
        elif (placevalposition > 1000):
            finalnumber = threeDigNumber + " " + getPostMilliaString(placevalposition) + \
                    ' ' + finalnumber
        else:
            finalnumber = threeDigNumber
        placevalposition += 1
        if finalnumber[-4:] == 'zero':
            finalnumber = finalnumber[:-4]
        if finalnumber[-1:] == ' ':
            finalnumber = finalnumber[:-1]
        number = number[:-3]
        if number != '':
            number = int(number)
        else:
            num = 0

    finalnumber = makeOrdinal(finalnumber)
    return finalnumber

if __name__ == "__main__":

    numb0r = input("Enter a number to ordinalize: ").replace(" ", "").replace("<br>", "")
    ordnum = getordnum(numb0r)


    print("\n" + numb0r, ":", ordnum)

 
       




