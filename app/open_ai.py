import os
from openai import OpenAI
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

client = OpenAI(api_key=OPENAI_API_KEY)


def get_sql_from_question(question: str) -> str:
    """Send user question to OpenAI and get SQL query back"""
    prompt_path = os.path.join(BASE_DIR, "prompt.txt")
    with open(prompt_path, "r") as f:
        PROMPT = f.read()
    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )
    sql_query = resp.choices[0].message.content.strip()
    print()
    print()
    print()
    print("resp ", resp)
    print("sql_query ", sql_query)
    print()
    print()
    return sql_query

get_sql_from_question("Сколько видео получило хотя бы один комментарий?")