import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_ID = os.getenv("SERVER_ID")

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Bot is online as {self.user}")
        await self.tree.sync(guild=guild)
        guild = discord.Object(id=GUILD_ID)
        print("Slash commands synced.")

client = MyClient()

@client.tree.command(name="embed", description="Send a custom embed with title and description")
@app_commands.describe(
    title="Title of the embed",
    description="Description/body of the embed",
    footer="footer of the embed"
)
async def embed(interaction: discord.Interaction, title: str, description: str, footer: str = None):
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color.blue()
    )
    if footer:  
        embed.set_footer(text=footer)
    await interaction.response.send_message(embed=embed)

client.run(TOKEN)
