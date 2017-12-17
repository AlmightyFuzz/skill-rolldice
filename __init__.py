import logging
from random import randint, choice
from functools import partial

from opsdroid.matchers import match_regex


RESPONSE_TEMPLATES = ['{name} rolled {roll}',
                      'Roll for {name} gave {roll}',
                      'The dice show {roll} for {name}',
                      'Probability gifts {name} with a roll of {roll}',
                      '{name} got a roll of {roll}']

CRIT_HIT_MESSAGE = 'Critical Hit for {name}! Total: {roll}'
CRIT_MISS_MESSAGE = 'Oops! Critical miss for {name}! Total: {roll}'

def setup(opsdroid):
    logging.debug("Loaded dice-roll module")


@match_regex(r'roll (?P<ndice>\d+)?(?:d(?P<dice>\d+))(?:\+(?P<mod>\d+))?', case_sensitive=False)
async def rolldice(opsdroid, config, message):
    match = message.regex
    ndice = match.group('ndice')
    ndice = int(ndice) if ndice else 1
    dice = int(match.group('dice'))
    mod = match.group('mod')
    mod = int(mod) if mod else 0

    crit = None

    rolls = map(partial(randint, 1), [dice]*ndice)
    rolls = list(rolls)
    total = sum(rolls) + mod

    if dice == 20:
        if 20 in rolls: 
            crit = 'critHit'
        if 1 in rolls:
            crit = 'critMiss'

    if crit == 'critHit':
        await message.respond(CRIT_HIT_MESSAGE.format(name=message.user, roll=total))
    elif crit == 'critMiss':
        await message.respond(CRIT_MISS_MESSAGE.format(name=message.user, roll=total))
    else:
        await message.respond(choice(RESPONSE_TEMPLATES).format(name=message.user,
                                                            roll=total))
