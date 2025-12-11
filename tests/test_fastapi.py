import pytest
import httpx
from httpx import ASGITransport
from app.fast_api_app import app


@pytest.mark.asyncio
async def test_index_route():
    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.get("/")
        assert resp.status_code == 200
        assert resp.json()["message"] == "Hello index!"


@pytest.mark.asyncio
async def test_webhook_route(monkeypatch):
    dummy_update = {
        "update_id": 123456,
        "message": {
            "message_id": 1,
            "date": 1609459200,
            "chat": {"id": 111, "type": "private"},
            "text": "Сколько всего видео есть в системе?"
        }
    }

    async def fake_feed_update(bot, update):
        return None

    monkeypatch.setattr("app.fast_api_app.dp.feed_update", fake_feed_update)

    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.post("/webhook", json=dummy_update)
        assert resp.status_code == 200
        assert resp.json() == {"ok": True}
