import logging
from random import randint
from functools import partial

from opsdroid.matchers import match_regex


def setup(opsdroid):
    logging.debug("Loaded dice-roll module")


@match_regex(r'roll (?P<ndice>\d+)?(?:d(?P<dice>\d+))(?:\+(?P<mod>\d+))?')
async def rolldice(opsdroid, config, message):
    match = message.regex
    ndice = match.group('ndice')
    ndice = int(ndice) if ndice else 1
    dice = int(match.group('dice'))
    mod = match.group('mod')
    mod = int(mod) if mod else 0

    rolls = map(partial(randint, 1), [dice]*ndice)
    total = sum(rolls) + mod

    await message.respond("Roll for {}: {}".format(message.user, total))
