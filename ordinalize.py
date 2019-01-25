""" 
This program takes an integer input from the user and converts it into an ordinal number.
For example, if 1256 is input, the program outputs 'one thousand two hundred fifty-sixth'.
It will take numbers up to 999,999,999,999,999,999,999,999
Next steps will be making it theoretically count up to infinity, tightening it up, getting 
rid of any unnecessary lines and making it object-oriented.

"""




nums1to19 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', \
        'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

numsTens = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

placevalues = ['', 'thousand', 'million', 'billion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', \
               'octillion', 'nonillion', 'decillion']

def makeOrdinal(numstr):
    if numstr[-3:] == 'one':
        numstr = numstr[:-3] + 'first'
    elif numstr[-3:] == 'two':
        numstr = numstr[:-3] + 'second'
    elif numstr[-5:] == 'three':
        numstr = numstr[:-5] + 'third'
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
            num = nums1to19[threedignum // 100] + ' hundred ' + get2DigNum(threedignum % 100)
    return num


def getordnum(number):
    placevalposition = 0
    finalnumber = ""
    while (number):
        number = str(number)
        threeDigNumber = int(number[-3:])
        threeDigNumber = get3DigNum(threeDigNumber)
        if ( placevalposition > 0 ) and ( threeDigNumber == 'zero' ):
            threezeros = True
        elif ( placevalposition > 0 ):

            finalnumber = threeDigNumber + " " + placevalues[placevalposition] + ' ' + finalnumber
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


numb0r = input("Enter a number to ordinalize: ")

ordnum = getordnum(numb0r)

print("\n" + numb0r, ":", ordnum)

 
       




