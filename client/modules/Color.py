# -*- coding: utf-8-*-
import random
import re

WORDS = ["FAVORITE", "COLOR"]

def handle(text, mic, profile):
    mic.say("Blue")


def isValid(text):
    return bool(re.search(r'\bfavorite color\b', text, re.IGNORECASE))
