FROM ubuntu:latest

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY sample.cpp .

RUN g++ sample.cpp -o sample

CMD ["./sample"]