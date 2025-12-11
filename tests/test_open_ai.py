from app.open_ai import get_sql_from_question


def test_sql_generation_count_all():
    sql = get_sql_from_question("Сколько всего видео есть в системе?")
    assert "COUNT" in sql
    assert "videos" in sql
