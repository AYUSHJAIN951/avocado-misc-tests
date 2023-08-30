Description:
------------
iperf is a tool for active measurements of the maximum achievable
bandwidth on IP networks.

Inputs Needed To Run Tests:
---------------------------
interface		- interface name eth1 or interface mac 02:5d:xx:xx:0x:00 
peer_ip			- IP of the Peer interface to be tested
peer_user		- Username in Peer system to be used
IPERF_SERVER_RUN	- Whether to run iperf server in peer or not (1 to run, 0 to not run)
EXPECTED_THROUGHPUT	- Expected Throughput as a percentage (1-100)
host-IP                 - Specify host-IP for ip configuration.
netmask                 - Specify netmask for ip configuration.

Requirements:
-------------
1. Generate sshkey for your test partner to run the test uninterrupted.
2. Install netifaces using pip. command: pip install netifaces
Peer machine.
