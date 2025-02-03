from nextcord import slash_command
from nextcord.ext.commands import Cog


class BadgeCog(Cog):
    def __init__(self): ...
    @slash_command()
    async def test1(self, inter):
        await inter.guild.create_auto_moderation_rule(
            name="test1",
            actions=[AutoModerationAction(type=AutoModerationActionType.block_message)],
            trigger_metadata=AutoModerationTriggerMetadata(
                keyword_filter=["i hate maskduck"]
            ),
        )

    @slash_command()
    async def test2(self, inter):
        await inter.guild.create_auto_moderation_rule(
            name="test2",
            actions=[AutoModerationAction(type=AutoModerationActionType.block_message)],
            trigger_metadata=AutoModerationTriggerMetadata(
                keyword_filter=["i hate maskduck"]
            ),
        )


def setup(bot):
    bot.add_cog(BadgeCog())
