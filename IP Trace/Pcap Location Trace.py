import os
import socket

import Functions.Networking.Pcap_location
import dpkt


def printPCap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                pass
            else:
                ip = eth.data
                src = socket.inet_ntoa(ip.src)
                dst = socket.inet_ntoa(ip.dst)
                print "[+] Src: {}\t\t\t\tDst: {}\n[+] Src: {}\t\t-->\t\tDst: {}".format\
                    (src, dst,Functions.Networking.Pcap_location.retGeoStr(os.path.abspath(Functions.Networking.Pcap_location.__file__),
                    src),Functions.Networking.Pcap_location.retGeoStr(os.path.abspath(Functions.Networking.Pcap_location.__file__),dst))
        except socket.error as e:
            pass

def main(file):
    f = open(file, "rb")
    pcap = dpkt.pcap.Reader(f)
    printPCap(pcap)


if __name__ == "__main__":
    main(raw_input("Enter Location of file "))
