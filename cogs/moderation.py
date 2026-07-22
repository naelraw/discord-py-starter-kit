import discord
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
    """Commandes de modération de base."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Supprime un nombre spécifique de messages.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        if amount < 1 or amount > 100:
            await interaction.response.send_message("Veuillez indiquer un nombre entre 1 et 100.", ephemeral=True)
            return

        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(
            f"🧹 `{len(deleted)}` message(s) nettoyé(s) par {interaction.user.mention}.",
            ephemeral=True
        )

    @clear.error
    async def clear_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("Permissions insuffisantes (Gérer les messages).", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))
