import subprocess
import os
import yara
from pathlib import Path

def scan_with_clamav(dev_path):
    """Scan the USB device using ClamAV"""
    try:
        result = subprocess.run(
            ['clamscan', '-r', dev_path],
            capture_output=True,
            text=True
        )
        print("[*] ClamAV Scan Results:")
        print(result.stdout)
        return result.returncode == 0
    except Exception as e:
        print(f"[-] ClamAV scan failed: {str(e)}")
        return False

def scan_with_yara(dev_path):
    """Scan the USB device using YARA rules"""
    try:
        # Load YARA rules from the rules directory
        rules_dir = Path(__file__).parent.parent / 'rules'
        rules = yara.compile(str(rules_dir / 'sample.yara'))
        
        # Scan the device
        matches = rules.match(dev_path)
        
        if matches:
            print("[!] YARA matches found:")
            for match in matches:
                print(f"  - Rule: {match.rule}")
                print(f"    Tags: {match.tags}")
                print(f"    Meta: {match.meta}")
        else:
            print("[+] No YARA matches found")
            
        return len(matches) == 0
    except Exception as e:
        print(f"[-] YARA scan failed: {str(e)}")
        return False

def scan_usb(dev_path):
    """Main scanning function that orchestrates both ClamAV and YARA scans"""
    print(f"[*] Starting security scan for {dev_path}")
    
    clamav_safe = scan_with_clamav(dev_path)
    yara_safe = scan_with_yara(dev_path)
    
    return clamav_safe and yara_safe 