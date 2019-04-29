FROM ubuntu:18.04

RUN mkdir /app
WORKDIR /app

# Base install
RUN apt-get update && apt-get install -y zip python3.6 python3.6-dev python3-venv python3-pip git
RUN pip3 install --upgrade pip

# Add local files
COPY templates ./templates
COPY statics ./statics
COPY flaskapp.py *.tar boot.sh ./
RUN chmod +x boot.sh

# Install Pie and Pie Webapp requirements
RUN pip3 install https://github.com/hipster-philology/pie-flask/archive/master.zip#egg=flask_pie gunicorn
# Small checkup
# RUN ls

ENV PIE_MODEL "<model-json.tar>"

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]