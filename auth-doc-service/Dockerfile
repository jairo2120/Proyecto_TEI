FROM python:3.8-slim-buster

# envioroment api flask 
ENV YOUR_HOST=your_host \
    YOUR_PORT=your_port

WORKDIR /usr/src/auth-doc-service
COPY . .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["code/app.py"]
ENTRYPOINT [ "python3" ]