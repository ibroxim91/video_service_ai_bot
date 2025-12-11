import pytest
from aiogram.types import Message
from bot import handle_text

class DummyMessage:
    def __init__(self, text):
        self.text = text
        self._answered = None

    async def answer(self, text):
        self._answered = text
        return text

@pytest.mark.asyncio
async def test_handle_text():

    msg = DummyMessage("Сколько всего видео есть в системе?")
    await handle_text(msg)

    assert msg._answered == "358"
