import discord
from discord.ext import commands
#Importamos la funcion get_class del archivo
from modelo import get_class #Importamos la funcion get_class del archivo

intencions = discord.Intents.default()
intencions.message_content = True

bot=commands.Bot(command_prefix='!', intents=intencions)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

    
@bot.command()
async def check(ctx):
    #Vamos a trabajar en comando para trabajar con google tachabel machine
    
    if ctx.message.attachments: #Asi verificamos si hay un archivo adjunto
        for archivo in ctx.message.attachments: #Se hace un for para recorrer los archivos adjuntos por si hay mas de uno
            nombre_archivo = archivo.filename #Se obtiene el nombre del archivo
            await archivo.save(f"img/{nombre_archivo}") #Se guarda el archivo en la carpeta actual
            
            
            resutado = get_class(
                model_path="./keras_model.h5", 
                labels_path="labels.txt", 
                image_path=f"img/{nombre_archivo}")
            
            await ctx.send(f"Resultado 🔎\n {resutado}")
            
            #await ctx.send(f"Archivo {nombre_archivo} guardado correctamente.") #Se envia un mensaje al canal de discord indicando que el archivo se guardo correctamente
    else:
        await ctx.send("No hay archivos adjuntos.")
        
bot.run("Tu Token") 