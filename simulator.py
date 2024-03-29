# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:55:26 2019
@author: Thiago
"""
from colorama import Fore, Style
import argparse as ap
import numpy as np
import random


class Individual:
    def __init__(self, individualId, sizeOfChromosome, parental, idA, idB, numberOfPopulations):
        self.individualId = individualId
        self.ChromosomeA = [parental]*sizeOfChromosome
        self.IDchromosomeA = idA
        
        #If Sexual, Y will be B
        self.ChromosomeB = [parental]*sizeOfChromosome
        self.IDchromosomeB = idB
        
        self.ancestry= [0.0]*numberOfPopulations
        
    #Chage this verification print
    def printIndividual(self):
        
        print(self.ancestry)
        print(str(self.individualId)+'\t', end='')
        print("Chromosome :", self.IDchromosomeA, end='\t')
        for i in range(0, len(self.ChromosomeA)):
            if self.ChromosomeA[i] == 1:
                print(Fore.BLUE+'1', end='')
            elif self.ChromosomeA[i] == 2:
                print(Fore.RED+'2', end='')
            elif self.ChromosomeA[i] == 3:
                print(Fore.GREEN+'3', end='')
            else:
                print(Style.RESET_ALL+str(self.ChromosomeA[i]), end='')
        print(Style.RESET_ALL)
        print("\tChromosome :", self.IDchromosomeB, end='\t')
        for i in range(0, len(self.ChromosomeB)):
            if self.ChromosomeB[i] == 1:
                print(Fore.BLUE+'1', end='')
            elif self.ChromosomeB[i] == 2:
                print(Fore.RED+'2', end='')
            elif self.ChromosomeB[i] == 3:
                print(Fore.GREEN+'3', end='')
            else:
                print(Style.RESET_ALL+str(self.ChromosomeB[i]), end='')
        print("")
        print(Style.RESET_ALL)

    def printProportionChromosome(self, chromosome, sizeCentiMorgans, ids, individual, sex, idChromosome):
        position = 1
        string=""
        before = chromosome[0]
        for i in range(1, len(chromosome)):
            if chromosome[i] == before :
                position = position+1
            else:
                proportion = (position/len(chromosome))*sizeCentiMorgans    
                position = 1
                #Temporario

                for namePop, idPop in ids.items():
                    if idPop == before:
                        string=string+namePop+"\t"+str(proportion)+"\t"+idChromosome+"\t"+str(individual)+"\t"+sex+"\n"
                before = chromosome[i]
        
        proportion = (position/len(chromosome))*sizeCentiMorgans    
        for namePop, idPop in ids.items():
            if idPop == before:
                string=string+namePop+"\t"+str(proportion)+"\t"+idChromosome+"\t"+str(individual)+"\t"+sex+"\n"
                
        return string
    
    def printIndividualcM(self, sizeCentiMorgans, ids, chromosome, individual, sex):
        string=""
        if(self.IDchromosomeA == chromosome):
            text=self.printProportionChromosome(self.ChromosomeA,sizeCentiMorgans, ids, individual, sex, chromosome)
            string=string+text
        if(self.IDchromosomeB == chromosome):
            text=self.printProportionChromosome(self.ChromosomeB,sizeCentiMorgans, ids, individual, sex, chromosome)
            string=string+text
        return string

    def getChromosome(self):

        if self.IDchromosomeA == self.IDchromosomeB:
            
            chr1 = []
            chr2 = []
            point = random.randrange(len(self.ChromosomeA))

            for i in range(0, point):
                chr1.append(self.ChromosomeA[i])
                chr2.append(self.ChromosomeB[i])

            for i in range(point, len(self.ChromosomeA)):
                chr1.append(self.ChromosomeB[i])
                chr2.append(self.ChromosomeA[i])

            return(chr1, chr2, self.IDchromosomeA, self.IDchromosomeB)
        else:
            return(self.ChromosomeA,self.ChromosomeB,self.IDchromosomeA, self.IDchromosomeB)    
             
            
            
    def setChromosome(self, chromosome, haplotype, idChromosome):
        if haplotype == 1:
            self.ChromosomeA = chromosome
            self.IDchromosomeA = idChromosome
            
        if haplotype == 2:
            self.ChromosomeB = chromosome
            self.IDchromosomeB = idChromosome

    def calculateAncestryOfIndividuals(self):
        total=0
        for i in range(0,len(self.ancestry)):
            self.ancestry[i]=0.0
        
        for i in range(0,len(self.ChromosomeA)):
            total=total+1
            anc=self.ChromosomeA[i]
            
            self.ancestry[anc]=self.ancestry[anc]+1
            
        for i in range(0,len(self.ChromosomeB)):
            total=total+1
            anc=self.ChromosomeB[i]
            
            self.ancestry[anc]=self.ancestry[anc]+1
        
        for i in range(0,len(self.ancestry)):
            self.ancestry[i] = self.ancestry[i]/total

class Population:
    def __init__(self):
        self.IndividualsMen = []
        self.IndividualsWomen = []

    def initializePopulation(self, numberOfIndividuals, sizeOfChromosome, parental, idA, idB, numberOfPopulations):
                      
        for i in range(0, int(numberOfIndividuals/2)):
            self.IndividualsMen.append(Individual(i, sizeOfChromosome, parental, idA, idB, numberOfPopulations))
            self.IndividualsMen[i].calculateAncestryOfIndividuals()
            
        for i in range(0, int(numberOfIndividuals/2)):
            self.IndividualsWomen.append(Individual(i, sizeOfChromosome, parental, idA, idA, numberOfPopulations))
            self.IndividualsWomen[i].calculateAncestryOfIndividuals()
        
        print("We create "+str(len(self.IndividualsMen))+" men and "+str(len(self.IndividualsWomen))+" women")
        
    def insertPopulation(self, proportion, sizeOfChromosome, ancestry, idA, idB):
        numberOfIndividualsM = int(proportion*(len(self.IndividualsMen)))
        for i in range(0, int(numberOfIndividualsM)):
            self.IndividualsMen.append(Individual(len(self.IndividualsMen),
                                               sizeOfChromosome, ancestry, idA, idB, numberOfPopulations))
            self.IndividualsMen[i].calculateAncestryOfIndividuals()
            
        numberOfIndividualsW = int(proportion*(len(self.IndividualsWomen)))    
        for i in range(0, int(numberOfIndividualsW)):
            self.IndividualsWomen.append(Individual(len(self.IndividualsWomen),
                                               sizeOfChromosome, ancestry, idA, idA, numberOfPopulations))
            self.IndividualsWomen[i].calculateAncestryOfIndividuals()
        print("We insert "+str(numberOfIndividualsM)+" men and "+str(numberOfIndividualsW)+" women")

    def printPopulation(self):
        #print ("Men:")
        for i in range(0, len(self.IndividualsMen)):
            self.IndividualsMen[i].printIndividual()
        #print ("Women:")
        for i in range(0, len(self.IndividualsWomen)):
            self.IndividualsWomen[i].printIndividual()
            
    def printPopulationcM(self, sizeOfChromosome, ids, chromosome, numberOfDiploidIndividuals, numberOfMen, numberOfWomen):
        
        string=""
        returnText=""
        if(chromosome == 'X'):
            
            selectedWomen = [0]*len(self.IndividualsWomen)
            selectedMen = [0]*len(self.IndividualsMen)

            for i in range(0, len(self.IndividualsWomen)):
                selectedWomen[i] = i
            
            for i in range(0, len(self.IndividualsMen)):
                selectedMen[i] = i
                    
            for p in range(numberOfMen):
                index = random.randrange(0, len(selectedMen))
                i1 = selectedMen.pop(index)
                returnText=self.IndividualsMen[i1].printIndividualcM(sizeOfChromosome, ids, chromosome, i1, "M")
                string=string+returnText
                
            for p in range(numberOfWomen):
                index = random.randrange(0, len(selectedWomen))
                i1 = selectedWomen.pop(index)
                returnText=self.IndividualsWomen[i1].printIndividualcM(sizeOfChromosome, ids, chromosome, i1, "W")
                string=string+returnText
        else:
            print("Nao sexual") 
            total=len(self.IndividualsMen)+len(self.IndividualsWomen)
            selected=[0]*(total)
            for i in range(0, len(selected)):
                selected[i] = i
            for p in range(numberOfDiploidIndividuals):
                index = random.randrange(0, len(selected))
                i1 = selected.pop(index)
                
                if(i1 < len(self.IndividualsMen)):
                    returnText=self.IndividualsMen[i1].printIndividualcM(sizeOfChromosome, ids, chromosome, i1, "M")    
                    #print("Imprimindo o individuo (M)"+str(i1))
                    #print(returnText)
                    string=string+returnText
                else:
                    idW=i1-len(self.IndividualsMen)
                    returnText=self.IndividualsWomen[idW].printIndividualcM(sizeOfChromosome, ids, chromosome, i1, "W")
                    #print("Imprimindo o individuo (W)"+str(i1))
                    #print(returnText)
                    string=string+returnText
            
        return string;
    def reproduce(self, sizeOfChromosome, numberOfPopulations):

        #Setting the children
        listChildrenWomen = []
        listChildrenMen = []
        for i in range(0, len(self.IndividualsWomen)):
            listChildrenWomen.append(Individual(i, sizeOfChromosome, 0, 0, 0,numberOfPopulations))

        for i in range(0, len(self.IndividualsMen)):
            listChildrenMen.append(Individual(i, sizeOfChromosome, 0, 0, 0,numberOfPopulations))


        #List of individuals
        selectedWomen = [0]*len(self.IndividualsWomen)
        selectedMen = [0]*len(self.IndividualsMen)

        for i in range(0, len(self.IndividualsWomen)):
            selectedWomen[i] = i
            
        for i in range(0, len(self.IndividualsMen)):
            selectedMen[i] = i
        #print("Cruzando: ")
        #Making pairs
        for p in range(len(self.IndividualsWomen)):
            #print(p)
            #i1 is a woman
            index = random.randrange(0, len(selectedWomen))
            i1 = selectedWomen.pop(index)
            
            #i2 is a man
            index = random.randrange(0, len(selectedMen))
            i2 = selectedMen.pop(index)
            
            #print("Cruzando "+str(i1)+" (M) com "+str(i2)+" (H)")
            
            #Cromosome
            chr1Woman, chr2Woman, id1Woman, id2Woman = self.IndividualsWomen[i1].getChromosome()
            chr1Man, chr2Man, id1Man, id2Man = self.IndividualsMen[i2].getChromosome()
            
            listChildrenWomen[p].setChromosome(chr1Woman, 1, id1Woman)
            listChildrenWomen[p].setChromosome(chr1Man, 2, id1Man)
                        
            listChildrenMen[p].setChromosome(chr2Woman, 1, id2Woman)
            listChildrenMen[p].setChromosome(chr2Man, 2, id2Man)
            
        
        self.IndividualsWomen = listChildrenWomen
        for i in range(0, len(self.IndividualsWomen)):
            self.IndividualsWomen[i].calculateAncestryOfIndividuals()
        
        self.IndividualsMen = listChildrenMen
        for i in range(0, len(self.IndividualsMen)):
            self.IndividualsMen[i].calculateAncestryOfIndividuals()
        #Updating the ancestries
        
# n 500 -r 1 -m 0.8 0.1 0.1 0.1 0.1 0.1 0.1 0.5 0.1 -t 20 19 18 14 13 12 8 7 6 -s EUR NAT AFR AFR EUR NAT NAT AFR EUR -p NAT -q 50 -c 22 -o output
def populationToID(sources):
    ids={}
    number={}
    idVector=[]
    newId=0
    for i in range(0, len(sources)):
        if not(sources[i] in ids):
            ids[sources[i]]=newId
            number[newId]=sources[i]
            newId=newId+1
    print(ids)
    for i in range(0, len(sources)):
        idVector.append(ids.get(sources[i],0))
    return(idVector, ids, number,newId)
    
    

if __name__ == '__main__':
    getOpt = ap.ArgumentParser(description='Simulate migrant tracts based on Genetic Algorithm')
    getOpt.add_argument('-n', help='effective number of diploid people in initial population')
    getOpt.add_argument('-r', help='recombination distance, in centiMorgans')
    getOpt.add_argument('-m', nargs='+',
                        help='migration probabilities to be included in the population')
    getOpt.add_argument('-t', nargs='+', help='migrantion times ')
    getOpt.add_argument('-s', nargs='+', help='source population labels (1- AFR, 2-EUR, 3-NAT)')
    getOpt.add_argument('-p', help='parental population')
    getOpt.add_argument('-o', help='output file name')
    getOpt.add_argument('-q', help='number of individuals (diploid) to be outputed ')
    getOpt.add_argument('-c', help='chromosome to be simulated (sexual chromosome (X) is implemented)')
    getOpt.add_argument('-y', help='Number of X-men to be outputed (chromosome X only)')
    getOpt.add_argument('-x', help='Number of X-women to be outputed (chromosome X only)')
    args = getOpt.parse_args()

    r = float(args.r)
    output = str(args.o)
    numberOfDiploidIndividuals = int(args.q)
    numberOfIndividuals = int(args.n)
    time = np.array(args.t, dtype='int')
    proportions = np.array(args.m, dtype='float')
    
    #Chromosome
    chromosome = str(args.c)
    numberOfMen= -1
    numberOfWomen= -1
    if(chromosome == "X"):
        idB="Y"
        sexual=1        
        numberOfMen= int(args.y)
        numberOfWomen= int(args.x)
        
    #Converting String to Integer ID
    parental = args.p
    sources = args.s
    sources,idsToNumber, numberToIDs, numberOfPopulations = populationToID(sources)
    
    #Converting the parental to ID
    parental=idsToNumber.get(parental)    
    
    sizeOfChromosome = 2000

    population = Population()
    idA = chromosome
    idB = chromosome
  
    sexual=0
    
    population.initializePopulation(numberOfIndividuals, sizeOfChromosome, parental, idA, idB, numberOfPopulations)

    oldest = max(time)
    for i in range(oldest, 0, -1):
        print("Generation "+str(i))
        if i in time:
            for j in range(0, len(time)):
                if i == time[j]:
                    proportion = proportions[j]
                    pop = sources[j]
            print ("Inserting the pop "+str(numberToIDs[pop])+" with proportion "+str(proportion))
            population.insertPopulation(proportion, sizeOfChromosome, pop, idA, idB)
        population.reproduce(sizeOfChromosome,numberOfPopulations)
        #population.printPopulation()
        #input("Press Enter to continue...")
    #population.printPopulation()
    outputFile=open(output, 'w')
    outputFile.write(population.printPopulationcM(r, idsToNumber,chromosome, numberOfDiploidIndividuals, numberOfMen, numberOfWomen))
    outputFile.close()
    
    #Temos que verificar tamanho do cromossomo. Correspondencia entre cM e tamanho vector?
   
