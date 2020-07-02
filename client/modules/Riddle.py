# -*- coding: utf-8-*-
import random
import re
from client import jasperpath

WORDS = ["RIDDLE","RIDDLES"]

def getRiddle():
    return "The person who makes it does not want it,the who person buys it does not use it, the person who uses it does not know they are using it. What is it?"

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by telling a joke.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    joke = getRiddle()

    mic.say(joke)


def isValid(text):
    """
        Returns True if the input is related to riddlesr.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\briddle\b', text, re.IGNORECASE))
