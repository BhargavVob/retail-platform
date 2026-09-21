FROM python:3.12-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN useradd --create-home appuser

USER appuser

EXPOSE 8081

ENV APP_VERSION=unknown
ENV PAYMENT_STATUS=FAILED

HEALTHCHECK --interval=10s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8081/health')" || exit 1

CMD ["python", "app.py"]
