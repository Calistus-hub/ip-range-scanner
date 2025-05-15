from optparse import OptionParser
import ipaddress

parser = OptionParser()
parser.add_option("-t", "--target", dest="target", help="Enter the IP range like 192.168.1.0/24")
(options, arguments) = parser.parse_args()

if not options.target:
    parser.error("You must give an IP range using -t or --target")

try:
    ip_range = ipaddress.ip_network(options.target, strict=False)
    print("The IP addresses in the range are:")
    for ip in ip_range.hosts():
        print(ip)
except ValueError:
    parser.error("The IP range is not correct. Use format like 192.168.1.0/24")