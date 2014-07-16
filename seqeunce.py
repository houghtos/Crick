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

    def decapitated (self, s = None):
        if s == None:
            s=self.seq
        return s[0:len(s) - (len(s)%3)]

    def converter (self, s = None):
        if s == None:
            s = self.decapitated(self.seq) #These two lines set s = seq input from set() function

        import numpy

        table_protein = [
            ["ttt","Phe"],
            ["ttc","Phe"],
            ["tta","Leu"],
            ["ttg","Leu"],
            ["ctt","Leu"],
            ["ctc","Leu"],
            ["cta","Leu"],
            ["ctg","Leu"],
            ["att","Ile"],
            ["atc","Ile"],
            ["ata","Ile"],
            ["atg","Met"],
            ["gtt","Val"],
            ["gtc","Val"],
            ["gta","Val"],
            ["gtg","Val"],
            ["tct","Ser"],
            ["tcc","Ser"],
            ["tca","Ser"],
            ["tcg","Ser"],
            ["cct","Pro"],
            ["ccc","Pro"],
            ["cca","Pro"],
            ["ccg","Pro"],
            ["act","Thr"],
            ["acc","Thr"],
            ["aca","Thr"],
            ["acg","Thr"],
            ["gct","Ala"],
            ["gcc","Ala"],
            ["gca","Ala"],
            ["gcg","Ala"],
            ["tat","Tyr"],
            ["tac","Tyr"],
            ["taa","STOP"],
            ["tag","STOP"],
            ["cat","His"],
            ["cac","His"],
            ["caa","Gln"],
            ["cag","Gln"],
            ["aat","Asn"],
            ["aac","Asn"],
            ["aaa","Lys"],
            ["aag","Lys"],
            ["gat","Asp"],
            ["gac","Asp"],
            ["gaa","Glu"],
            ["gag","Glu"],
            ["tgt","Cys"],
            ["tgc","Cys"],
            ["tga","STOP"],
            ["tgg","Trp"],
            ["cgt","Arg"],
            ["cgc","Arg"],
            ["cga","Arg"],
            ["cgg","Arg"],
            ["agt","Ser"],
            ["agc","Ser"],
            ["aga","Arg"],
            ["agg","Arg"],
            ["ggt","Gly"],
            ["ggc","Gly"],
            ["gga","Gly"],
            ["ggg","Gly"]
        ]

        for i in range (0, len(s), 3):
            triplet = s[i:i+3]


            for i in range (0, len(table_protein)):
                if table_protein[i][0] == triplet:
                    print (table_protein[i][0], " ", table_protein[i][1])

    def rnaconverter (self, s = None):
        if s == None:
            s=self.seq
        j = ""

        for i in range (0, len(s)):
            if s[i] == "t":
                j = j + "u"
            else:
                j = j + s[i]
        return j


#--------------------------
def main():
    pass


if __name__ == '__main__':
    main()
#---------------------------


dna = sequence()
dna.set(input("Please enter a string "))
print (dna.rnaconverter())

#print ("Sequence: ", dna.seq)
#print ("Decapitated: ", dna.decapitated())
#print ("Checked out? ", dna.check_seq())

#dna.converter()



