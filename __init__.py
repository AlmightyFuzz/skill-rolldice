from opsdroid.matchers import match_regex
import logging
from random import randint

def setup(opsdroid):
    logging.debug("Loaded dice-roll module")

@match_regex(r'rolld4')
async def rolld4(opsdroid, config, message):
    text = "Roll: {}".format(randint(1,4))
    await message.respond(text)

@match_regex(r'rolld6')
async def rolld6(opsdroid, config, message):
    text = "Roll: {}".format(randint(1,6))
    await message.respond(text)
	
@match_regex(r'rolld8')
async def rolld8(opsdroid, config, message):
    text = "Roll: {}".format(randint(1,8))
    await message.respond(text)
	
@match_regex(r'rolld10\b')
async def rolld10(opsdroid, config, message):
    text = "Roll: {}".format(randint(1,10))
    await message.respond(text)
	
@match_regex(r'rolld12')
async def rolld12(opsdroid, config, message):
    text = "Roll: {}".format(randint(1,12))
    await message.respond(text)
	
@match_regex(r'rolld20')
async def rolld20(opsdroid, config, message):
    text = "Roll: {}".format(randint(1,20))
    await message.respond(text)
	
@match_regex(r'rolld100')
async def rolld100(opsdroid, config, message):
    text = "Roll: {}".format(randint(1,100))
    await message.respond(text)
