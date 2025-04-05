import sys
import os
import subprocess
from scanner import scan_usb
from monitor import trace_behavior

def mount_usb_to_sandbox(dev_path):
    print(f"[+] Mounting {dev_path} into sandbox...")

    # Example using Docker volume passthrough (basic simulation)
    # Replace this with QEMU-based full isolation for production
    docker_cmd = [
        "docker", "run", "--rm", "-v", f"{dev_path}:/mnt/usb:ro", 
        "--network", "none", "usb-sandbox-image"
    ]
    print("[*] Launching Docker container for analysis (simulated)")
    subprocess.run(docker_cmd)

def main():
    if len(sys.argv) < 2:
        print("Usage: sandbox_manager.py <device_path>")
        sys.exit(1)

    dev_path = sys.argv[1]
    print(f"[*] Received device path: {dev_path}")

    # Step 1: Mount in isolated container/VM
    mount_usb_to_sandbox(dev_path)

    # Step 2: Static scan
    print("[*] Running ClamAV and YARA...")
    scan_usb(dev_path)

    # Step 3: Optional dynamic monitoring
    print("[*] Monitoring for behavior...")
    trace_behavior(dev_path)

    print("[✓] Analysis complete.")

if __name__ == "__main__":
    main() 