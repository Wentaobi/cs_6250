#!/usr/bin/python
# CS 6250 Fall 2016 - Project 7 - SDN Firewall

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import packets
from pyretic.core import packet
import re

def make_firewall_policy(config):
    # TODO - This is where you need to write the functionality to create the
    # firewall. The config is the firewall cfg file that you created or as used in the
    # autograder.  PLEASE DO NOT HARD CODE FIREWALL RULES IN THIS FILE OR YOU WILL LOSE CREDIT.

    # feel free to remove the following "print config" line once you no longer need it
 # for demonstration purposes only, so you can see the format of the config
    rules = []

    for entry in config:

        rule=match()

        if entry['dstip'] != '*':
            rule=rule&match(dstip=IPAddr(entry['dstip']))
        if entry['srcip'] != '*' :
            rule=rule&match(srcip=IPAddr(entry['srcip']))
        if entry ['dstmac'] != '*' :
            rule=rule & match(dstmact=MAC(entry['dstmac']))
        if entry['srcmac'] != '*':
            rule=rule & match(srcmac=MAC(entry['srcmac']))
        if entry['dstport'] != '*':
            if entry['protocol'] == '6' or entry['protocol'] == '17':
                rule=rule & match(protocol=int(entry['protocol']), dstport=int(entry['dstport']),ethtype=packet.IPV4)
            else:
                rule2 = rule & match(dstport=int(entry['dstport']), protocol=6, ethtype=packet.IPV4)
                rules.append(rule2)ñ
                rule = rule & match(dstport=int(entry['dstport']), protocol=17, ethtype=packet.IPV4)
        if entry['srcport'] != '*':
            if entry['protocol'] == '6' or entry['protocol'] == '17':
                rule=rule & match(protocol=int(entry['protocol']), srcport=int(entry['srcport']),ethtype=packet.IPV4)
            else:
                rule2 = rule & match(srcport=int(entry['srcport']), protocol=6, ethtype=packet.IPV4)
                rules.append(rule2)
                rule = rule & match (srcport=int(entry['srcport']), protocol=17, ethtype=packet.IPV4)
        if entry['srcport'] == '*' and entry['dstport'] == '*':
            if entry['protocol'] == '6' or entry['protocol'] == '17':
                rule=rule & match(protocol=int(entry['protocol']), ethtype=packet.IPV4)
            else:
                rule2 = rule & match(protocol=6, ethtype=packet.IPV4)
                rules.append(rule2)
                rule = rule & match (protocol=17, ethtype=packet.IPV4)
        rules.append(rule)
        pass

    allowed=~(union(rules))
    print allowed
    return allowed
