from opsdroid.matchers import match_regex
import logging
from random import randint

def setup(opsdroid):
    logging.debug("Loaded dice-roll module")

def roll(upperBound, user):
    return "Roll for {}: {}".format(user, randint(1,upperBound))

@match_regex(r'rolld4')
async def rolld4(opsdroid, config, message):
    await message.respond(roll(4,message.user))

@match_regex(r'rolld6')
async def rolld6(opsdroid, config, message):
    await message.respond(roll(6,message.user))

@match_regex(r'rolld8')
async def rolld8(opsdroid, config, message):
    await message.respond(roll(8,message.user))

@match_regex(r'rolld10\b')
async def rolld10(opsdroid, config, message):
    await message.respond(roll(10,message.user))

@match_regex(r'rolld12')
async def rolld12(opsdroid, config, message):
    await message.respond(roll(12,message.user))

@match_regex(r'rolld20')
async def rolld20(opsdroid, config, message):
    await message.respond(roll(20,message.user))

@match_regex(r'rolld100')
async def rolld100(opsdroid, config, message):
    await message.respond(roll(100,message.user))
