import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "PEGA_AQUI_TU_TOKEN"   # ← Variable en Railway

TRACKER_URL = "https://grabify.link/L8A6UR"
EPSTEIN_IMAGE = "https://cdn.abcotvs.com/dip/images/18170915_111825-wabc-epstein-img.jpg"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot listo como {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="epstein", description="Te envía el troll a tu MD")
async def epstein(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Jeffrey Epstein víctimas",
        description="Haz clic para ver el vídeo completo 👇\n(Cuidado... puede ser fuerte)",
        color=0x000000
    )
    embed.set_image(url=EPSTEIN_IMAGE)

    view = discord.ui.View()
    button = discord.ui.Button(label="Ver el vídeo", style=discord.ButtonStyle.red, url=TRACKER_URL)
    view.add_item(button)

    try:
        await interaction.user.send(embed=embed, view=view)
        await interaction.response.send_message("✅ Te envié el troll a tu privado (MD). Reenvíalo a quien quieras.", ephemeral=True)
    except:
        await interaction.response.send_message("❌ Activa los mensajes privados del servidor.", ephemeral=True)

bot.run(TOKEN)
