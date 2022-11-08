import discord
from discord.ext import commands

class help_cg(commands.Cog):
    def __init__(self, bot):
        self.bot =  bot

        self.help_message = """
```
+info Muestra los comandos/informacion
+rep <link> Reproducir la canción seleccionada de youtube
+pausa Pausar la cancion que estas escuchando
+desp Resumir la cancion que pausaste
+saltar Saltar canciones
+cola Ver que canciones estan en cola
+borrar Borrar todas las canciones de la cola
+terminar Termina y sale del chat de voz


utiliza tambien: 

+r
+p
+dp
+s
+c
+b
+t
```
"""

        self.text_channel_text = []

        @commands.Cog.listener()
        async def on_read(self):
            for guild in self.bot.guilds:
                for channel in guild.text_channels:
                    self.text_channel_text.append(channel)
        
            await self.send_to_all(self.help_message)
        
        async def send_to_all(self,msg):
            for text_channel in self.text_channel_text:
                await text_channel.send(msg)


        @commands.command(name='info' , help='Muestra los demas comandos')

        async def help(self, ctx):
            await ctx.send(self.help_message)