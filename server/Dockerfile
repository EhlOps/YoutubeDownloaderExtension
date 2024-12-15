FROM python:3.12-alpine

RUN apk update
RUN apk upgrade
RUN apk add --no-cache ffmpeg

WORKDIR /server

COPY requirements.txt .

RUN pip install --no-cache-dir -U -r requirements.txt

COPY . .

RUN mkdir /downloads

EXPOSE 8888

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]