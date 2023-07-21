import numpy as np
import random

respostas=np.genfromtxt("lista texto.txt",dtype="str",delimiter=",")
numquestao=random.randint(0,len(respostas)-1)
questao = respostas[numquestao]
imagemnome = questao[0]
print(imagemnome)