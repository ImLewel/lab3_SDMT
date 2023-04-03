FROM golang:1.17 as builder

WORKDIR /usr/src/golang-app

COPY . .

RUN CGO_ENABLED=0 go build -o /usr/src/golang-app/build/fizzbuzz

FROM scratch

COPY --from=builder /usr/src/golang-app/build/fizzbuzz /build/
COPY --from=builder /usr/src/golang-app/templates/index.html /templates/


CMD ["/build/fizzbuzz", "serve"]
