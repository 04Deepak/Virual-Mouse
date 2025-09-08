# base python image
FROM python:3.11-slim

# set working dir inside container
WORKDIR /app

# install system deps for opencv
RUN apt-get update && apt-get install -y \
    libgl1 libglib2.0-0 libsm6 libxext6 libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# copy dependency list
COPY requirements.txt .

# install python deps
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# expose flask port
EXPOSE 5000

# run flask
CMD ["python", "app.py"]
