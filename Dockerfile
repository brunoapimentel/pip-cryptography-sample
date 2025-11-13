FROM registry.access.redhat.com/ubi9/python-311:9.7

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .
COPY pyproject.toml .

CMD ["python", "main.py"]
