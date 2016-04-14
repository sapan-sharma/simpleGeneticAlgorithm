## genetic algorithm to find out an expression which solves to any number > -10000
## current program is to find an expression that solves to 10


import random

class simpleArithmaticProblem:

    outputNum=10
    controlValue=500
    rightChromosome = ''
    rightArithmaticString=''    
    offspringPopulationCount=0

    #0:         0000
        #1:         0001
        #2:         0010
        #3:         0011
        #4:         0100
        #5:         0101
        #6:         0110
        #7:         0111
        #8:         1000
        #9:         1001
    allOperandsList=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001']
        #+-*/         
    allOperatorsList=['1010','1011','1100','1101'] #index 0 of list means number 10(+), 1 means 11(-) and so on




    def main(self): #increase Population Until Right Chromosome Is Born

        evolutionProcess='failure'
        parentChromosomes = []
        offspringChromosomes = []

        for i in range(1,100):
            parentChromosomes.append(self.generateRandomChromosome())

##        for i in range(0,10):
##            print(random.choice(parentChromosomes))

        loopCount=0
        while evolutionProcess=='failure' and loopCount< self.controlValue:
            loopCount += 1
            #print('d')
            print(loopCount)


            chosenChroms= self.rouletteWheelSelectionForSex(parentChromosomes)#random.choice(parentChromosomes)
            maleChromosome = chosenChroms[0]
            #print(maleChromosome)#print
            #print(self.getFitnessScore(maleChromosome))
        
            femaleChromosome =chosenChroms[1]
            #print(femaleChromosome)        #print
            #print(self.getFitnessScore(femaleChromosome))


            newOffsprings = self.haveSexAndProduceOffspringChromosomes(maleChromosome,femaleChromosome)
            
            #print('offspring1')
            #print(newOffsprings[0])

##            if loopCount==10:
##                newOffsprings[0]=['0101', '1010', '0101', '1100', '0100','1010','0010']
##                offspringChromosomes.append(newOffsprings[0])
##                evolutionProcess= 'success'
##            else:
            offspringChromosomes.append(newOffsprings[0])
            offspringChromosomes.append(newOffsprings[1])
            #print('offspring2')
            #print(newOffsprings[1])
            print(' :' + str(self.getFitnessScore(newOffsprings[0])) + ' :'+str(self.getFitnessScore(newOffsprings[1])))
            
            if self.getFitnessScore(newOffsprings[0]) == 0 or self.getFitnessScore(newOffsprings[1]) == 0 :
                evolutionProcess= 'success'


        if evolutionProcess== 'success':
            newOffspring1=[]
            if self.getFitnessScore(newOffsprings[0]) == 0:
                newOffspring1 = newOffsprings[0]
            else:
                newOffspring1 = newOffsprings[1]
                
            for i in range(0,len(newOffspring1)):                
                self.rightChromosome+= newOffspring1[i]

            self.rightArithmaticString= self.decodeToArithmaticString(newOffspring1)
            
        #start printing results
        print('rightChromosome= ' +str(self.rightChromosome))
        print('rightArithmaticString= ' +str(self.rightArithmaticString))
        print('offspringPopulation count= ' +str(len(offspringChromosomes)))
        
        return None



    

    def encodeToChromosomes():
        return null
    
    def generateRandomChromosome(self): #if the candidate chromosome doesnt have valid encoded characters, it is not a valid chromosome
        
        retChrom=[]
        
        for i in range(0,random.randint(0,9)):
            retChrom.append(random.choice(self.allOperandsList))
            retChrom.append(random.choice(self.allOperatorsList))
        retChrom.append(random.choice(self.allOperandsList))

        return retChrom




    fitScoreMax=1.38
    def getFitnessScore(self,chromosome): #closer the score to 0, better the expression for evolution
        retFitnessScore=0
        calculatedValue=0
        op1=-10000
        op2=-10000
        operator='nothing'

        #print(chromosome)
        
        for i in range(0,len(chromosome)):
            element=chromosome[i]
            
            if element in self.allOperandsList:
                #if chromosome[i-1] in self.allOperandsList:
                    if op1 == -10000:
                        op1= self.decodeToNumber(element)
                    else:
                        op2= self.decodeToNumber(element)
            
            elif element in self.allOperatorsList:
                operator= element
                
            if op2 >-10000:
                if operator == '1010':
                    op1 = op1 + op2
                if operator == '1011':
                    op1 = op1 - op2
                if operator == '1100':
                    op1 = op1 * op2
                if operator == '1101':
                    try:
                        op1 = op1 / op2
                    except:
                        #print('divide by 0')
                        return self.fitScoreMax+1

                #reset op2 and operator to evaluate further in the expression
                op2=-10000
                operator='nothing'

        calculatedValue= op1

        #calc. fitness score. if calculatedValue = outputNum, then score = 0
        
        if calculatedValue == self.outputNum:
            retFitnessScore = 0
        else:
            retFitnessScore = abs(calculatedValue - self.outputNum)/42                                    
        
        return retFitnessScore



    def decodeToNumber(self, bStr):
        
        val= 8*int(bStr[0:1]) + 4*int(bStr[1:2]) + 2*int(bStr[2:3]) + 1*int(bStr[3:4])
        return val
        


    def rouletteWheelSelectionForSex(self,parentChromosomes):
        chosenChrom=[]
        rouletteWheel =[]
        rouletteWheelLength = 2000 #hard code named rouletteWheelLength instead of circumference because roull. wheel is implemented using a linear data structure
        
        #we'll directly reject chromosomes which evaluate to >|100|. this means that fitness scores >1.38 will be rejected altogehter
        for i in range(0, len(parentChromosomes)):
            fitScore = self.getFitnessScore(parentChromosomes[i])
            if fitScore <= self.fitScoreMax:#1.38
                rouletteWeight = int(round(rouletteWheelLength/1+fitScore,0))
                #print(rouletteWeight)
                for inner in range(0,rouletteWeight):   #upon completion of this for loop, roulette wheel construction is done
                    rouletteWheel.append(i)
        
        #now, time to spin the wheel :)
        chosenPointer = random.choice(rouletteWheel)
        chosenChrom.append(parentChromosomes[chosenPointer])

        #readjust the wheel
        rouletteWheel.remove(chosenPointer)        
        chosenPointer = rouletteWheel[random.randint(0,rouletteWheelLength)] #spin again
        chosenChrom.append(parentChromosomes[chosenPointer])
        
        return chosenChrom






    def haveSexAndProduceOffspringChromosomes(self, chromosome1, chromosome2):
        offsprings = self.crossOver(chromosome1, chromosome2) #there will be two
        self.mutate(offsprings)
        return offsprings





    def crossOver(self, chromosome1, chromosome2):

