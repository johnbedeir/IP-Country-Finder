import requests

# Function to get the country of IP addresses using the ip-api.com batch endpoint


def get_countries_for_ips(ip_list):
    url = 'http://ip-api.com/batch'
    try:
        response = requests.post(url, json=ip_list)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None


# Load IP addresses from a file
with open('ips.txt', 'r') as file:
    ip_addresses = [line.strip() for line in file if line.strip()]

# Split the IP addresses into chunks of 100 because the batch endpoint has a limit
chunk_size = 100
chunks = [ip_addresses[i:i + chunk_size]
          for i in range(0, len(ip_addresses), chunk_size)]

# Get the countries for the IP addresses
for chunk in chunks:
    results = get_countries_for_ips(chunk)
    if results:
        for result in results:
            country = result.get('country', 'Unknown')
            print(f"{result['query']} is located in {country}")


# Remember to replace 'ips.txt' with the path to your text file containing the IP addresses.
