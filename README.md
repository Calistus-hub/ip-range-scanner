# IP Range Scanner (Python)

This Python script scans a given IP range and list all possible host IP addresses.

It was created as part of my hands-on learning in Cybersecurity and Ethical Hacking, while exploring Python scripting and networking tools.

#Features

Takes an IP range (CIDR notation) from the command line
Uses Python's built-in 'ipaddress' module to generate all hosts
Simple and effective for small network scans

#Usage

```bash
python3 ip_range_exercise.py -t 192.168.1.0/24

Example Output

The IP addresses in the range are:
192.168.1.1
192.168.1.2
...

Skills Used

Python scripting
IP addressing (CIDR)
Command-line tools
optparse and ipaddress modules
