# Telegram YouTube Bot
This is a Telegram bot that allows users to search and download YouTube videos directly from Telegram, The bot uses the youtube_dl Python library to extract video information and send the file of the requested video to the user in the chat and the user can save it to his device.

# Caching Videos
To reduce the number of downloads and save time, this bot implements a video caching mechanism. If a video has already been downloaded, the bot will send you the cached version instead of downloading it again.

# Running the Bot in a Docker Container
This bot can also be run inside a Docker container.
