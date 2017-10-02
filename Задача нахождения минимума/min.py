from function import *
from parameters import *
import random
BEG=0
END=100
NUMBER_VAR=2
MAX_ITERATION=1e5
EPS=1e-5

def Sort(fun, coorginate):
    for i in range(len(fun)):
        for j in range(i+1, len(fun)):
            if(fun[j]<fun[i]):
                fun[j], fun[i]=fun[i], fun[j]
                coorginate[j], coorginate[i]=coorginate[i], coorginate[j]
                                

def mutation(exemplar):
    indexChange=random.randint(0,NUMBER_VAR-1)
    newExemplar=()
    for i in range(NUMBER_VAR):
        if i!=indexChange:
            newExemplar+=((exemplar[i]),)
        else:
            x=exemplar[i]+random.uniform(0,10)-5
            if x<BEG:
                x=BEG
            if x>END:
                x=END
            newExemplar+=(x,)
    return newExemplar

def evolution(parents):
    newGeneration=[]
    for i in range(nextGeneration):
        if i<bestParants:
            newGeneration.append(parents[i])
            newGeneration.append(mutation(parents[i]))
            newGeneration.append(mutation(parents[i]))
        elif i<bestParants+goodParants:
            newGeneration.append(parents[i])
            newGeneration.append(mutation(parents[i]))
        else:
            newGeneration.append(parents[i])
    return newGeneration
    
def genetic():
    generation=[]
    fun=[]
    for i in range(firstGeneration):
        coordinates=()
        for j in range(NUMBER_VAR):
            coordinates+=(random.uniform(BEG,END),)
        generation.append(coordinates)
        fun.append(function(coordinates))
    print('global - ', fun)
    Sort(fun, generation)
    print('global - ', fun)
    globMin=fun[0]
    dotMin=generation[0]
    iteration=1
    while iteration<MAX_ITERATION:
        iteration+=1
        generation=evolution(generation)
        fun=[]
        for i in range(len(generation)):
            fun.append(function(generation[i]))
        Sort(fun, generation)
        if(fun[0]<globMin):
           # if(globMin-fun[0]<EPS):
           #     globMin=fun[0]
           #     dotMin=generation[0]
           #     break
            globMin=fun[0]
            dotMin=generation[0]
    print('global minimum - {:6.7g}'.format(globMin))
    print('dot: ', dotMin)
    print('iteration - ', iteration)

genetic()   
                         
