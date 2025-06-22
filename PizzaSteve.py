import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("SERVER_ID"))

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Bot is online as {self.user}")
        guild = discord.Object(id=GUILD_ID)
        await self.tree.sync(guild=guild)
        print("Slash commands synced.")

client = MyClient()

@bot.event
async def PizzaSteve(message)
    if message.author.bot:
        return
    if bot.user in message.mentions:
        before = time.perf_counter()
        typing = message.channel.typing()
        await typing.__aenter__()  # Simulate typing to help measure latency
        after = time.perf_counter()
        await typing.__aexit__(None, None, None)

        latency = round((after - before) * 1000)
        
        await message.channel.send("Pizza Steve?\n", latency + "ms")
    elif "pizza steve!" in message.content.lower():
        before = time.perf_counter()
        typing = message.channel.typing()
        await typing.__aenter__()  # Simulate typing to help measure latency
        after = time.perf_counter()
        await typing.__aexit__(None, None, None)

        latency = round((after - before) * 1000)
        
        await message.channel.send("Pizza Steve?\n", latency + "ms")

@client.tree.command(name="userphone", description="hopefully starts userphone", guild=discord.Object(id=GUILD_ID))
async def userphone(interaction: discord.Interaction):
    await interaction.response.send_message('/userphone')

@client.tree.command(name="embed", description="Send a custom embed with title and description", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(
    title="Title of the embed",
    description="Description/body of the embed",
    footer="footer of the embed"
)
async def embed(interaction: discord.Interaction, title: str, description: str, footer: str = None):
    description = description.replace("||", "\n")
    if footer:
        footer = footer.replace("||", "\n")
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color.blue()
    )
    if footer:  
        embed.set_footer(text=footer)
    await interaction.response.send_message(embed=embed)

client.run(TOKEN)
