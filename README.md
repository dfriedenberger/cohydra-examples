# cohydra-examples

## start "Ping" Test  (example from cohydra repo https://github.com/osmhpi/cohydra )

```
python basic_example.py  
```

## start "Real Time Protocol" Test  (see srtp_example.py)

```
python srtp_example.py  
```

### validate dropped Packets

#### Logfiles
```
root@docker-desktop:~/dev/simulation-logs/2021-02-02-14-59-29# grep "word:" srtp-receiver.stdout.log | wc -l     
113
root@docker-desktop:~/dev/simulation-logs/2021-02-02-14-59-29# grep "sending word" srtp-sender.stdout.log | wc -l
250
```
#### Wireshark
```
simulation-logs/2021-02-02-14-59-29/srtp-receiver.ns3-eth0.pcap 
```

## notes (only for me :-) 
### create srtp-container
```
docker build -t frittenburger/cohydra/srtp docker/srtp
```

#### create network once
```
docker network create --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 srtp-network
```

```
docker network ls                                                                   
NETWORK ID     NAME           DRIVER    SCOPE
e2500b5fe8ff   srtp-network   bridge    local
```

### start receive service
```
docker run --rm -t --network=srtp-network --ip=172.20.240.1 --name srtp-receiver -p 1111:1111/udp frittenburger/cohydra/srtp /root/libsrtp-2.3.0/test/rtpw -e 128 -k aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa -r 172.20.240.1 1111 
```

### validate ip 
```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' srtp-receiver
```


### start sender
```
docker run --rm --network=srtp-network --name srtp-sender -t frittenburger/cohydra/srtp /root/libsrtp-2.3.0/test/rtpw -w /root/libsrtp-2.3.0/test/words.txt -e 128 -k aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa -s 172.20.240.1 1111
```


