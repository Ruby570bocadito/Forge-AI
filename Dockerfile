FROM python:3.11-slim

LABEL maintainer="AIHACK Team"
LABEL description="AIHACK - AI-Powered Pentesting Suite with Local LLM"
LABEL version="2.0.0"

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    nmap \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash aihack

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R aihack:aihack /app

USER aihack

ENV OLLAMA_HOST=http://host.docker.internal:11434
ENV DEFAULT_MODEL=llama3.2
ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('${OLLAMA_HOST}/api/tags', timeout=5)"

CMD ["python", "main.py"]
