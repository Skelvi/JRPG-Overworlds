import discord
from discord import app_commands
from discord import Intents
import numpy as np
import random, os, sys

id_do_servidor = ()
filenames = os.listdir("images")

class client (discord.Client):
  def __init__(self):
    super().__init__(intents = discord.Intents.default())
    self.synced = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:
      await tree.sync(guild=discord.Object(id=id_do_servidor))
      self.synced = True
    print ('bot funcionando'.format(client))
intents = discord.Intents.default()
intents.message_content = True
aclient = discord.Client (intents=intents)
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='testando')
async def teste(interaction: discord.Interaction):
  await interaction.response.send_message(f"estou funcionando",ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'random', description='imagem randomica')
async def imagem(interacao: discord.Interaction):
  imagens = random.choice(filenames)
  imagemradomica = os.path.join("images", imagens)
  await interacao.response.send_message(file=discord.File(imagemradomica), ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'quiz', description='quiz teste')
async def quiz(interacao: discord.Interaction):
  respostas=np.genfromtxt("lista texto.txt",dtype = str,delimiter=",")
  numquestao=random.randint(0,len(respostas)-1)
  questao = respostas[numquestao]
  imagemnome = questao[0]
  resposta = questao[1]
  y = str(resposta)
  x = str(imagemnome)
  imagemquiz = os.path.join("images", x)
  await interacao.response.send_message(f"Qual é esse jogo?",file=discord.File(imagemquiz),ephemeral=False) 
  msg = await aclient.wait_for('message')
  palpite = msg.content
  print(palpite)
  if palpite == y:
    await interacao.followup.send('certo')
  else:
    await interacao.followup.send('errado')


aclient.run('')