FROM python:3.7-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY pipeline.py .
CMD [ "python", "pipeline.py"]