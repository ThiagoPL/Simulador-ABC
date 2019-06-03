# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:55:26 2019

@author: Thiago
"""
from colorama import Fore, Style
class Individual:
    def __init__(self, individualId, sizeOfChromosome, parental, idA, idB):
        self.individualId= individualId
        self.ChromosomeA= [parental]*sizeOfChromosome
        self.IDchromosomeA=idA
        self.ChromosomeB= [parental]*sizeOfChromosome
        self.IDchromosomeB=idB
        
    def printIndividual(self):
        print(str(self.individualId)+'\t', end='')
        for i in range(0, len(self.ChromosomeA)):
            if(self.ChromosomeA[i] == 1):
                print(Fore.BLUE+'1', end='')
            if(self.ChromosomeA[i] == 2):
                print(Fore.RED+'2', end='')
            if(self.ChromosomeA[i] == 3):
                print(Fore.GREEN+'3', end='')
        print("\n\t", end='')
        for i in range(0, len(self.ChromosomeB)):
            if(self.ChromosomeB[i] == 1):
                print(Fore.BLUE+'1', end='')
            if(self.ChromosomeB[i] == 2):
                print(Fore.RED+'2', end='')
            if(self.ChromosomeB[i] == 3):
                print(Fore.GREEN+'3', end='')
        print("")
        print(Style.RESET_ALL) 
    
#    def crossover(self, point):
        

class Population:
    def __init__(self):
        self.Individuals=[]
    
    def initializePopulation(self,numberOfIndividuals, sizeOfChromosome, parental, idA, idB):
        for i in range(0,numberOfIndividuals):
            self.Individuals.append(Individual(i,sizeOfChromosome, parental, idA, idB))
            
    def insertPopulation(self, proportion, sizeOfChromosome, ancestry, idA, idB):   
        numberOfIndividuals=int(proportion*(len(self.Individuals)))
        for i in range(0,numberOfIndividuals):
            self.Individuals.append(Individual(len(self.Individuals),sizeOfChromosome, ancestry, idA, idB))
        
    def printPopulation(self):
        for i in range (0,len(self.Individuals)):
            self.Individuals[i].printIndividual()
            
#    def reproduce:
#        ind = [0]*len(self.Individuals)
        
        #Pairs
#        while(0 in ind):
#            rand1 = random.randint(0,len())
            
        #Cromosome
        
        #Substitution
        
        
        
        
if __name__ == '__main__':
    
    numberOfIndividuals=10
    sizeOfChromosome=20
    parental=3
    
    idA=22
    idB=22
    
    #1 AFR
    #2 EUR
    #3 NAT
    
    
    population= Population()
    population.initializePopulation(numberOfIndividuals, sizeOfChromosome, parental, idA, idB)
    population.printPopulation()
    for i in range(1,2):
        proportion=0.1
        pop=1
        population.insertPopulation(proportion, sizeOfChromosome, pop, idA, idB)
        population.printPopulation()
        print ("=========================================================================================")
        proportion=0.2
        pop=2
        population.insertPopulation(proportion, sizeOfChromosome, pop, idA, idB)
        population.printPopulation()
        print ("=========================================================================================")