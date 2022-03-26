# syntax=docker/dockerfile:1
# Declaration above must be the first line

# Some packages are not tested with Python > 3.9
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create project folder in docker
WORKDIR /code

# Install Django dependencies.
COPY requirements.txt /code/
RUN pip install -r requirements.txt
    # &&\
    # wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
    # sudo apt install ./google-chrome-stable_current_amd64.deb

# Copy code to docker container
COPY . /code/
