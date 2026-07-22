import os
import sys
import asyncio
import discord
from discord.ext import commands
from config import TOKEN, logger

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        """Chargement dynamique des extensions (Cogs) et synchronisation des Slash Commands."""
        logger.info("Chargement des modules (Cogs)...")
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("__"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    logger.info(f"Cog chargé : {filename[:-3]}")
                except Exception as e:
                    logger.error(f"Échec du chargement du Cog {filename}: {e}")

        logger.info("Synchronisation des commandes Slash...")
        synced = await self.tree.sync()
        logger.info(f"Synchronisé {len(synced)} commande(s) Slash globales.")

    async def on_ready(self):
        logger.info(f"Connecté sous le nom : {self.user} (ID: {self.user.id})")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name="/help | Starter Kit v1.0"
            )
        )

async def main():
    if not TOKEN:
        logger.critical("Erreur: Le DISCORD_TOKEN est manquant dans le fichier .env")
        sys.exit(1)

    bot = Bot()
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Arrêt du bot demandé par l'utilisateur.")
