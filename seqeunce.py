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


class sequence:
    seq= ""


    def set( self, s ):

        self.seq = s.lower()
        return

    #def codonset (self, s = None):
        if s == None:
            s = self.check_seq

        print (s)
        return

    def check_seq ( self, s = None):
        if s == None:
            s=self.seq
        matches = 0
        nucleotides = "atcg"
        for i in range(0, len(s)):
            for j in range (0, len(nucleotides)):
                if s[i] == nucleotides[j]:
                    matches=matches+1

        if matches == len(s)and len(s) > 0:
            isOkay=1

        else:
            isOkay=0

        return isOkay



    def converter (self, s = None):
        if s == None:
            s  = self.seq #These two lines set s = seq input from set() function


            m = 0
            q = 3
            j = 0



        for i in range (0, len(s), 3):
            print (s[m:q])
            m = m + 3
            q = q + 3
            j = j + 1








#--------------------------
def main():
    pass


if __name__ == '__main__':
    main()
#---------------------------


dna = sequence()
dna.set("ATCACGTC")
dna.check_seq()
#dna.codonset()
dna.converter()


