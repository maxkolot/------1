import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from markups import *
from db import Database
import os
from aiogram.types.message import ContentType, Message
from yookassa import *
import time
import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from vidos_30 import circle_30
from circle_60 import circle_60
from aiogram.types import InputFile
from krug import krug1
from aiogram.utils.helper import Helper, HelperMode, ListItem
from orig import circleOrig, circleOrig_30


async def days_to_sec(days):
    return days * 24 * 60 * 60


async def time_sub_day(get_time):
    time_now = int(time.time())
    midlle = int(get_time) - time_now
    if midlle <= 0:
        return False
    else:
        dt = str(datetime.timedelta(seconds=midlle))
        dt = dt.replace('days', 'дней')
        dt = dt.replace('day', 'день')
        return dt

async def clean1 (vi):
    os.remove(vi)
async def clean(vi, vi2):
   os.remove(vi)
   os.remove(vi2)


async def cleanall(vi, vi2, au):
   os.remove(vi)
   os.remove(vi2)
   os.remove(au)



