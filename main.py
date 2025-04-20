# importar las librerías necesarias
import random 
import discord
from discord.ext import commands
import time

# establecer los permisos para leer el contenido de los mensajes
intents = discord.Intents.default()
intents.message_content = True

# definir el prefijo de los comandos
bot = commands.Bot(command_prefix="&", intents=intents)

# cuando el bot se conecta
@bot.event
async def on_ready():
    print(f'hemos iniciado sesión como {bot.user}')

# comando para preguntas de matemática
@bot.command()
async def matematica(ctx):
    preguntas_mates = [
        ("¿cuánto es 5 + 3?", "8"),
        ("¿cuál es la raíz cuadrada de 16?", "4"),
        ("¿cuánto es 12 x 6?", "72"),
        ("si tienes un ángulo de 90°, ¿cómo se llama?", "recto"),
        ("¿cuánto es 2³?", "8")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_mates)

    await ctx.send(f"pregunta de mates: {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for("message", check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

# comando para preguntas de comunicación
@bot.command()
async def comunicacion(ctx):
    preguntas_comu = [
        ("¿qué tipo de palabra es rápidamente?", "adverbio"),
        ("¿cuál es el sinónimo de efímero?", "fugaz"),
        ("¿cuál es el sujeto de la oración: el perro de juan ladra fuerte?", "el perro"),
        ("¿qué significa la palabra sagaz?", "inteligente"),
        ("¿qué figura literaria se usa en 'el viento susurraba en la noche'?", "personificación")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_comu)
    
    await ctx.send(f"la pregunta es: {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    mensaje = await bot.wait_for('message', check=check)
    
    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

# comando para preguntas de inglés
@bot.command()
async def ingles(ctx):
    preguntas_ingles = [
        ("¿cómo se dice perro en inglés?", "dog"),
        ("¿cómo se traduce la palabra 'table'?", "mesa"),
        ("¿cuál es el pasado de 'go'?", "went"),
        ("¿qué significa 'blue' en español?", "azul"),
        ("¿cómo se dice 'grande' en inglés?", "big")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_ingles)

    await ctx.send(f"la pregunta es: {pregunta}")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

# comando para preguntas de ciencias sociales
@bot.command()
async def ciencias_sociales(ctx):
    preguntas_sociales = [
        ("¿quién descubrió américa?", "cristóbal colón"),
        ("¿en qué año comenzó la revolución francesa?", "1789"),
        ("¿cuál fue la primera civilización en américa?", "olmeca"),
        ("¿cuál es la capital de egipto?", "el cairo"),
        ("¿quién escribió la declaración de independencia de ee.uu.?", "thomas jefferson")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_sociales)

    await ctx.send(f"la pregunta es: {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

# comando para preguntas de ciencia y tecnología
@bot.command()
async def ciencia_tecnologia(ctx):
    preguntas_ciencia = [
        ("¿qué gas necesitamos para respirar?", "oxígeno"),
        ("¿cuál es el planeta más grande del sistema solar?", "júpiter"),
        ("¿quién descubrió la ley de la gravedad?", "isaac newton"),
        ("¿qué tipo de energía usa un panel solar?", "solar"),
        ("¿qué elemento tiene el símbolo 'h' en la tabla periódica?", "hidrógeno")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_ciencia)

    await ctx.send(f"la pregunta es: {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

# comando para preguntas de arte y cultura
@bot.command()
async def arte_cultura(ctx):
    preguntas_arte = [
        ("¿quién pintó la mona lisa?", "leonardo da vinci"),
        ("¿cuál es el género musical típico de argentina?", "tango"),
        ("¿cuál es el teatro más famoso de londres?", "globe"),
        ("¿quién escribió romeo y julieta?", "william shakespeare"),
        ("¿cuál es el instrumento musical nacional del perú?", "charango")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_arte)

    await ctx.send(f"la pregunta es: {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

# comando para preguntas de dpcc
@bot.command()
async def dpcc(ctx):
    preguntas_dpcc = [
        ("¿qué es la empatía?", "ponerse en el lugar del otro"),
        ("¿qué significa el derecho a la igualdad?", "todos somos iguales ante la ley"),
        ("¿qué es el bullying?", "acoso escolar"),
        ("¿cuál es la importancia del respeto?", "convivencia armoniosa"),
        ("¿qué significa ser ciudadano?", "tener derechos y deberes")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_dpcc)

    await ctx.send(f"la pregunta es: {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

# comando para preguntas de etp
@bot.command()
async def etp(ctx):
    preguntas_etp = [
        ("¿qué es un emprendimiento?", "iniciar un negocio"),
        ("¿qué significa 'pymes'?", "pequeñas y medianas empresas"),
        ("¿qué es la contabilidad?", "registro de transacciones económicas"),
        ("¿cuál es el objetivo de un currículum vitae?", "presentar experiencia laboral"),
        ("¿qué es el marketing?", "estrategia para vender productos o servicios")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_etp)

    await ctx.send(f"la pregunta es: {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

# comando para preguntas de física
@bot.command()
async def fisica(ctx):
    preguntas_fisica = [
        ("¿cuál es la fórmula del mru?", "v x t = d")
    ]

    pregunta, respuesta_correcta = random.choice(preguntas_fisica)

    await ctx.send(f"la pregunta es: {pregunta}")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    mensaje = await bot.wait_for('message', check=check)

    if mensaje.content.strip().lower() == respuesta_correcta.lower():
        await ctx.send("¡correcto!")
    else:
        await ctx.send(f"nop, la respuesta era: {respuesta_correcta}")

bot.run
