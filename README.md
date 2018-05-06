# PyBFD

Small async API wrapper for the [Bots for Discord](https://botsfordiscord.com/) API

## Examples

You dont need discord.py to use PyBFD

```py
import sys
import bfd

client = bfd.Client('YOUR API TOKEN')

async def main():
    profile = client.get_bot(int(sys.argv[1]))

    print(profile)
    print('name:', profile.name)
    print('prefixes:', profile.prefix)
    print('server count:', profile.guild_count)
    print('invite link', profile.invite)
    print('owner:', profile.owner)

client.loop.run_until_complete(main())
```

Embed PyBFD into your bot with commands.

```py
import bfd
from discord.ext import commands

class BFD:
    def __init__(self, bot);
        self.bot = bot
        self.client = bfd.Client('YOUR API TOKEN')

    @commands.command(name='profile')
    async def profile_bot(self, ctx, bot: discord.User):
        profile = await self.client.get_bot(bot.id)

        em = discord.Embed(title=profile.name, description=profile.shortdesc)
        em.add_field(name='prefix', value=profile.prefix)
        em.add_field(name='guilds', value=profile.guild_count)
        em.add_field(name='approved', value=profile.approved)
        em.add_field(name='owner', value=profile.owner.name)

        em.set_thumbnail(url=profile.avatar)
        em.set_footer(text='[invite](%s)' %(profile.invite))

        return await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(BFD(bot))
```

If your bot is using BFD, you'll want to post your server count, here's how to do that with PyBFD

```py
import bfd

class BFDapi:
    def __init__(self, bot):
        self.bot = bot
        self.client = bfd.Client('YOUR API TOKEN')

        self.task = bot.loop.create_task(self.update_guild_count())

    def __unload(self):
        self.task.cancel()

    async def update_guild_count(self):
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            await me.update(server_count=len(self.bot.guilds))
            await asyncio.sleep(1800)

def setup(bot):
    bot.add_cog(BFDapi(bot))
```
