import numpy as np
import random, os
##NAO DEU CERTO,TENTAR FAZER FUNCIONAR DEPOIS
##pegando todos os arquivos da pasta overworlds e quizimages
def overworld():
    overworlds = os.listdir("overworlds")
    imagens = random.choice(overworlds)
    imagemradomica = os.path.join("overworlds", imagens)
    return imagemradomica
def quizzes():
##transfomando os textos do arquivo lista texto.txt em um array 2D
    respostas=np.genfromtxt("lista texto.txt",dtype = str,delimiter=",")
##randomizando um numero dependendo do tamanho do array do arquivo de texto
    numquestao=random.randint(0,len(respostas)-1)
##pegando um array do numero randomizado acima
    questao = respostas[numquestao]
##colocando os objetos do array em variaveis, talvez não seja necessario?
    imagemnome = questao[0]
    resposta1 = questao[1]
    resposta2 = questao[2]
    resposta3 = questao[3]
    resposta4 = questao[4]
##transformando os objetos em array para string para o comando os.path.join conseguir ler
    y = str(resposta1)
    z = str(resposta2)
    o = str(resposta3)
    u = str(resposta4)
    x = str(imagemnome)
    imagemquiz = os.path.join("quizimages", x)
    return y,z,o,u,imagemquiz
##tem muitos comentarios aqui, talvez simplificar?