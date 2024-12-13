FROM python:3.12-alpine

WORKDIR /server

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]