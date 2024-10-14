import subprocess
from termcolor import colored
import argparse


# Function to scan IPs for anonymous FTP login
def scan_ip(ip, output_file):
    cmd = f"nmap --script ftp-anon -p 21 {ip}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if "Anonymous FTP login allowed" in result.stdout:
        print(colored(f"[+] {ip} - Anonymous FTP login allowed", "green"))
        with open(output_file, "a") as outfile:
            outfile.write(f"{ip}\n")
    else:
        print(colored(f"[-] {ip} - No anonymous FTP login", "red"))


# Main function
def main():
    parser = argparse.ArgumentParser(
        description="Scan a list of IPs for anonymous FTP logins."
    )

    # Making input_file a required argument by removing the default None
    parser.add_argument(
        "-i",
        "--input_file",
        type=str,
        required=True,  # This makes the argument mandatory
        help="Path to the file containing the list of IPs.",
    )

    parser.add_argument(
        "-o",
        "--output_file",
        default="anon_ftp_ips.txt",
        help="Path to the output file (default: anon_ftp_ips.txt).",
    )

    args = parser.parse_args()

    # Open the input file and scan each IP
    with open(args.input_file, "r") as infile:
        for line in infile:
            ip = line.strip()
            if ip:
                scan_ip(ip, args.output_file)

    print(colored(f"\nScans complete. Results saved to {args.output_file}.", "yellow"))


if __name__ == "__main__":
    main()
