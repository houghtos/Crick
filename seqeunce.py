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

def main():
    pass

if __name__ == '__main__':
    main()

sequence = input ("Please enter a ten digit nucleotide sequence ")
print (sequence)


#If then statement to enforce the sequence divided as an array maximum 10 characters
if sequence == sequence[10]:
print ("You have entered more than 10 nucleotides please try again")
sequence = input ("Please enter a ten digit nucleotide sequence ")