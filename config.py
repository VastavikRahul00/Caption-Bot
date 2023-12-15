import os


class Config(object):
    # env vars
    BOT_TOKEN = "6904308427:AAGaakMLSjhfTZvgraGIXYfeZH5DjE-Hfls"  # string
    API_ID = 24064094  # int
    API_HASH = "49ceca00ad75c0491a74093f6893626a"  # string
    
    # db vars
    # keep empty if don't want to add any extra caption
    CAPTION_TEXT = "Forwardby : 💓💓YASH💓💓"  
    # BOTTOM or TOP or NIL
    CAPTION_POSITION = "BOTTOM"  
    ADMIN_USERNAME = "videodertxt"  # without "@". 

    # a list of strings of words to remove from the existing caption
    WORDS_TO_REMOVE = [r".*Download.*"]  
    # a list of regex pattern strings to remove from the existing caption. 
    # For eg. r".*Join.*" will remove the entire line having word Join
    REGEX_PATTERNS = []  

    # keep empty to allow in all channels. Can add multiple channels separated by a comma.
    # Don't forget -100 before the channel ID
    ALLOWED_CHANNELS = []

    # REMOVE or POSTFIX or NIL. Useful for tamilblasters, tamilmv and other webites
    WEBSITE_PREFIX = "POSTFIX"  

    # True or False. Replaces YIFY website with YTS
    YTS_WEBSITE_REPLACE = True 

    # Dictionary of words to replace
    REPLACE_DICTIONARY = {}

    # Replace dot separator with space
    SEPARATOR_SPACE = True
