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
