FROM alpine:latest

RUN apk add --no-cache socat
RUN apk add dos2unix

COPY entrypoint.sh /entrypoint.sh
RUN dos2unix /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]



COPY ./ping.sh /ping.sh
RUN dos2unix /ping.sh
CMD [ "/ping.sh" ]
