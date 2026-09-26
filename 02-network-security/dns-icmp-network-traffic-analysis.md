# DNS and ICMP Network Traffic Analysis

## Incident Summary

Customers reported a **destination port unreachable** error while attempting to access a website. Network traffic was reviewed using packet-capture information from `tcpdump`.

## Analysis

The browser sent DNS requests using **UDP** to resolve the website's IP address. The traffic showed ICMP error responses indicating that **UDP port 53** on the destination DNS server was unreachable.

The DNS query information also contained indicators consistent with an address-record query. Together, the traffic suggested that DNS communication was impaired and the server was not successfully accepting UDP DNS requests.

## Potential Causes Considered

Possible explanations included:

- DNS service unavailability
- firewall filtering or blocking
- network misconfiguration
- DNS server downtime
- a denial-of-service condition affecting the DNS service

The evidence supported a DNS availability problem, while the exact root cause required further investigation rather than assuming a single cause.

## Skills Demonstrated

DNS, UDP, ICMP, port 53 analysis, tcpdump interpretation, troubleshooting, and incident documentation.
