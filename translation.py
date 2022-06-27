import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""<b>I Am Mega Link Downloader To Telegram Bot</b>"""
    
    DOWNLOAD_START = "<b>Downloading ⬇️</b>"
    UPLOAD_START = "<b>Uploading ⬆️</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "<b>• Downloaded In <b>{}</b> Seconds \n• Uploaded In <b>{}</b> Seconds"
    SAVED_CUSTOM_THUMB_NAIL = "<b>Custom Thumbnail Saved</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>Thumbnail Cleared</b>"

    HELP_USER = f"""<b>Personal</b>"""
