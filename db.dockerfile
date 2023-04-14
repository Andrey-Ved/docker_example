FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ~/db

COPY requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt

COPY db ./db

CMD ["python", "-m", "db"]
