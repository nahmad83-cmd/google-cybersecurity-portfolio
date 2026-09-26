# NIST CSF Incident Analysis

## Incident Summary

Employees were unable to access the company network. Packet-sniffer logs showed a flood of ICMP packets, and the incident was treated as a DDoS event associated with a firewall configuration that allowed excessive ICMP traffic.

## Applying the NIST Cybersecurity Framework

### Identify
Reviewed affected systems, devices, access policies, and the path of the attack to identify security gaps and affected resources.

### Protect
Implemented protective measures including firewall rate limiting for ICMP traffic, checks for spoofed IP addresses, network monitoring, and IDS/IPS capabilities.

### Detect
Improved monitoring for abnormal traffic patterns and detection of suspicious ICMP activity.

### Respond
Outlined actions such as isolating affected systems, restoring critical services, analyzing network logs, communicating with management, and reporting incidents to appropriate authorities when necessary.

### Recover
Prioritized restoration of critical network services, kept non-critical services offline during the incident, and planned staged restoration after malicious traffic subsided.

## Key Takeaway

The NIST CSF provides a structured way to connect technical incident handling with broader security planning across **Identify, Protect, Detect, Respond, and Recover**.

## Skills Demonstrated

NIST CSF, DDoS response, firewall controls, IDS/IPS, network monitoring, incident response, recovery planning, and documentation.
