
FROM debian:buster

RUN apt-get update -y
RUN apt-get install -y gcc make procps wget

WORKDIR /root/
RUN wget https://github.com/cisco/libsrtp/archive/v2.3.0.tar.gz
RUN tar -xvzf v2.3.0.tar.gz
WORKDIR /root/libsrtp-2.3.0
RUN ./configure
RUN make

RUN apt-get install -y dos2unix

COPY entrypoint.sh /entrypoint.sh
RUN dos2unix /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]