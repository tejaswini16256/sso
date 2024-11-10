
FROM ubuntu:latest


RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean;


WORKDIR /app


COPY Code.java .


RUN javac Code.java

CMD ["java", "Code"]
