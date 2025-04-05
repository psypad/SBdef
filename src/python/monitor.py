import subprocess
import time
import os
from pathlib import Path

def trace_behavior(dev_path):
    """Monitor the behavior of processes accessing the USB device"""
    try:
        # Create a temporary mount point
        mount_point = Path("/tmp/usb_analysis")
        mount_point.mkdir(exist_ok=True)
        
        # Mount the device read-only
        subprocess.run(['mount', '-o', 'ro', dev_path, str(mount_point)])
        
        # Start strace monitoring
        strace_cmd = [
            'strace',
            '-f',  # Follow child processes
            '-e', 'trace=file,process',  # Monitor file and process operations
            '-o', '/tmp/usb_trace.log',
            '--', 'ls', '-la', str(mount_point)
        ]
        
        print("[*] Starting behavior monitoring...")
        process = subprocess.Popen(strace_cmd)
        
        # Monitor for a short period
        time.sleep(5)
        
        # Cleanup
        process.terminate()
        subprocess.run(['umount', str(mount_point)])
        mount_point.rmdir()
        
        # Analyze the trace log
        with open('/tmp/usb_trace.log', 'r') as f:
            trace_data = f.read()
            
        print("[*] Behavior Analysis Results:")
        print(trace_data)
        
        # Clean up the trace log
        os.remove('/tmp/usb_trace.log')
        
        return True
    except Exception as e:
        print(f"[-] Behavior monitoring failed: {str(e)}")
        return False 