import socket

def scan_target(target, ports, verbose=False):
    """
    Perform a TCP port scan on the given target for the specified ports.
    
    Args:
        target (str): The target IP address or domain.
        ports (list): List of ports (integers) to scan.
        verbose (bool): Enable verbose output.
        
    Returns:
        dict: A dictionary containing the target, a list of open ports, and a list of closed ports.
    """
    open_ports = []
    closed_ports = []
    
    if verbose:
        print(f"[SCAN] Starting TCP scan on {target} for ports: {ports}")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)  # Set timeout to 3 seconds
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                if verbose:
                    print(f"[SCAN] Port {port} is OPEN.")
            else:
                closed_ports.append(port)
                if verbose:
                    print(f"[SCAN] Port {port} is CLOSED.")
        except Exception as e:
            if verbose:
                print(f"[SCAN] Error scanning port {port}: {e}")
            closed_ports.append(port)
        finally:
            sock.close()
    
    results = {"target": target, "open_ports": open_ports, "closed_ports": closed_ports}
    
    if verbose:
        print(f"[SCAN] Scan complete. Results: {results}")
    
    return results
