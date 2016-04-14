fitScoreMax=1.38
outputNum=42
allOperandsList=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001']
        #+-*/         
allOperatorsList=['1010','1011','1100','1101'] #index 0 of list means number 10(+), 1 means 11(-) and so on

def decodeToNumber(bStr):
        
        val= 8*int(bStr[0:1]) + 4*int(bStr[1:2]) + 2*int(bStr[2:3]) + 1*int(bStr[3:4])
        return val

def getFitnessScore(chromosome): #closer the score to 0, better the expression for evolution
        retFitnessScore=0
        calculatedValue=0
        op1=-10000
        op2=-10000
        operator='nothing'

        #print(chromosome)
        
        for i in range(0,len(chromosome)):
            element=chromosome[i]
            
            if element in allOperandsList:
                #if chromosome[i-1] in allOperandsList:
                    if op1 == -10000:
                        op1= decodeToNumber(element)
                    else:
                        op2= decodeToNumber(element)
            
            elif element in allOperatorsList:
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
                        return fitScoreMax+1

                #reset op2 and operator to evaluate further in the expression
                op2=-10000
                operator='nothing'

        calculatedValue= op1

        #calc. fitness score. if calculatedValue = outputNum, then score = 0
        
        if calculatedValue == outputNum:
            retFitnessScore = 0
        else:
            retFitnessScore = abs(calculatedValue - outputNum)/42                                    
        
        return retFitnessScore


getFitnessScore(['0101', '1010', '0101', '1100', '0100','1010','0010'])
