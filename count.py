""" count.py - Basic counter commands for use with events.py
    Copyright (C) 2019  GriffinG1

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import discord
from discord.ext import commands


class Count:

    def __init__(self, bot):
        self.bot = bot
        self.bot.counter = True  # Would normally be stored in main.py. Handles toggling of counter.
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=210.0, type=commands.BucketType.channel)
    async def wait(self, ctx):
        """Returns how long it's gonna take"""
        if self.bot.counter:
            if not ctx.channel.id == 0:
                await ctx.message.delete()
                ctx.command.reset_cooldown(ctx)
                try:
                    return await ctx.author.send("This command is restricted to <#1>. Please try again there.")
                except discord.Forbidden:
                    return await ctx.send("This command is restricted to <#1>. Please try again there.")
            with open("tally.txt") as f:
                tally = f.read()
            await ctx.send("The counter is at **{}** :slight_smile:".format(tally))

    @commands.command(hidden=True)
    async def modify(self, ctx, amount=0):
        """Modify the timer"""
        if ctx.author == ctx.guild.owner and self.bot.counter:
            with open("tally.txt") as f:
                tally = f.read()
                f.close()
            if amount == 0:
                return await ctx.send("No change was made to the counter. It's still at {} :frowning2:".format(tally))
            elif int(tally) + amount <= 0:
                return await ctx.send("Error, you're going into a bad place!")
            else:
                with open("tally.txt", "w") as f:
                    tally = int(tally) + amount
                    f.write(str(tally))
                    f.close()
            if amount < 0:
                true_amount = amount - amount * 2
                await ctx.send("Removed {} from the counter. It is now at **{}** :slight_frown:".format(true_amount, tally))
            else:
                await ctx.send("Added {} to the counter. It is now at **{}** :slight_smile:".format(amount, tally))
        else:
            await ctx.send("You don't have permission to do that!")


def setup(bot):
    bot.add_cog(Count(bot))
