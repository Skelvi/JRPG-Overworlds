import discord
from discord import app_commands
import random, os, asyncio
import numpy as np

##definindo variaveis importantes como o servidor que o bot ira ficar online e a biblioteca intents
intents = discord.Intents.default()
intents.message_content = True
id_do_servidor =""
aclient = discord.Client (intents=intents)
tree = app_commands.CommandTree(aclient)
listaquiz=[]

##comando para o bot responder quando eles estiver funcionando
@aclient.event 
async def on_ready():
  print ('bot online com o usuario {0.user}'.format(aclient))

##comando de teste basico, talvez excluir depois?
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='testando')
async def teste(interaction: discord.Interaction):
  await interaction.response.send_message(f"estou funcionando",ephemeral = False)

##comando de imagem aleatoria
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'random', description='Pega uma imagem de um mundo de JRPG randômico')
async def imagem(interacao: discord.Interaction):
  overworlds = os.listdir("overworlds")
  imagens = random.choice(overworlds)
  imagemradomica = os.path.join("overworlds", imagens)
  await interacao.response.send_message(file=discord.File(imagemradomica), ephemeral = False)

##comando de quiz basico
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'quiz', description='Teste os seus conhecimentos de JRPGs!')
async def quiz(interacao: discord.Interaction):
##Checando para ver se o usuario já está jogando
  if interacao.user in listaquiz:
    await interacao.response.send_message(f"Você já está em um quiz {interacao.user}!")
  else:
    listaquiz.append(interacao.user)
##transfomando os textos do arquivo lista texto.txt em um array 2D
    respostas=np.genfromtxt("lista texto.txt",dtype = str,delimiter=",")
##randomizando um numero
    numquestao=random.randint(0,len(respostas)-1)
##pegando um array do numero randomizado acima
    questao = respostas[numquestao]
##transformando os objetos em array para string para o comando os.path.join conseguir ler
    y = str(questao[1])
    z = str(questao[2])
    o = str(questao[3])
    u = str(questao[4])
    x = str(questao[0])
    imagemquiz = os.path.join("quizimages", x)
    await interacao.response.send_message(f"{interacao.user} Qual é esse jogo? você tem 15 segundos e uma tentativa só!",file=discord.File(imagemquiz),ephemeral=False)
##checagens do quiz
    while True: 
      try:
        msg = await aclient.wait_for('message', timeout=15) ##pegando a mensagem do cliente,descobrir um jeito de pegar SÓ a messagem de quem chamou
        if msg.channel == interacao.channel and msg.author == interacao.user:
          palpite = msg.content
          if palpite == y or palpite == z or palpite == o or palpite == u:
            await interacao.followup.send(f"Você acertou {interacao.user}")
            break
          else:
            await interacao.followup.send(f"Você errou {interacao.user}.")
            break
      except asyncio.TimeoutError:
        await interacao.followup.send(f"Acabou o tempo {interacao.user}!")
        break
    listaquiz.remove(interacao.user)
    
##token do bot
aclient.run('')