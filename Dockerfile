FROM python:3.12-slim

RUN pip install --no-cache-dir markitdown-mcp

COPY start.py .

CMD ["python", "start.py"]
