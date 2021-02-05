#!/bin/sh

sleep 10

until ip a show ns3-eth0 &> /dev/null
do
  echo 'waiting for network connection ...'
  sleep 1
done


echo "ping"
ping  -c 1 srtp-receiver

echo "$@"
exec "$@"
