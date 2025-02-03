from __future__ import annotations

from code import interact
from types import tag
from typing import TYPE_CHECKING

import typing_extensions
from black import format_cell
from nextcord import SlashOption, slash_command
from nextcord.ext import application_checks as app_checks

from models.basecog import BaseCog

if TYPE_CHECKING:
    from typing import TypeVar

    from nextcord import Interaction
    from nextcord.ext import commands
    from typing_extensions import Self

    BotLike = TypeVar("BotLike", bound=commands.Bot)

TAG_NAME_SLASH_OPTION = SlashOption(name="tag_name", description="The tag's name")


class Tagging(BaseCog):
    def __init__(self: Self, bot: BotLike) -> None:
        self._bot = bot

    @slash_command(name="tag")
    async def _tag(self: Self, inter: Interaction) -> None: ...

    @_tag.subcommand()
    async def create(self: Self, interaction: Interaction) -> None: ...

    @_tag.subcommand()
    async def delete(
        self: Self, interaction: Interaction, tag_name: str = TAG_NAME_SLASH_OPTION
    ):
        if self._bot.db.get_tag_by_name(tag_name)["owner"] != interaction.user.id:
            await interaction.send(
                "You're not allowed to delete this tag. If you want to force delete and **you have administrator permissions**, consider `/tag force delete` instead."
            )

    @_tag.subcommand()
    async def force(self: Self, interaction: Interaction): ...

    @force.subcommand()
    @app_checks.has_permissions(administrator=True)
    async def delete(
        self: Self, interaction: Interaction, tag_name: str = TAG_NAME_SLASH_OPTION
    ) -> None:
        self._bot.db.get_tag_by_name(tag_name).delete()
        await interaction.send("Force-deleted the tag {}.".format(tag_name))


def setup(bot: BotLike) -> None:
    bot.add_cog(Tagging(bot))
