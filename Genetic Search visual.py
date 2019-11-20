# -*- coding: utf-8 -*-
import pygame
import random
import string

myString = "?+=#$&*()[].<>,!_1234567890 abcdefghijklmnopqrstuvwxyz"
class builtpopulation:
    
    def __init__(self,target,MuRate,maxpop):
        self.population = []
        self.newgen = []
        self.mutationRate = MuRate
        self.gen = 0
        #self.target = target
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
        
        self.pool = []
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
        #print("Gen :",self.gen)
        
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

def listToString(s):  
    str1 = ""   
    for ele in s:  
        str1 += ele  
    return str1  
        
        


#print("start")
target1str = ''
print("="*75)
print("Enter < 16 latters")
target1str = input("Enter String : "or "Hello...!")
print("Latters : "+str(len(target1str)))
target1str = target1str.lower()
print("="*75)
print("(Press Enter to skip) (avg population : 200)")
maxpop = int(input("Enter the Poputation per Generation : ") or "200")
print("="*75)
print("(Press Enter to skip) (avg mutation rate : 0.01)")
MuRate = float(input("Enter the Mutation Rate : ") or "0.01")
print("="*75)
pop = builtpopulation(target1str,MuRate,maxpop)

stop = False
count = 0
updateper= True


#loop    
pygame.init()
 
size = (800, 600)
win = pygame.display.set_mode(size)
pygame.display.set_caption("genetic algo")
clock = pygame.time.Clock()
while not stop:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    if updateper:
        pop.calcFitness(target1str)
        pop.naturalSelection()
        pop.generate()
        #print(pop.population[pop.maxfitnessindex].gens,pop.population[pop.maxfitnessindex].fitness)
        #===========================================================================================
        #font1 = pygame.font.SysFont('comicsans', 30)
        font2 = pygame.font.SysFont('comicsans', 20)
        font = pygame.font.Font("C:/Users/Personal/Documents/python projects/Genetic algo/hpunk.ttf", 30)
        font3 = pygame.font.Font("C:/Users/Personal/Documents/python projects/Genetic algo/oreos.ttf", 30)
        font4 = pygame.font.Font("C:/Users/Personal/Documents/python projects/Genetic algo/East_Lift.ttf", 30)
        font5 = pygame.font.Font("C:/Users/Personal/Documents/python projects/Genetic algo/oreos.ttf", 20)
        win.fill(51)
        
        rgb = (0, 200, 250)
        
        text = font.render('Target :'+str(target1str), 1, rgb)
        win.blit(text, (0,50))
       
        text3 = font3.render(''+listToString(pop.population[pop.maxfitnessindex].gens), 1,rgb)
        win.blit(text3, (0,150))
        
        text4 = font5.render('Generation : '+str(pop.gen), 1,rgb)
        win.blit(text4, (0,200))

        text5 = font5.render('Population : '+str(maxpop), 1,rgb)
        win.blit(text5, (0,225))
        
        text6 = font5.render('Mutation Rate : '+str(MuRate), 1,rgb)
        win.blit(text6, (0,250))
        j = 0
        y = 10
        for i in pop.population:
            #print(str(i.gens))
            text1 = font2.render(''+str(i.gens), 0,rgb)
            win.blit(text1, (480,y))
            y+=12
            j+=1
        
        pygame.draw.rect(win, rgb, [450,0, 15, 600], 2)
        pygame.draw.rect(win, rgb, [454,5, 8, 592], 0)
        pygame.draw.rect(win, rgb, [780,0, 15, 600], 2)
        pygame.draw.rect(win, rgb, [784,5, 8, 592], 0)
        pygame.draw.rect(win, rgb, [0,100, 450, 15], 2)
        pygame.draw.rect(win, rgb, [5,104, 440, 8], 0)
        
        
        pygame.display.update()
        #===========================================================================================
        if(pop.evaluate(target1str)):
            print("done")
            updateper=False
 
        pop.population = pop.newgen.copy()
        count+=1

print("over")
	
pygame.quit()