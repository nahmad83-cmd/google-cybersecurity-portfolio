# SYN Flood Incident Analysis

## Incident Summary

A web server became increasingly unresponsive and legitimate users began receiving gateway timeout errors. Network-log analysis showed a high volume of repeated TCP SYN requests from an external source.

## TCP Analysis

A normal TCP three-way handshake uses:

1. **SYN** — client initiates the connection.
2. **SYN-ACK** — server acknowledges and reserves resources.
3. **ACK** — client completes the connection setup.

In the analyzed traffic, repeated SYN requests consumed server resources while legitimate connections began failing. The pattern was consistent with a **SYN flood denial-of-service attack**.

## Effect on Legitimate Users

Early legitimate clients were able to complete TCP handshakes and access the site. As the volume of SYN requests increased, later legitimate clients received resets and gateway timeouts because the server could no longer respond normally.

## Conclusion

The activity demonstrated how transport-layer traffic patterns can reveal availability attacks and how packet-level evidence can be used to explain the effect of an attack on legitimate users.

## Skills Demonstrated

TCP/IP, three-way handshake analysis, SYN flood recognition, DoS investigation, packet-log interpretation, and incident reporting.
