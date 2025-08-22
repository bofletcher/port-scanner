import argparse
from scanner.core import scan_port

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target host or IP")
    parser.add_argument("ports", help="Comma-separated ports (e.g. 22,80,443)")
    args = parser.parse_args()

    ports = [int(p.strip()) for p in args.ports.split(",")]
    for port in ports:
        if scan_port(args.host, port):
            print(f"[+] {args.host}:{port} OPEN")
        else:
            print(f"[-] {args.host}:{port} CLOSED")

if __name__ == "__main__":
    main()
