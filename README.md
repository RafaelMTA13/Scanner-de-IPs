# 🔎 Python Port Scanner

This is a simple and effective **network port scanner** written in **Python**. It scans a list of commonly used ports on a given host (IP or domain) and reports whether each port is open or closed.

---

## 🚀 Features

- Scans standard ports (FTP, SSH, HTTP, HTTPS, etc.)
- Identifies open and closed ports
- Uses socket-based TCP scanning
- Colored output for readability
- Easy to use and modify

---

## 🧠 Technologies

- Python 3
- `socket` module (standard library)

---

## 🛠️ How to Use

### 1. Clone the repository

```bash
git clone https://github.com/RafaelMTA13/Scanner-de-IPs.git
cd Scanner-de-IPs
```

---

### 2. Run the script

```bash
python port_scanner.py
```

> You must have Python 3 installed on your system.

---

### 3. Example Output

```
Enter the IP address or website to scan: scanme.nmap.org

🔎 Scanning scanme.nmap.org...

✅ Port 22 OPEN (SSH)
⛔ Port 23 CLOSED (Telnet)
✅ Port 80 OPEN (HTTP)
⛔ Port 110 CLOSED (POP3)
...
```

---

## 🔒 License

This project is open-source and available under the **MIT License**.  
You are free to use, modify, and share it.

---

## 👤 Author

Created by **Rafael Monteiro**  
GitHub: [RafaelMTA13](https://github.com/RafaelMTA13)

A personal project for learning and portfolio development.  
Feel free to contribute, fork, or give feedback!
