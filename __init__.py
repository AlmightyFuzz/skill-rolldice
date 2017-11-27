import logging
from random import randint, choice
from functools import partial

from opsdroid.matchers import match_regex


RESPONSE_TEMPLATES = ['{name} rolled {roll}',
                      'roll for {name} gave {roll}',
                      'the dice show {roll} for {name}',
                      'probability gifts {name} with a roll of {roll}',
                      '{name} got a roll of {roll}']


def setup(opsdroid):
    logging.debug("Loaded dice-roll module")


@match_regex(r'[Rr]oll (?P<ndice>\d+)?(?:d(?P<dice>\d+))(?:\+(?P<mod>\d+))?', case_sensitive=False)
async def rolldice(opsdroid, config, message):
    match = message.regex
    ndice = match.group('ndice')
    ndice = int(ndice) if ndice else 1
    dice = int(match.group('dice'))
    mod = match.group('mod')
    mod = int(mod) if mod else 0

    rolls = map(partial(randint, 1), [dice]*ndice)
    total = sum(rolls) + mod

    await message.respond(choice(RESPONSE_TEMPLATES).format(name=message.user,
                                                            roll=total))
