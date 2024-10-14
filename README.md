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
- Ensure you have Nmap installed on your system:
```
sudo apt-get install nmap  # For Debian/Ubuntu-based systems
```

## Usage
- Prepare a text file containing the list of IP addresses you want to scan, with each IP on a new line. Check the file test.txt.
- Run the scanner with the following command:
```
python FTP-AnonHunter.py -i <input_file> [-o <output_file>]
```
--i, --input_file: Path to the file containing the list of IPs (required).
- -o, --output_file: Path to the output file (optional, default: anon_ftp_ips.txt).

## Example
- To scan a list of IP addresses in a file named ip_list.txt and save the results to results.txt:
```
python FTP-AnonHunter.py -i ip_list.txt -o results.txt
```
## Output
The script prints the results to the terminal with color-coded messages:
- Green: Anonymous FTP login is allowed.
- Red: No anonymous FTP login.