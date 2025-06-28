import discord
from discord import app_commands
import os
import time
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("SERVER_ID"))
        
def load_image_links(filepath="images.txt"):
    try:
        with open(filepath, "r") as f:
            return [
                line.strip() for line in f
                if line.strip().startswith("http://") or line.strip().startswith("https://")
            ]
    except FileNotFoundError:
        print("images.txt not found.")
        return []

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

        if self.user in message.mentions or "pizza steve!" in content or any(role.name == "Pizza Steve" for role in message.role_mentions):
            start = time.perf_counter()
            response = await message.channel.send("Pizza Steve?")
            end = time.perf_counter()
            latency = round((end - start) * 1000)
            
            await message.channel.send(f"Latency: {latency}ms")

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
@client.tree.command(name="pizzacat", description="Posts a pizzacat", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(
    channel="channel to send a pizzacat to"
)
async def pizzacat(interaction: discord.Interaction, channel: discord.TextChannel = None):
    if channel:
        target_channel = channel
        try:
            await interaction.response.send_message('Pizzacat sent', ephemeral = True)
            image_links = load_image_links()
            image_url = random.choice(image_links)
            await target_channel.send(image_url)
        except discord.Forbidden:
            await interaction.response.send_message('Permissions not valid for this channel')
    else:
        image_links = load_image_links()
        image_url = random.choice(image_links)
        await interaction.response.send_message(image_url)
        
client.run(TOKEN)
