from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase


PREFIX = "."
OWNER_IDS = [703690700314902581]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
            self.VERSION = version
            with open("./lib/bot/token", "r", encoding="utf-8") as tf:
                self.TOKEN = tf.read()
                print('[+] Bot is booting up')
                #print(f"{self.TOKEN=}")
                super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
            print("[+] Bot Online")

    async def on_disconnect(self):
            print("[*] Bot Now Offline")

    async def on_ready(self):
            if not self.ready:
                self.ready = True
                self.guild = self.get_guild(789150188722847795)
                print("[+] Bot Ready")

            else:
                print("[!] Bot Reconnected")

    async def on_message(self, message):
            pass

bot = Bot()