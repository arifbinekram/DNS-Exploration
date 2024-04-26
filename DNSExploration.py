import dns.resolver
import socket

def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]] + result[1]
    except socket.herror:
        return ["No PTR Record found"]

def DNSRequest(domain):
    ips = []
    try:
        result = dns.resolver.resolve(domain, 'A')
        for answer in result:
            print(f"{domain} {answer.address}")
            reverse_names = ReverseDNS(answer.address)
            print(f"Domain Names: {reverse_names}")
    except dns.resolver.NXDOMAIN:
        print(f"No such domain: {domain}")
    except dns.resolver.Timeout:
        print(f"DNS query timed out for: {domain}")
    except dns.resolver.NoAnswer:
        print(f"No answer returned for: {domain}")
    return ips

def SubdomainSearch(domain, dictionary, nums):
    for word in dictionary:
        subdomain = f"{word}.{domain}"
        DNSRequest(subdomain)
        if nums:
            for i in range(10):
                s = f"{word}{i}.{domain}"
                DNSRequest(s)

# Usage example
domain = "google.com"
dictionary_file = "subdomains.txt"
dictionary = []
with open(dictionary_file, "r") as f:
    dictionary = f.read().splitlines()
SubdomainSearch(domain, dictionary, True)

