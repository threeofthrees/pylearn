'''
Created on Sep 25, 2016

@author: Mohibur
'''
import random
import datetime

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"

def generateParent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

def getFitness(guess):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)
    
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)
    
def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = getFitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))
    
random.seed()
startTime = datetime.datetime.now()
bestParent = generateParent(len(target))
bestFitness = getFitness(bestParent)
display(bestParent)

while True:
    child = mutate(bestParent)
    childFitness = getFitness(child)
    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
