#!/usr/bin/env python3

from cohydra import ArgumentParser, Network, DockerNode, Scenario

def main():
    scenario = Scenario()

    net = Network("10.0.0.0", "255.255.255.0")

    programm = "/root/libsrtp-2.3.0/test/rtpw"
    wordlist = "/root/libsrtp-2.3.0/test/words.txt"
    key = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ip = "10.0.0.1"

    #srtp
    receiver_command = "{0} -e 128 -k {1} -r {2} 1111".format(programm,key,ip)
    sender_command = "{0} -e 128 -k {1} -w {2} -s {3} 1111".format(programm,key,wordlist,ip)

    #rtp
    #receiver_command = "{0} -r {1} 1111".format(programm,ip)
    #sender_command = "{0} -w {1} -s {2} 1111".format(programm,wordlist,ip)

    ports = dict()
    ports["1111"] = "1111/udp"
    print(receiver_command)
    print(sender_command)

    node1 = DockerNode('srtp-receiver', docker_build_dir='./docker/srtp', exposed_ports = ports, command=receiver_command)
    node2 = DockerNode('srtp-sender', docker_build_dir='./docker/srtp', command=sender_command)

    net.connect(node1, node2, delay='1000ms')

    scenario.add_network(net)

    with scenario as sim:
        # To simulate forever, just do not specifiy the simulation_time parameter.
        sim.simulate(simulation_time=180)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)