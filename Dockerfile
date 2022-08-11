FROM jenkins/jenkins:lts
RUN apt-get update
RUN pip install Flask
RUN curl -sSL https://get.docker.com/ | sh
EXPOSE 8080
CMD [ "python3", "service/server.py" ]