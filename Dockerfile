FROM ubuntu:18.04

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y zip python3.6 python3.6-dev python3-venv python3-pip
ADD https://github.com/mikekestemont/pie/archive/dev.zip ./
RUN unzip webapp.zip && mv -f ./pie-webapp/* ./ && rm -rf pie-webapp

RUN python3.6 -m venv venv
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-app.txt

COPY model.tar boot.sh ./
RUN chmod +x boot.sh
RUN ls

ENV FLASK_APP app.py
ENV PIE_MODEL /app/model.tar

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]