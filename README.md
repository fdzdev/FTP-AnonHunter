# AnonFTP-Scanner

**AnonFTP-Scanner** is a Python tool designed to scan IP addresses for anonymous FTP logins. It utilizes Nmap’s `ftp-anon` script to check if an FTP server allows anonymous login on port 21 and logs the results to an output file.

## Features
- Scans IP addresses for anonymous FTP access on port 21.
- Logs the results of the scan to a specified output file.
- Color-coded output in the terminal for easy result interpretation.

## Requirements
- Python 3.x
- Nmap
- `termcolor` module (for color-coded output)

To install the required dependencies, run:
```bash
pip install termcolor
```
## Installation
- Clone this repository to your local machine:
```
git clone https://github.com/yourusername/anonftp-scanner.git
```
- Navigate to the cloned repository directory:
```
cd anonftp-scanner
```
