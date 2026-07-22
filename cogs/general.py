import discord
from discord import app_commands
from discord.ext import commands

class General(commands.Cog):
    """Commandes d'information et utilitaires généraux."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Vérifie la latence du bot.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong !",
            description=f"Latence du serveur : `{latency} ms`",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="serverinfo", description="Affiche les statistiques du serveur actuel.")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("Cette commande doit être exécutée dans un serveur.", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"Statistiques — {guild.name}",
            color=discord.Color.blue()
        )
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(name="Membres", value=str(guild.member_count), inline=True)
        embed.add_field(name="Canaux", value=str(len(guild.channels)), inline=True)
        embed.add_field(name="Créé le", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))