##        chromosome1=['0111', '1010', '0110', '1010', '0110', '1100', '0111', '1010', '0001']
##        chromosome2=['0101', '1010', '0111', '1101', '0000', '1011', '0111', '1011', '0001', '1010', '1000', '1101', '0000', '1101', '1001', '1011', '0001']

        selList = []
        if len(chromosome1)>len(chromosome2):
            selList=chromosome1
        else:
            selList=chromosome2

        crossoverJunction = random.randint(0,len(selList))

        tempChrom = []

##        print('cr junc ' + str(crossoverJunction))
##        print('before')
##        print(chromosome1)
##        print(chromosome2)

        
        tempChrom=chromosome1[crossoverJunction:]

        
        chromosome1n = chromosome1[:crossoverJunction] + chromosome2[crossoverJunction:]
        chromosome2n = chromosome2[:crossoverJunction] + tempChrom


##        print('after')
##        print(chromosome1n)
##        print(chromosome2n)        

        return [chromosome1n,chromosome2n]



    def mutate(self,offsprings):
##    mutationRate= .001
##
##    if random.randint(1,1/mutationRate) = 1:
        return None
        
        
    
    def decodeToArithmaticString(self, chromosome): #left to right arithmatic string. eg: +1*2-4/10
        retstring=[]
        print(chromosome)
        for element in chromosome:
            print(element)
            if element == '0000':
                retstring.append('0')
            elif element == '0001':
                retstring.append('1')
            elif element == '0010':
                retstring.append('2')
            elif element == '0011':
                retstring.append('3')
            elif element == '0100':
                retstring.append('4')
            elif element == '0101':
                retstring.append('5')
            elif element == '0110':
                retstring.append('6')
            elif element == '0111':
                retstring.append('7')
            elif element == '1000':
                retstring.append('8')
            elif element == '1001':
                retstring.append('9')
            elif element == '1010':
                retstring.append('+')
            elif element == '1011':
                retstring.append('-')
            elif element == '1100':
                retstring.append('*')
            elif element == '1101':
                retstring.append('/')
        
        return retstring

x = simpleArithmaticProblem()
simpleArithmaticProblem.main(x)

