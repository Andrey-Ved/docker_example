FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ~/ui

COPY requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt

COPY ui ./ui

CMD ["python", "-m", "ui"]
