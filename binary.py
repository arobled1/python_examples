#===============================================================================
# Description:
# By user request, this converts base-2 binary to a decimal integer or a
# decimal integer to base-2 binary.
# If "b2d" is entered, the binary is split into a list with each 1 or 0 being
# considered an element of the list.
# Since 'raw_input' reads input as a string, each element is converted from a
# string to an integer.
# Then each element from right to left is multiplied by its binary value
# and each product is summed until the result is the value of the entire
# binary in decimal form.
# If "d2b" is entered, the 'raw_input' is converted from a string to an integer.
# For any integer a, a mod 2 will always result in a 1 or a 0.
# Therefore, the code iteratively computes floor divisions of the decimal by
# 2**j mod 2 and appends the resulting 0 or 1 to a list.
# In order to avoid trailing zeros in our list, a 'sum' variable is used to keep
# track of when our list has reached the last 1 necessary to complete the
# binary form.
#===============================================================================
# Author: Alan Robledo
#===============================================================================
# Output:
#   'b2d'       Binary    ------>       Decimal
#                 0                        0
#                 1                        1
#                 1010                     9
#                 1100                     12
#   'd2b'       Binary    <------       Decimal
#                 1100                     12
#                 10111                    23
#                 1100100                  100
#===============================================================================
# Notes:
# 'b2d' will crash if the user inputs letters as Python will not want to convert
# them into integers, which it shouldn't!
#===============================================================================
def binary_to_decimal():
    usr_bin = raw_input("Type your binary: ")
    bin_list = list(usr_bin)
    bin_list = [ int(x) for x in bin_list ]
    decimal = 0
    i = 0
    j = len(bin_list) - 1
    k = 0
    while i == 0:
        decimal = decimal + bin_list[j]*2**k
        j = j - 1
        k = k + 1
        if j < 0:
            i = 1
    return decimal

def decimal_to_binary():
    usr_dec = raw_input("Type your decimal: ")
    dec = int(usr_dec)
    binary = []
    i = 0
    j = 0
    sum = 0
    while i == 0:
        binary.append((dec/(2**j) % 2))
        if (dec/(2**j) % 2) == 1:
            sum = sum + 2**j
        j = j + 1
        if sum == dec:
            i = 1
    binary.reverse()
    binary = [str(x) for x in binary]
    print_bin = ''.join(binary)
    return print_bin

print """Do you want to convert binary to decimal (enter 'b2d')?
or
Do you want to convert decimal to binary (enter 'd2b')?"""
choice = raw_input()
if choice == "b2d":
    decimal = binary_to_decimal()
    print "Decimal is: %d" % decimal
elif choice == "d2b":
    print_bin = decimal_to_binary()
    print "Binary is: %s" % print_bin
