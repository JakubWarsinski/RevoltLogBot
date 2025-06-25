import os
import revolt
import config
import asyncio
import webserver

from dotenv import load_dotenv
from revolt import Message, Client
from revolt.utils import client_session
from utils.content_validate import is_valid_message
from utils.embed_schema import generate_message_description

load_dotenv()

TOKEN = os.getenv("TOKEN")

class Client(revolt.Client):
    async def on_ready(self):
        cfg = config.ServerData(self)
        await cfg.initialize()

        self.skipped = [
            "01JY9FYY06D1VG90YAAXCTP5YF",
            "01JYC3TJ7K8TTKXDFW1GVSG6M3",
            "01JYC3TTYAD8X3PW51GY3CYJCY",
            "01JYC4EKZSSDAQ8GD3YE4DGR32",
            "01JYGQZFJSY6VE26CJCBAYW6Q9",
            "01JYC3ZR1FH3V5MR66BBS8K2KN"
        ]

        print("Bot is ready!")


    async def on_message(self, message: Message):
        if not is_valid_message(message):
            return

        if message.channel.id in self.skipped:
            return

        await generate_message_description(config.CHANNELS["Posted_Messages"], message, "CREATED", color="#00ff37")


    async def on_message_delete(self, message: Message):
        if not is_valid_message(message):
            return
        
        if message.channel.id in self.skipped:
            return

        await generate_message_description(config.CHANNELS["Removed_Messages"], message, "DELETED", color="#ff2600")


    async def on_message_update(self, before: Message, after: Message):
        if not is_valid_message(after):
            return

        if before.channel.id in self.skipped:
            return

        await generate_message_description(config.CHANNELS["Edited_Messages"], before, "UPDATED", color="#ffd900", second_message=after)


    async def on_channel_update(self, before, after):
        channel_id = before.id
        
        channel_name = next((name for name, id in config.CHANNEL_IDS.items() if id == channel_id), None)

        if channel_name:
            await config.fetch_channel(channel_name)


async def main():
    async with client_session() as session:
        client = Client(session, TOKEN)
        await client.start()

webserver.keep_alive()
asyncio.run(main())