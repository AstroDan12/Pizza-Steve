import discord
from discord import app_commands
import os
import time
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("SERVER_ID"))

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # REQUIRED to read messages
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Bot is online as {self.user}")
        guild = discord.Object(id=GUILD_ID)
        await self.tree.sync(guild=guild)
        print("Slash commands synced.")

    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()

        if self.user in message.mentions or "pizza steve!" in content:
            start = time.perf_counter()
            response = await message.channel.send("Pizza Steve?")
            end = time.perf_counter()
            latency = round((end - start) * 1000)
            
            await response.edit(content=f"Pizza Steve?\nLatency: {latency}ms")

client = MyClient()

@client.tree.command(name="userphone", description="hopefully starts userphone", guild=discord.Object(id=GUILD_ID))
async def userphone(interaction: discord.Interaction):
    await interaction.response.send_message('/userphone')

@client.tree.command(name="embed", description="Send a custom embed with title and description", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(
    title="Title of the embed",
    description="Description/body of the embed",
    footer="Footer of the embed"
)
async def embed(interaction: discord.Interaction, title: str, description: str, footer: str = None):
    description = description.replace("||", "\n")
    if footer:
        footer = footer.replace("||", "\n")
    emb = discord.Embed(title=title, description=description, color=discord.Color.blue())
    if footer:
        emb.set_footer(text=footer)
    await interaction.response.send_message(embed=emb)

client.run(TOKEN)
