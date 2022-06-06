# import library
import math, random
 
# function to generate OTP
def generateOTP() :
    ##FOR DIGITS
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
    length = len(digits) 
    # length of password can be changed
    # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * length)]

    # ##FOR STRINGS
    # # Declare a string variable 
    # # which stores all string
    # string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # OTP = ""
    # length = len(string)
    # for i in range(6) :
    #     OTP += string[math.floor(random.random() * length)]    
 
    return OTP

    