""" events.py - Counter ticker for use with count.py
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

update_message = """
The counter is now at **{}** :upside_down:
"""
listA = [
]
listB = [
]


class Events:

    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def on_message(self, message):
        if self.bot.counter:
            list_A_ctn = False
            list_B_ctn = False
            badStr = False
            words = message.content.lower().replace(',', '').replace('`', '').split()
            if not message.author.name == self.bot.user.name:
                for word in words:
                    for x in listA:
                        if x == word:
                            list_A_ctn = True
                            break
                    for y in listB:
                        if y == word:
                            list_B_ctn = True
                            break
                if list_B_ctn and list_A_ctn:
                    badStr = True

                if badStr is True:
                    with open("tally.txt") as f:
                        tally = f.read()
                    with open("tally.txt", "w") as f:
                        tally = int(tally) + 1
                        f.write(str(tally))
                    await message.channel.send(update_message.format(tally))
                else:
                    pass
            else:
                pass


def setup(bot):
    bot.add_cog(Events(bot))
