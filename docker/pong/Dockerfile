FROM alpine:latest

RUN apk add dos2unix

COPY entrypoint.sh /entrypoint.sh
RUN dos2unix /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["tail", "-f", "/dev/null"]
