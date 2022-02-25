from cProfile import run
from multiprocessing.connection import Client
import discord
from discord.ext import commands
import asyncio
import os
import sys
import re
import json
import sys
from colorama import Fore

client = discord.Client()

async def console():
    
    print("=================================")
    print("███████╗██╗   ██╗ ██████╗██╗  ██╗")
    print("╚════██║██║░░░██║██╔════╝██║░██╔╝")
    print("  ███╔═╝██║░░░██║╚█████╗░█████═╝")
    print("██╔══╝░░██║░░░██║░╚═══██╗██╔═██╗")
    print("███████╗╚██████╔╝██████╔╝██║░╚██╗")
    print("╚══════╝░╚═════╝░╚═════╝░╚═╝░░╚═╝")
    print("=================================")

asyncio.run(console())

token = input('\033[1;90m[\033[1;91m?\033[1;90m] \033[1;96mtoken: ')


@client.event
async def on_ready():
    os.system('cls')
    print('\033[1;36mLogado com sucesso!')
    print('Informações da conta')
    print(f"USER: {client.user.name}")
    print(f"ID: {client.user.id}")

client.run(token, bot=False)
