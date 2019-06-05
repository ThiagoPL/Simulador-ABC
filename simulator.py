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
    def __init__(self, individualId, sizeOfChromosome, parental, idA, idB):
        self.individualId = individualId
        self.ChromosomeA = [parental]*sizeOfChromosome
        self.IDchromosomeA = idA
        self.ChromosomeB = [parental]*sizeOfChromosome
        self.IDchromosomeB = idB

    #Chage this verification print
    def printIndividual(self):
        print(str(self.individualId)+'\t', end='')
        for i in range(0, len(self.ChromosomeA)):
            if self.ChromosomeA[i] == 1:
                print(Fore.BLUE+'1', end='')
            elif self.ChromosomeA[i] == 2:
                print(Fore.RED+'2', end='')
            elif self.ChromosomeA[i] == 3:
                print(Fore.GREEN+'3', end='')
            else:
                print(Style.RESET_ALL+str(self.ChromosomeA[i]), end='')
        print("\n\t", end='')
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

    def printProportionChromosome(self, chromosome, sizeCentiMorgans, ids):
        position = 1
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
                        print (namePop+"\t"+str(proportion))
                before = chromosome[i]
        
        proportion = (position/len(chromosome))*sizeCentiMorgans    
        for namePop, idPop in ids.items():
            if idPop == before:
                print (namePop+"\t"+str(proportion))




    def printIndividualcM(self, sizeCentiMorgans, ids):
        
        self.printProportionChromosome(self.ChromosomeA,sizeCentiMorgans, ids)
        print("=========================================================")
        self.printProportionChromosome(self.ChromosomeB,sizeCentiMorgans, ids)
        print("=========================================================")


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

    def setChromosome(self, chromosome, haplotype, idChromosome):
        if haplotype == 1:
            self.ChromosomeA = chromosome
            self.IDchromosomeA = idChromosome
        if haplotype == 2:
            self.ChromosomeB = chromosome
            self.IDchromosomeB = idChromosome



class Population:
    def __init__(self):
        self.Individuals = []

    def initializePopulation(self, numberOfIndividuals, sizeOfChromosome, parental, idA, idB):
        for i in range(0, numberOfIndividuals):
            self.Individuals.append(Individual(i, sizeOfChromosome, parental, idA, idB))

    def insertPopulation(self, proportion, sizeOfChromosome, ancestry, idA, idB):
        numberOfIndividuals = int(proportion*(len(self.Individuals)))
        for i in range(0, numberOfIndividuals):
            self.Individuals.append(Individual(len(self.Individuals),
                                               sizeOfChromosome, ancestry, idA, idB))

    def printPopulation(self):
        for i in range(0, len(self.Individuals)):
            self.Individuals[i].printIndividual()
    def printPopulationcM(self, sizeOfChromosome, ids):
        for i in range(0, len(self.Individuals)):
            self.Individuals[i].printIndividualcM(sizeOfChromosome, ids)


    def reproduce(self, sizeOfChromosome):

        #Setting the children
        listChildren = []
        for i in range(0, len(self.Individuals)):
            listChildren.append(Individual(i, sizeOfChromosome, 0, idA, idB))

        #List of individuals
        selected = [0]*len(self.Individuals)

        for i in range(0, len(self.Individuals)):
            selected[i] = i

        #Making pairs
        for p in range(len(self.Individuals) // 2):
            index = random.randrange(0, len(selected))
            i1 = selected.pop(index)
            index = random.randrange(0, len(selected))
            i2 = selected.pop(index)

            #Cromosome
            chr1, chr2, id1, id2 = self.Individuals[i1].getChromosome()

            listChildren[2*p].setChromosome(chr1, 1, id1)
            listChildren[2*p+1].setChromosome(chr2, 2, id2)

            chr1, chr2, id1, id2 = self.Individuals[i2].getChromosome()

            listChildren[2*p].setChromosome(chr1, 2, id1)
            listChildren[2*p+1].setChromosome(chr2, 1, id2)

        if selected != []:
            index = selected[0]

            while index == selected[0]:
                index = random.randrange(0, len(self.Individuals))


            chr1, chr2, id1, id2 = self.Individuals[selected[0]].getChromosome()
            listChildren[-1].setChromosome(chr1, 1, id1)

            chr1, chr2, id1, id2 = self.Individuals[index].getChromosome()
            listChildren[-1].setChromosome(chr1, 2, id1)

            #print(str(selected)+ " "+str(index)
            #Now the children become fathers
        self.Individuals = listChildren

def populationToID(sources):
    ids={}
    idVector=[]
    newId=0
    for i in range(0, len(sources)):
        if not(sources[i] in ids):
            newId=newId+1
            ids[sources[i]]=newId
    print(ids)
    for i in range(0, len(sources)):
        idVector.append(ids.get(sources[i],0))
    return(idVector, ids)
    
    
#Parameter example: -n 60 -r 10 -m 0.8 0.1 0.1 -t 50 19 18 -s 2 3 1 -p 3 -q 10 -c 20
if __name__ == '__main__':
    getOpt = ap.ArgumentParser(description='Simulate migrant tracts based on Genetic Algorithm')
    getOpt.add_argument('-n', help='effective number of diploid people in initial population')
    getOpt.add_argument('-r', help='recombination distance, in centiMorgans')
    getOpt.add_argument('-m', nargs='+',
                        help='migration probabilities to be included in the population')
    getOpt.add_argument('-t', nargs='+', help='migrantion times ')
    getOpt.add_argument('-s', nargs='+', help='source population labels (1- AFR, 2-EUR, 3-NAT)')
    getOpt.add_argument('-p', help='parental population')
    getOpt.add_argument('-q', help='number of chromosome to be simulated')
    getOpt.add_argument('-c', help='number of chromosome')
    args = getOpt.parse_args()

    r = float(args.r)
    chromosome = str(args.c)
    numberOfChromosome = int(args.q)
    numberOfIndividuals = int(args.n)
    time = np.array(args.t, dtype='int')
    proportions = np.array(args.m, dtype='float')

    #Converting String to Integer ID
    parental = args.p
    sources = args.s
    sources,ids=populationToID(sources)
    
    #Converting the parental to ID
    parental=ids.get(parental)    
    
    sizeOfChromosome = 10


    idA = chromosome
    idB = chromosome

    population = Population()
    population.initializePopulation(numberOfIndividuals, sizeOfChromosome, parental, idA, idB)

    oldest = max(time)
    for i in range(oldest, 0, -1):
        proportion = 0.5
        if i in time:
            for j in range(0, len(time)):
                if i == time[j]:
                    proportion = proportions[j]
                    pop = sources[j]
            population.insertPopulation(proportion, sizeOfChromosome, pop, idA, idB)
        population.reproduce(sizeOfChromosome)
    population.printPopulation()

    population.printPopulationcM(r, ids)

    
    #Temos que verificar tamanho do cromossomo. Correspondencia entre cM e tamanho vector?
   
