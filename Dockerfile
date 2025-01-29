FROM python:3.8-slim-buster

# Install system dependencies needed for building packages
RUN apt update -y && apt install -y gcc build-essential

# Install awscli
RUN apt install awscli -y

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
