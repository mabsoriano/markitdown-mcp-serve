FROM python:3.12-slim

RUN pip install --no-cache-dir markitdown-mcp

CMD ["markitdown-mcp", "--http", "--host", "0.0.0.0", "--port", "3001"]
