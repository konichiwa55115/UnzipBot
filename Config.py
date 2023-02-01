import os


class Config:
    API_ID = int(os.environ.get("API_ID", 17983098))  # Change 12345 to your API_ID
    API_HASH = os.environ.get("API_HASH", "ee28199396e0925f1f44d945ac174f64")  # Change None to your API_HASH
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6089522865:AAG0vUsYSBg-BaSfiG1T5E1QTrorjoMDA4U")  # Change None to your BOT_TOKEN
    OWNER_ID = int(os.environ.get("OWNER_ID", 1227193881))  # Change 0 to your OWNER_ID
    OWNER_NAME = os.environ.get("OWNER_NAME", "Tamer19871")  # Change None to your OWNER_NAME

    # For Local Deploys edit above 5 lines.
    # Put your API_ID and OWNER_ID (without comma) and API_HASH,BOT_TOKEN n OWNER_NAME (with commas) below.
    # If got any problem ask in @MysteryBotsChat.
