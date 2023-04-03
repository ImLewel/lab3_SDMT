FROM golang:1.17

WORKDIR /usr/src/golang-app

COPY . .

RUN go build -o build/fizzbuzz

CMD ["./build/fizzbuzz", "serve"]
