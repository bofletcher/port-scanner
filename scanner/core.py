import socket

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Attempt TCP connect scan on one port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        sock.close()
        return True
    except:
        return False
