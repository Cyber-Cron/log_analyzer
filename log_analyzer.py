import re
from collections import Counter

def analyze_log(file_path):
	"""
	Analyze the log file and print statistics
	"""
	with open(file_path, 'r') as file:
		lines = file.readlines()

	# Define a pattern to extract IP addresses (modify as needed)
	ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

	# Extract IP addresses from log lines
	ip_addresses = []
	for line in lines:
		ip_addresses.extend(ip_pattern.findall(line))

	# Count occurences of each IP address
	ip_count = Counter(ip_addresses)

	print("Log Analysis Results:")
	print("----------------------")
	for ip, count in ip_count.items():
		print(f"{ip}: {count} occurrences")

if __name__ == "__main__":
	# Replace 'logfile.log' with the path to your log file
	log_file_path = 'logfile.log'
	analyze_log(log_file_path)
