# FROM        python:3.12-alpine

# ENV         PYTHONUNBUFFERED=1

# WORKDIR     /home

# COPY        ./requirements.txt .

# COPY        * ./

# RUN         pip install -r requirements.txt \
#             && adduser --disabled-password --no-create-home doe

# USER        doe

# EXPOSE      8000

# CMD         ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]
# Pull base image
FROM python:3.12

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

COPY ./requirements.txt .
# Install dependencies
RUN pip install -r requirements.txt \
    && adduser --disabled-password --no-create-home doe

USER doe

COPY . /code/

EXPOSE 8000