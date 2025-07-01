# Scanner-de-IPs

Port Scanner
This Python script provides a simple and effective port scanner that allows you to check the status of common network ports on a given host. It's a useful tool for basic network reconnaissance and security auditing.

How it Works
The script attempts to establish a connection to a predefined list of common ports on the target host. For each port, it reports whether the port is open (meaning a service is listening on that port) or closed (meaning no service is actively listening or the connection was refused).

Key Features
Easy to Use: Simply run the script and provide the IP address or hostname you want to scan.

Common Ports: Scans a default list of frequently used ports, including HTTP, HTTPS, FTP, SSH, and more.

Customizable: The list of ports to scan can be easily modified within the scan_ports function.

Error Handling: Includes basic error handling for invalid hostnames.
