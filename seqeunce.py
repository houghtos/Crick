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
'''
def insertion (list):
    for index in range (1,len(list)):
        value = list[index]
        i = index - 1
        while i>=0:
            if value < list[i]:
                list[i+1] = list[i] #shift number in slot i right to slot i + 1
                list[i] = value #shift value left into slot i
                i = i - 1
            else:
                break
'''
class HMM:
    toy_states = {}
    toy_observations = {}
    toy_start_probability = {}
    toy_transition_probaility = {}
    toy_emission_probability = {}

    def dataset (self,):

        states = ('Intron', 'Exon', "5' Splice")

        observations = ('A', 'T', 'C', 'G')

        start_probability = {'Proceed': 1, 'No': 0.0}

        transition_probability = {
       'Exon' : {'Proceed': 0.1, 'Residue': 0.9},
       "5' Splice" : {'Proceed': 1, 'Residue': 0.0},
       'Intron': {'Proceed': 0.1, 'Residue': 0.9}

        }

        emission_probability = {
       'Exon' : {'A': 0.25, 'T': 0.25, 'C': 0.25, 'G' : 0.25},
       "5' Splice" : {'A': 0.05, 'T': 0.0, 'C': 0.0, 'G' : 0.95},
       'Intron': {'A': 0.4, 'T': 0.4, 'C': 0.1, 'G' : 0.1}
        }

        states = self.toy_states
        observations =  self.toy_observations
        start_probabdility = self.toy_start_probability
        transition_probability = self.toy_transition_probaility
        emission_probability = self.toy_emission_probability

        return


    def viterbi(self, obs = None, states = None, start_p = None, trans_p = None, emit_p = None):
        V = [{}]
        path = {}

        if obs == None:
            obs = self.toy_observations
        if states == None:
            states = self.toy_states
        if start_p == None:
            start_p = self.toy_start_probability
        if trans_p == None:
            trans_p = self.toy_transition_probaility
        if emit_p == None:
            emit_p = self.toy_emission_probability

        # Initialize base cases (t == 0)
        for y in states:
            V[0][y] = start_p[y] * emit_p[y][obs[0]]
            path[y] = [y]

        # Run Viterbi for t > 0
        for t in range(1, len(obs)):
            V.append({})
            newpath = {}

            for y in states:
                (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
                V[t][y] = prob
                newpath[y] = path[state] + [y]

            # Don't need to remember the old paths
            path = newpath
        n = 0           # if only one element is observed max is sought in the initialization values
        if len(obs)!=1:
            n = t
        print_dptable(V)
        (prob, state) = max((V[n][y], y) for y in states)
        return (prob, path[state])

    # Don't study this, it just prints a table of the steps.
    def print_dptable(V):
        s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
        for y in V[0]:
            s += "%.5s: " % y
            s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
            s += "\n"
        print(s)
    '''
    def example():

        return viterbi(observations,
                       states,
                       start_probability,
                       transition_probability,
                       emission_probability)
    print(example())
    '''


#Functions dnaconverter and rnaconverter of this class should not be called at the same time
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

    def dnaconverter (self, s = None):
        if s == None:
            s=self.seq
        j = ""

        for i in range (0, len(s)):
            if s[i] == "u":
                j = j + "t"
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

'''
dna.set(input("Please enter a string "))
print (dna.seq)
print (dna.dnaconverter())

print ("Sequence: ", dna.seq)
print ("Decapitated: ", dna.decapitated())
print ("Checked out? ", dna.check_seq())
'''

test = HMM()
test.dataset()
test.viterbi()






