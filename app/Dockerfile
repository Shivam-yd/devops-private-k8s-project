FROM python:3.12-slim

WORKDIR /app

RUN useradd \
    --create-home \
    --shell /usr/sbin/nologin \
    appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser app.py .

EXPOSE 5000

ENV ENVIRONMENT=local
ENV APP_VERSION=1.0.0

USER appuser

CMD ["python", "app.py"]
