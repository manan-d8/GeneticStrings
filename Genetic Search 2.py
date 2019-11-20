# -*- coding: utf-8 -*-
import random
import string

myString = " abcdefghijklmnopqrstuvwxyz"

class builtpopulation:
    
    def __init__(self,target,MuRate,maxpop):
        self.population = []
        self.newgen = []
        self.mutationRate = MuRate
        self.gen = 0
        for i in range(maxpop):
            self.population.append(DNA(len(target)))
            
    def calcFitness(self,target):
        for i in range(len(self.population)):
            self.population[i].calcfitness(target)
            
    def calctotalfitness(self):
        self.totalfitness = 0
        for i in range(len(self.population)):
            self.totalfitness += self.population[i].fitness
            
    def naturalSelection(self):
        self.calctotalfitness()
        
        self.maxfitness = 0
        self.maxfitnessindex = 0
        for i in range(len(self.population)):
            if(self.maxfitness<self.population[i].fitness):
                self.maxfitness = self.population[i].fitness
                self.maxfitnessindex = i

    def generate(self):
        self.newgen = []
        for i in range(len(self.population)):
            
            a = random.randint(0,self.totalfitness)
            b = random.randint(0,self.totalfitness)
            tempsum = 0
            for i in range(len(self.population)):
                tempsum += self.population[i].fitness
                if(tempsum >= a):
                    p1 = self.population[i]
                    
                    break 
            tempsum = 0
            for i in range(len(self.population)):
                tempsum += self.population[i].fitness
                if(tempsum >= b):
                    p2 = self.population[i]
                    break 
            #print("Fail")
            child = p1.crossover(p2)
            child.mutate(MuRate)
            self.newgen.append(child)
            
        self.gen +=1
        print("Gen :",self.gen)
        
    def evaluate(self,target):
        for i in range(len(self.population)):
            if(self.population[i].isSame(target)):
               print("got it")
               return 1
               pass
        
class DNA:

    def __init__(self,lenOfT):
        self.gens = []
        self.fitness = 0
        
        for i in range(lenOfT):
            self.gens.append(random_string_generator(string.ascii_letters))
            
    def calcfitness(self,target):
        score = 0
        for i in range(len(self.gens)):
            if(self.gens[i] == target[i]):
                score+=1
        self.fitness = score

    def crossover(self,partner):
        child = DNA(len(self.gens))
        
        midpoint = random.randint(0,len(self.gens))
        
        for i in range(len(self.gens)):
            if(i>midpoint):
                child.gens[i] = self.gens[i]
            else:
                child.gens[i] = partner.gens[i]
        return child
        
    def mutate(self,Mrate):
        for i in range(len(self.gens)):
            randno = random.random()
            if(randno < Mrate):
                self.gens[i] = random_string_generator(myString)
    
    def isSame(self,target):
        for i in range(len(self.gens)):
            if(self.gens[i] != target[i]):
                return False
        return True
        pass
                

def random_string_generator(listChar):
    return (''.join(random.choice(listChar)).lower())


print("start")
target1str = 'hello world'
MuRate = 0.01
maxpop = 200
pop = builtpopulation(target1str,MuRate,maxpop)

stop = False
count = 0
#loop    

while not stop:
    
    pop.calcFitness(target1str)
    pop.naturalSelection()
    pop.generate()
    print(pop.population[pop.maxfitnessindex].gens,pop.population[pop.maxfitnessindex].fitness)
    if(pop.evaluate(target1str)):
        stop = True
    pop.population = pop.newgen.copy()
    count+=1
    
    if(count>1000):
        stop=True

print("over")
