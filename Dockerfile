#Image from Docker Hub the project is being built on. 
#Pre-exisitng image-alpine is a lightweight version of docker, runs python version 3.7
FROM python:3.7-alpine 

#Optional-shows who maintains the project.  
MAINTAINER John Napier

#Sets Python unbuffered environment variable. 
#Tells Python to run in unbuffered mode-reccomended when running python in docker conatiners. 
#Doesn't allow python to buffer the outputs and prints the, directly. 
ENV PYTHONUNBUFFERED 1

#Stores Dependencies. Copies requirements file in the app DIR, 
#Pastes them to a requirements.txt file in the docker file. 
COPY ./requirements.txt /requirements.txt
#Runs package manager that comes with alpine(apk), 
  #update the registry, don't store registry index on docker file to minimize docker footprint. 
RUN apk add --update --no-cache postgresql-client
#creates alias for dependencies e.g. '.tmp-builds-deps', dependencies follow '\'
RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
    gcc libc-dev linux-headers postgresql-dev 
#Intsalls copied requirements folder and installs it into docker image using pip. 
RUN pip install -r /requirements.txt
#deletes alias 
Run apk del .tmp-build-deps 

#Creates DIR in Docker image to store application source code. 
RUN mkdir /app
#Switches to created DIR as default DIR. 
#Any application run with this Docker container will start in this DIR.
WORKDIR /app
#Copies from app folder in app DIR, pastes into app folder created in Docker image.
COPY ./app /app 

#Creates User that runs application using Docker. 
#'user' is the user_name.
RUN adduser -D user 
#Switches to that user. 
#Done for security purposes. Prevents from someone using the application from the root account and gaining root access. 
User user 
