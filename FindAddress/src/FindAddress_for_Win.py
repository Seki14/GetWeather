#!/usr/bin/env python

# Tool name   :FindAddress for Windows
# Module name :FindAddress_for_Win.py
# Detail      :This tool is to get address or postal code.
# Implementer :R.Ishikawa
# Version     :1.0
# Last update :2019/11/16

# Version History
# 1. Create New                    R.I Ver.1.0  2019/11/16

import sys

# Set Path including "KEN_ALL.CSV" for Windows
csv_path = "C:\"

def GetAddress():
    postal_code = input("Type target postal code:")
    fp = open(csv_path, "r", encoding="shift_jis")
    for line in fp:
        line = line.replace(' ', '') # cut space
        line = line.replace('"', '') # cut double quatation
        cells = line.split(",")      # split by comma
        code = cells[2]  # Postal code
        pref = cells[6]  # Prefucture
        city = cells[7]  # City name
        ad = cells[8]    # Address name
        title = pref + city + ad
        if code.find(postal_code) != -1:
            print(title)
    fp.close()

def GetPostalCode():
    addr = input("Type target address:")
    fp = open(csv_path, "r", encoding="shift_jis")
    for line in fp:
        line = line.replace(' ', '') # cut space
        line = line.replace('"', '') # cut double quatation
        cells = line.split(",")      # split by comma
        code = cells[2]  # Postal Code
        pref = cells[6]  # Prefucture
        city = cells[7]  # City name
        ad = cells[8]    # Address name
        title = pref + city + ad
        if title.find(addr) != -1:
            print(code + ":" + title)
    fp.close()


def main():
    print("\n")
    print("####################################################")
    print("################### FINDADDRESS ####################")
    print("####################################################")
    print("\n")
    print("[DISCRIPTION]")
    print(" This tool is to get address or postal code.")
    print(" If you type '1', you can get unknown address by typing postal code.")
    print(" If you type '2', you can get unknown postal code by typing KEYWORD about address name.")
    print("\n")

    while True:
        print("[OPERATION]")
        print("input the following number which you want to get.")
        number = input("[1:Address  2:PostalCode  99 or SPACE):Close]:")
        if number.isdigit() != 1: # Filter non-integer value
            sys.exit()
        int_number = int(number)  # Convert String to Integer
        if int_number == 1:       # The case that user types "1"
            GetAddress()
            print("\n")
        elif int_number == 2:     # The case that user types "2"
            GetPostalCode()
            print("\n")
        elif int_number == 99:    # The case that user types "99"
            sys.exit()
        else:                     # Exception handling
            print("Invalid Number. Type again.")
            print("\n")

if __name__ == "__main__":
    main()

