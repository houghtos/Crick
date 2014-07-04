#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sean
#
# Created:     03/07/2014
# Copyright:   (c) Sean 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def check_sequence( sequence ):
    isOkay = 0
    matches = 0
    nucleotides = "atcg"


    for i in range(0, len(sequence)):
        for j in range (0, len(nucleotides)):
            if sequence[i] == nucleotides[j]:
                matches=matches+1

    if matches == len(sequence):
        isOkay=1
    return isOkay



def main():
    pass


if __name__ == '__main__':
    main()

sequence = input('Please enter a ten digit nucleotide sequence ')
print (check_sequence(sequence))

