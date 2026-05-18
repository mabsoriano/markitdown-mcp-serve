FROM python:3.12-slim

RUN pip install --no-cache-dir markitdown-mcp

EXPOSE 8080

CMD markitdown-mcp --http --host 0.0.0.0 --port ${PORT:-8080}
