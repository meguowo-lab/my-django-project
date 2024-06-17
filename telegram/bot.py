from aiogram import Bot
from aiogram.types.input_file import BufferedInputFile


class Channel:
    def __init__(self, bot: Bot, channel_id: str | None) -> None:
        self.bot = bot
        if not channel_id:
            raise Exception("Telegram channel is not specified!")

        self.channel_id = channel_id

    async def send_news(self, author: str, title: str, news_url: str, image: bytes):
        await self.bot.send_photo(
            self.channel_id,
            BufferedInputFile(image, "hello.png"),
            caption=f"автор: {author}\n<b>{title}</b>\n\n<a href={news_url}>читать новость...</a>",
        )
