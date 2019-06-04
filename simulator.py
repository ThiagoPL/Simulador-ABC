# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:55:26 2019
@author: Thiago
"""
from colorama import Fore, Style
import random
import argparse as ap
import numpy as np
import os



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
            elif(self.ChromosomeA[i] == 2):
                print(Fore.RED+'2', end='')
            elif(self.ChromosomeA[i] == 3):
                print(Fore.GREEN+'3', end='')
            else:
                print(Style.RESET_ALL+str(self.ChromosomeA[i]), end='') 
        print("\n\t", end='')
        for i in range(0, len(self.ChromosomeB)):
            if(self.ChromosomeB[i] == 1):
                print(Fore.BLUE+'1', end='')
            elif(self.ChromosomeB[i] == 2):
                print(Fore.RED+'2', end='')
            elif(self.ChromosomeB[i] == 3):
                print(Fore.GREEN+'3', end='')
            else:
                print(Style.RESET_ALL+str(self.ChromosomeB[i]), end='') 
        print("")
        print(Style.RESET_ALL) 
    
    def getChromosome(self):
        
        if(self.IDchromosomeA == self.IDchromosomeB):
            chr1=[]
            chr2=[]
            point=random.randrange(len(self.ChromosomeA))
            
            for i in range(0,point):
                chr1.append(self.ChromosomeA[i])
                chr2.append(self.ChromosomeB[i])
            
            for i in range(point,len(self.ChromosomeA)):
                chr1.append(self.ChromosomeB[i])
                chr2.append(self.ChromosomeA[i])
            
            return(chr1,chr2, self.IDchromosomeA,self.IDchromosomeB)
        
    def setChromosome(self, chromosome, haplotype, idChromosome):
        if (haplotype == 1):
            self.ChromosomeA=chromosome
            self.IDchromosomeA= idChromosome
        if (haplotype == 2):
            self.ChromosomeB=chromosome
            self.IDchromosomeB= idChromosome
            
            
            
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
            
    def reproduce(self, sizeOfChromosome):
        
        #Setting the children
        listChildren=[]
        for i in range(0,len(self.Individuals)):
            listChildren.append(Individual(i,sizeOfChromosome, 0, idA, idB))
        
        #List of individuals
        selected=[0]*len(self.Individuals)
        
        for i in range(0, len(self.Individuals)):
            selected[i]=i
        
        #Making pairs
        for p in range(len(self.Individuals) // 2):
           index= random.randrange(0, len(selected))
           i1=selected.pop(index)
           index= random.randrange(0, len(selected))
           i2=selected.pop(index)
           
           #Cromosome
           chr1,chr2, id1, id2=self.Individuals[i1].getChromosome()
           
           listChildren[2*p].setChromosome(chr1,1,id1)
           listChildren[2*p+1].setChromosome(chr2,2,id2)
           
           chr1,chr2, id1, id2=self.Individuals[i2].getChromosome()
           
           listChildren[2*p].setChromosome(chr1,2,id1)
           listChildren[2*p+1].setChromosome(chr2,1,id2)
           
        if(len(selected)!=0):
            index=selected[0]
            
            while(index == selected[0]):
                 index= random.randrange(0, len(selected))
                 
            
            chr1,chr2, id1, id2=self.Individuals[selected[0]].getChromosome()
            listChildren[-1].setChromosome(chr1,1,id1)
            
            chr1,chr2, id1, id2=self.Individuals[index].getChromosome()
            listChildren[-1].setChromosome(chr1,2,id1)
            
            #print(str(selected)+ " "+str(index)
            #Now the children become fathers
        self.Individuals=listChildren
        
if __name__ == '__main__':
     getOpt = ap.ArgumentParser(description='Simulate migrant tracts based on Genetic Algorithm')
     getOpt.add_argument('-n',help='effective number of diploid people in initial population')
     getOpt.add_argument('-r',help='recombination distance, in centiMorgans')
     getOpt.add_argument('-m',nargs='+',help='migration probabilities to be included in the population') 
     getOpt.add_argument('-t',nargs='+',help='migrantion times ')
     getOpt.add_argument('-s',nargs='+',help='source population labels (1- AFR, 2-EUR, 3-NAT)')
     getOpt.add_argument('-p',help='parental population')
     getOpt.add_argument('-q',help='number of chromosome to be simulated')
     getOpt.add_argument('-c',help='number of chromosome')
     args = getOpt.parse_args()
     
     numberOfChromosome=int(args.q)
     chromosome=str(args.c)
     numberOfIndividuals=int(args.n)
     r=float(args.r)
     sources=np.array(args.s,dtype='float')
     time=np.array(args.t,dtype='int')
     proportions= np.array(args.m,dtype='float')
     parental=int(args.p)
     #Temos que verificar tamanho do cromossomo. Correspondencia entre cM e tamanho vector?
     sizeOfChromosome=1000
    
     print(parental)
     idA=chromosome
     idB=chromosome
  
     population= Population()
     population.initializePopulation(numberOfIndividuals, sizeOfChromosome, parental, idA, idB)
     
     oldest=max(time)
     for i in range(oldest,1,-1):
             proportion=0.5
             if i in time:
                 for j in range(0,len(time)):
                     if(i == time[j]):
                         proportion=proportions[j]
                         pop=sources[j]
                 population.insertPopulation(proportion, sizeOfChromosome, pop, idA, idB)
             population.reproduce(sizeOfChromosome)
     population.printPopulation()
