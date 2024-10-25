import os
import traceback

import discord
import dotenv

from config import bot
from src.global_src.global_embed import no_perm_embed
from src.global_src.global_path import version_path
from src.global_src.global_roles import (
    assistant_director_role_id,
    community_manager_role_id,
    developer_role_id,
    head_of_operations_role_id,
    owner_role_id,
    staff_manager_role_id,
)

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

cogs = ["cogs.gamble"]

for cog in cogs:
    try:
        bot.load_extension(cog)
        print(f'Cog loaded "{cog}"')
    except Exception as e:
        print(f'Error loading cog: "{cog}": {e}')
        traceback.print_exc()

@bot.event
async def on_ready():
    print(f"{bot.user} is not dead lol!")
    await bot.change_presence(activity=discord.Game(name="with Grover ❤️"))


async def get_cog_names(ctx: discord.AutocompleteContext):
    name = ctx.options["name"]
    return [cog for cog in cogs if name.lower() in cog.lower()]


@bot.slash_command(name="reload_cog", description="Reload a specific cog")
async def reload_cog(
    ctx: discord.ApplicationContext,
    name: discord.Option(str, "Cog name to reload", autocomplete=get_cog_names),  # type: ignore
):
    if int(ctx.author.id) != 756509638169460837 and not any(
        role.id
        in [
            staff_manager_role_id,
            community_manager_role_id,
            assistant_director_role_id,
            head_of_operations_role_id,
            developer_role_id,
            owner_role_id,
        ]
        for role in ctx.author.roles
    ):
        if name.lower() in cogs:
            try:
                bot.reload_extension(name.lower())
                await ctx.respond(f'Cog "{name}" reloaded correctly')
            except Exception:
                await ctx.respond(f'Failed to reload cog "{name}"')
            return
        await ctx.respond(f'I can"t find "{name}" :c')
    else:
        await ctx.respond("You are not allowed to use this")


@bot.slash_command(name="kill", description="ONLY USE IN URGENCY CASE")
async def kill(
    ctx: discord.ApplicationContext,
):
    await ctx.defer(ephemeral=True)
    if int(ctx.author.id) != 756509638169460837 and not any(
        role.id
        in [
            staff_manager_role_id,
            community_manager_role_id,
            assistant_director_role_id,
            head_of_operations_role_id,
            developer_role_id,
            owner_role_id,
        ]
        for role in ctx.author.roles
    ):
        await ctx.respond(embed=no_perm_embed, ephemeral=True)
        return
    await ctx.respond("Killing bot...", ephemeral=True)
    await bot.close()


@bot.slash_command(name="version", description="View bot version")
async def version(
    ctx: discord.ApplicationContext,
):
    await ctx.defer(ephemeral=True)
    if int(ctx.author.id) != 756509638169460837 and not any(
        role.id
        in [
            staff_manager_role_id,
            community_manager_role_id,
            assistant_director_role_id,
            head_of_operations_role_id,
            developer_role_id,
            owner_role_id,
        ]
        for role in ctx.author.roles
    ):
        await ctx.respond(embed=no_perm_embed, ephemeral=True)
        return

    version_file = open(version_path, "r")
    version = version_file.read()
    version_file.close()

    await ctx.respond(
        f"{version}.\nPing: `{round(bot.latency * 1000, 2)}`ms", ephemeral=True
    )


bot.run(token)
