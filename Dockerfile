FROM python:3.9-alpine3.12

ENV PORT=8000
ENV PYTHONUNBUFFERED=TRUE


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]