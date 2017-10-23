import logging
from random import randint
from functools import partial

from opsdroid.matchers import match_regex


def setup(opsdroid):
    logging.debug("Loaded dice-roll module")


@match_regex(r'roll (\d+)?(?:d(\d+))(?:\+(\d+))?')
async def rolldice(opsdroid, config, message):
    match = message.regex
    ndice = int(match.group(1))
    dice = int(match.group(2))
    mod = int(match.group(3))

    rolls = map(partial(randint, 1), [dice]*ndice)
    total = sum(rolls) + mod

    await message.respond("Roll for {}: {}".format(message.user, total))
