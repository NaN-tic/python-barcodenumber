#This file is part of barcodenumber. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
Check the barcodes
'''
import math

__version__ = '1.0'

def barcodes():
    '''
    Return the list of country's codes that have check function
    '''
    res = [x.replace('check_code_', '').upper() for x in globals()
            if x.startswith('check_code_')]
    res.sort()
    return res

def is_pair(x):
    return not x%2

def check_code_ean13(number):
    '''
    Check ean13 code.
    '''
    if not number:
        return True
    if len(number) <> 13:
        return False
    try:
        int(number)
    except:
        return False
    oddsum = 0
    evensum = 0
    total = 0
    eanvalue = number
    reversevalue = eanvalue[::-1]
    finalean = reversevalue[1:]

    for i in range(len(finalean)):
        if is_pair(i):
            oddsum += int(finalean[i])
        else:
            evensum += int(finalean[i])
    total=(oddsum * 3) + evensum

    check = int(10 - math.ceil(total % 10.0)) %10

    if check != int(number[-1]):
        return False
    return True

def check_code(code, number):
    '''
    Check barcode
    '''
    try:
        checker = globals()['check_code_%s' % code.lower()]
    except KeyError:
        return False
    return checker(number)
