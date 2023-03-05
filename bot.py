from telegram.ext import Updater, MessageHandler, Filters
from utils import search_download_youtube_video, get_youtube_video
from loguru import logger
from utils import search_download_youtube_video
import os
from collections import OrderedDict
import glob


class LRUCache:

    # initialising capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    # we return the value of the key
    # that is queried in O(1) and return -1 if we
    # don't find the key in out dict / cache.
    # And also move the key to the end
    # to show that it was recently used.
    def get(self, key: bool) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    # first, we add / update the key by conventional methods.
    # And also move the key to the end to show that it was recently used.
    # But here we will also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)
    def put(self, key: str, value: bool) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            lru_key, lru_val = self.cache.popitem(last=False)
            return lru_key
        return None


class Bot:
    def __init__(self, token):
        # create frontend object to the bot programmer
        self.updater = Updater(token, use_context=True)

        # add _message_handler as main internal msg handler
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, self._message_handler))

    def start(self):
        """Start polling msgs from users, this function never returns"""
        self.updater.start_polling()
        logger.info(f'{self.__class__.__name__} is up and listening to new messages....')
        self.updater.idle()

    def _message_handler(self, update, context):
        """Main messages handler"""
        self.send_text(update, f'Your original message: {update.message.text}')

    def send_video(self, update, context, file_path):
        """Sends video to a chat"""
        context.bot.send_video(chat_id=update.message.chat_id, video=open(file_path, 'rb'), supports_streaming=True)

    def send_text(self, update, text, quote=False):
        """Sends text to a chat"""
        # retry https://github.com/python-telegram-bot/python-telegram-bot/issues/1124
        update.message.reply_text(text, quote=quote)


class QuoteBot(Bot):
    def _message_handler(self, update, context):
        to_quote = True

        if update.message.text == "Don\'t quote me please":
            to_quote = False

        self.send_text(update, f'Your original message: {update.message.text}', quote=to_quote)


class YoutubeBot(Bot):
    num_results = 1
    cache_size = 3

    def __init__(self, token):
        super().__init__(token)
        self.cache = LRUCache(YoutubeBot.cache_size)
        video_typs = ["mp4", "mov", "avi", "flv", "3gpp", "wmv", "webm", "mpegs"]
        for v_type in video_typs:
            fileList = glob.glob(f"*.{v_type}", recursive=True)
            for filePath in fileList:
                try:
                    os.remove(filePath)
                except OSError:
                    print("Error while deleting file")

    def _message_handler(self, update, context):
        video_name = update.message.text
        videos = get_youtube_video(video_name)
        if self.cache.get(videos[0]['id']) != -1:
            self.send_text(update, f'Your video for: {update.message.text} from local cache is:')
            # self.send_video(update, context, f"./{videos[0]['title']}-{videos[0]['id']}.*")
            re_to_find = f"./*-{videos[0]['id']}.*"
            fileList = glob.glob(re_to_find, recursive=True)
            # Iterate over the list of filepaths & remove each file.
            for filePath in fileList:
                try:
                    self.send_video(update, context, filePath)
                except OSError:
                    print("Error while deleting file")
        else:
            locations = search_download_youtube_video(video_name)
            self.send_text(update, f'Your video for: {update.message.text} from youtube     is:')
            self.send_video(update, context, f"./{locations[0]}")
            lru_file = self.cache.put(videos[0]['id'], True)
            if lru_file != None:
                # os.remove(f"./{locations[0]}")
                # os.remove(f"*{lru_file}*")
                fileList = glob.glob(f"*{lru_file}*", recursive=True)
                # Iterate over the list of filepaths & remove each file.
                for filePath in fileList:
                    try:
                        os.remove(filePath)
                    except OSError:
                        print("Error while deleting file")


if __name__ == '__main__':
    with open('.telegramToken') as f:
        _token = f.read()

    # my_bot = Bot(_token)
    # my_bot.start()
    # my_bot = QuoteBot(_token)
    # my_bot.start()
    my_bot = YoutubeBot(_token)
    my_bot.start()
