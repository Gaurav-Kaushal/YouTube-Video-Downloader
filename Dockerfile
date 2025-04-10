FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "YT_Video_Downloader.py"]
