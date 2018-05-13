FROM python:3.6-slim-stretch
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:$PYTHONPATH

RUN mkdir /code
RUN mkdir /config

# Install dependencies
COPY requirements.txt /config/requirements.txt
RUN pip install --no-cache-dir -r /config/requirements.txt

# Copy code
WORKDIR /code
COPY . /code/

VOLUME /code/static
EXPOSE 8000

WORKDIR /code/trest/
CMD ["tail", "-f", "/dev/null"]
