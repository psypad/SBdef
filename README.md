# SBdef

# 🔐 USB Firewall – Isolated USB Malware Detection System

> A hybrid C++ and Python-based software firewall that intercepts USB device connections and dynamically analyzes them in an isolated sandbox environment to detect malicious behavior or software.

---

## 📜 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Security Model](#security-model)
- [Planned Features](#planned-features)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

The **USB Firewall** project aims to protect systems against USB-borne threats by isolating and analyzing USB devices in real-time. Upon detection of a USB insertion event, the device is redirected to a sandbox where its contents and potential behaviors are scanned and monitored.

This project is ideal for:
- Security researchers
- Forensics investigators
- Cybersecurity enthusiasts
- Systems developers working on endpoint protection

---

## ✨ Features

- 🔌 USB device monitoring with event interception (via C++ `udev` listener)
- 🧪 On-the-fly sandbox instantiation using QEMU or Docker
- 🦠 File scanning using ClamAV and YARA rules
- 🔍 Dynamic behavior tracing via `strace`, `auditd`, or Python-based syscall wrappers
- 📋 Logging and alert system
- 🧊 Optional GUI/TUI dashboard for scan results (planned)
- 🛡 USB whitelisting and policy enforcement (planned)

---

## 🏗 Architecture

```plaintext
+---------------------------+
|     USB Detection (C++)  |
|     - libudev, udev rules|
+------------+--------------+
             |
             v
+---------------------------+
|     Sandbox Manager       |
|     - Python orchestrator |
|     - Launch QEMU/Docker  |
+------------+--------------+
             |
             v
+---------------------------+
|   Static Malware Scanning |
|     - ClamAV/YARA         |
+------------+--------------+
             |
             v
+---------------------------+
|  Dynamic Behavior Monitor |
|     - strace, auditd, etc |
+------------+--------------+
             |
             v
+---------------------------+
|     Report & Alert Engine |
|     - JSON logs or GUI    |
+---------------------------+
```

---

## ⚙️ Getting Started

### System Requirements

| Component          | Requirement                           |
|--------------------|----------------------------------------|
| OS                 | Linux (Ubuntu 20.04+, Arch, etc.)      |
| C++ Compiler       | GCC/G++ 9+ or Clang                    |
| Python             | Python 3.8+                            |
| Virtualization     | QEMU/KVM or Docker                     |
| Antivirus Tools    | ClamAV, YARA                           |
| Libraries          | libudev, pyudev, subprocess, json, etc |

---

## 🚀 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourname/usb-firewall.git
cd usb-firewall
```

2. **Install system dependencies**:
```bash
sudo apt update
sudo apt install libudev-dev clamav yara qemu docker.io python3-pip
pip3 install pyudev rich
```

3. **Build the USB event listener (C++)**:
```bash
cd src/cpp
make
```

4. **Run the Python sandbox controller**:
```bash
cd ../python
python3 sandbox_manager.py
```

---

## 🧪 Usage

Once all components are installed and running:

1. Insert a USB device.
2. The C++ daemon detects the insertion and blocks auto-mount.
3. The Python manager launches a sandbox and redirects the USB storage.
4. Static and dynamic scans are performed.
5. Scan results are logged and optionally displayed in the console or GUI.

---

## 🧩 Components

| Component               | Language | Description |
|-------------------------|----------|-------------|
| `usb_listener.cpp`      | C++      | Detects USB insertions via libudev |
| `sandbox_manager.py`    | Python   | Orchestrates sandbox launching and device passthrough |
| `scanner.py`            | Python   | Runs ClamAV and YARA on USB contents |
| `monitor.py`            | Python   | Uses strace/auditd to monitor process behavior |
| `logger.py`             | Python   | Logs events, results, alerts |
| `rules/`                | N/A      | YARA rules for signature-based malware detection |
| `policies/`             | JSON     | Optional: USB device whitelist/blacklist |

---

## 🔒 Security Model

- **No device is mounted on the host system directly.**
- Devices are attached to isolated environments with limited or no network access.
- Sandboxes run in ephemeral mode (destroyed after each session).
- All file reads/writes are monitored and logged.
- Alerts are generated based on known malware signatures and suspicious behavior.

---

## 🗺 Planned Features

- [ ] GUI Dashboard (Electron/PyQt)
- [ ] Machine learning–based anomaly detection
- [ ] Persistent logging database (SQLite/Elastic)
- [ ] Real-time USB traffic analysis (firmware-level)
- [ ] Kernel module for USB access control
- [ ] Network behavior sandboxing

---

## 🤝 Contributing

We welcome contributions! Please fork the repository and submit a pull request. All code should follow the established style guides (`clang-format` for C++, `black` for Python).

---

## 🪪 License

This project is licensed under the MIT License. See `LICENSE` for more information.

---

