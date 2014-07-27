
#!/usr/bin/env python
#Execute a command and read it's output line by line and extract IP addresses
import subprocess, string, re
process = subprocess.Popen('/usr/bin/host -a google.com', shell=True, stdout=subprocess.PIPE);

for line in process.stdout:
	match = re.findall('A	(\d+\.\d+\.\d+\.\d+)', line)
	if match: print match[0]

----------------------------------------------

#!/usr/bin/env python
# control application with expect
import pexpect
import sys

child = pexpect.spawn('ftp ftp.microsoft.com')
child.expect('(?i)name .*: ')
child.sendline('anonymous')
child.expect('(?i)password')
child.sendline('password')
child.expect('ftp> ')
child.sendline('ls')
child.expect('ftp> ')
child.sendline('quit')
print child.before

--------------------------------------------------

#!/usr/bin/env python
# control application with expect
import pexpect
import sys

sites = ['ftp.microsoft.com','ftp.openbsd.org','ftp.ubuntu.com','ftp.adobe.com']

for site in sites:
	print "[*] Accessing %s" % site
	child = pexpect.spawn('ftp',[site],timeout=10)

	child.expect('Name')
	child.sendline('anonymous')

	child.expect('Password')
	child.sendline('')

	child.expect('ftp> ')
	child.sendline('ls')

	child.expect('ftp> ')
	child.sendline('quit')
	print child.before


------------------------------------------------------

#!/usr/bin/env python
# Download and print a page
import urllib2
response = urllib2.urlopen("http://www.bing.com/search?q=test")
print response.read()

------------------------------------------------------

#!/usr/bin/env python
# Download a page and extract data from it
import urllib2,re
response = urllib2.urlopen("http://www.bing.com/search?q=frb")
data = response.read()

matches = re.findall('<div class="sb_tlst"><h3><a href="(.*?)" ', data)
for match in matches:
	print "GOT A HIT:",match


-------------------------------------------------

#!/usr/bin/env python
# Download a page and extract data from it
import urllib2

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='Restricted Access',
                          uri='https://www.thesprawl.org/test/index.html',
                          user='admin',
                          passwd='password')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)

try:
	response = urllib2.urlopen('https://www.thesprawl.org/test/index.html')

except urllib2.HTTPError:
	print "[!] Wrong Login or Password"

else:
	print "[*] Login is correct. Printing returned content..."
	print response.read()


------------------------------------------------


#!/usr/bin/env python
# Download a page and extract data from it
import urllib, urllib2
params = urllib.urlencode(dict(login='admin', password='admin'))
response = urllib2.urlopen('http://thesprawl.org/test/authenticate.php', params)
print response.read()


----------------------------------------------

SCAPY

----------------------------------------------

#!/usr/bin/env python
# Sniffing all packets and displaying summary
from scapy.all import *

def process(pkt):
	print pkt.summary()

sniff(prn=process)


----------------------------------------------
#!/usr/bin/env python
# Sniffing UDP and extracting DNS query ids
from scapy.all import *

def process(pkt):
	if DNS in pkt:
		print pkt[DNS].id

sniff(prn=process,filter="udp")


----------------------------------------------

#!/usr/bin/env python
# Crafting a sample ICMP packet
from scapy.all import *

send(IP(dst="4.2.2.2")/ICMP()/"HELLOOOOO")




----------------------------------------------

#!/usr/bin/env python
# Crafting a sample ICMP packet
from scapy.all import *


pkt = sr1(IP(dst="slashdot.org")/TCP(dport=80,flags="S"))
if pkt:
	if pkt[TCP].flags == 18:
		print "Port is open"
	elif pkt[TCP].flags == 20:
		print "Port is closed"
	else:
		print "Got a weird answer"
	
else:
	print "Target host did not answer"


----------------------------------------------

#!/usr/bin/env python
# Crafting a sample ICMP packet
from scapy.all import *


pkt = sr1(IP(dst="4.2.2.1")/UDP(sport=RandShort())/DNS(qd=DNSQR(qname="google.com")))
if pkt:
	#pkt.show()
	print "Answer:",pkt[DNS].an.rdata
