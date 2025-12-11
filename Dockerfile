FROM python:3.11-slim
WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8001


# CMD ["python", "bot.py"]
CMD ["uvicorn", "app.fast_api_app:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
