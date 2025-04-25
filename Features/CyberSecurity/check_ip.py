import csv

# Step 1: Read unique IPs
def read_unique_ips(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        ips = {ip.strip().strip('"') for row in reader for ip in row if ip.strip()}
    return sorted(ips)

# Step 2: Print links for checking
def print_check_links(ips):
    for ip in ips:
        print(f"IP: {ip}")
        print(f"  Talos:      https://talosintelligence.com/reputation_center/lookup?search={ip}")
        print(f"  VirusTotal: https://www.virustotal.com/gui/ip-address/{ip}")
        print()

# Run
if __name__ == "__main__":
    ip_file = "./Features/CyberSecurity/ips.csv"
    unique_ips = read_unique_ips(ip_file)
    print_check_links(unique_ips)