FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ~/api

COPY requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt

COPY api ./api

CMD ["python", "-m", "api"]

