from typing import List
from typing import Union
from pyrogram import filters
from config import COMMAND_PREFIXES


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
