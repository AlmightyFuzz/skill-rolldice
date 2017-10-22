from opsdroid.matchers import match_regex
import logging
from random import randint

def setup(opsdroid):
    logging.debug("Loaded dice-roll module")

@match_regex(r'rolld4')
async def rolld4(opsdroid, config, message):
    text = "Roll: {}".format(randint(1,4))
    await message.respond(text)
