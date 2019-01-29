FROM ubuntu:18.04

RUN mkdir /app
WORKDIR /app

# Base install
RUN apt-get update && apt-get install -y zip python3.6 python3.6-dev python3-venv python3-pip git
RUN python3.6 -m venv venv
RUN pip3 install --upgrade pip

# Add local files
COPY templates ./templates
COPY statics ./statics
COPY flaskapp.py morph.tar boot.sh lemma-pos.tar ./
RUN chmod +x boot.sh

# Download and install
ADD https://github.com/ponteineptique/pie/archive/webapp-customization.zip ./
RUN unzip webapp-customization.zip && mv -f ./pie-webapp-customization/* ./ && rm -rf pie-webapp-customization

# Install Pie and Pie Webapp requirements
RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-app.txt

# Small checkup
# RUN ls

ENV PIE_MODEL "<morph.tar,MODE,TEMPS,PERS,NOMB,GENRE,CAS,DEGRE><lemma-pos.tar,lemma,pos>"

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]