FROM python:3.9.6-alpine

#Add some dockerifle 
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .
