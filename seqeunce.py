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


class sequence:    #Created a 'class' named sequence
    seq= ""        #Create a variable for the class "sequence" class which is equal to an empty string (Character array with no characters, size zero)



#Why do I need to make the variable of the class "self.seq = s" in a function we named here "set"  --?
#Overloard function.  This function will run default if no value is given to s
#Function: Sets seq variable equal to s

    def set( self, s ): #"def" declares a function.  The name  of the function is "set". All functions in a class must contain ( self
        self.seq = s #This sets the class variable seq equal to the variable s ??????????
        return #ends the function set



#This will run if value is given
    def check_seq ( self, s = None ):
        if s == None:
            s = self.seq

        isOkay = 0 # Set default 0 to return FALSE.  Must satisfy if matches ==len(s)
        matches = 0 #Has a value of +1 added
        nucleotides = "atcg"


        for i in range(0, len(s)): #For loop run as much times as the length of the string, "i" is introduced as a loop variable equal to 0 running to length of "s" which is equal to "seq" class variable from running dna.set()
            for j in range (0, len(nucleotides)): #For loop runs
                if s[i] == nucleotides[j]: #If list (array) of variable s[i which is defined as 0 --- THIS IS THE LINE I DONT UNDERSTAND
                    matches=matches+1 #Add one to variable matches introduced above

        if matches == len(s):
            isOkay=1
        return isOkay


#--------------------------
def main():
    pass


if __name__ == '__main__':
    main()
#---------------------------


dna = sequence() #Define DNA as apart of the sequence class.  Can now use functions
dna.set()  #Sets class variable seq to string "atcg"
dna.check_seq()


