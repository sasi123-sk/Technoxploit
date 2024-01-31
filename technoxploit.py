#!/usr/bin/env python3
import subprocess
import argparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def display_banner():
    banner = r"""
  {}
    _____         _                           _       _ _
   |_   _|__  ___| |__  _ __   _____  ___ __ | | ___ (_) |_
     | |/ _ \/ __| '_ \| '_ \ / _ \ \/ / '_ \| |/ _ \| | __|
     | |  __/ (__| | | | | | | (_) >  <| |_) | | (_) | | |_
     |_|\___|\___|_| |_|_| |_|\___/_/\_\ .__/|_|\___/|_|\__|
                                       |_|
                                       - sasikaran.surge.sh
                                       - insta: 0xwhitedevil
    """.format(Fore.GREEN)
    print(banner)

def find_server_version(url):
    try:
        command = f"curl -I {url}"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        headers = output.decode().split('\n')
        for header in headers:
            if header.lower().startswith('server:'):
                return header.strip().split(':', 1)[1].strip()
    except subprocess.CalledProcessError as e:
        print(f"Error fetching headers for {url}: {e}")
    return None

def search_exploits(server_version):
    try:
        command = f"searchsploit {server_version}"
        exploits = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return exploits.decode()
    except subprocess.CalledProcessError as e:
        print(f"Error searching exploits: {e}")
    return None

def main():
    parser = argparse.ArgumentParser(description="Server Version and Exploit Search Tool")
    parser.add_argument("-u", "--url", help="Single URL to analyze")
    parser.add_argument("-l", "--list", help="File containing a list of URLs to analyze")
    parser.add_argument("-help", "--show-help", action="store_true", help="Display this help message")

    args = parser.parse_args()

    if args.show_help:
        parser.print_help()
        return

    display_banner()

    if args.url:
        server_version = find_server_version(args.url)
        if server_version:
            print(f"{Fore.CYAN}Server Version for {args.url}: {server_version}{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}Searching for exploits...{Style.RESET_ALL}")
            exploits = search_exploits(server_version)
            if exploits:
                print(exploits)
            else:
                print(f"{Fore.GREEN}No exploits found.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Unable to determine the server version for {args.url}{Style.RESET_ALL}")

    elif args.list:
        with open(args.list, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                server_version = find_server_version(url)
                if server_version:
                    print(f"\n{Fore.CYAN}Server Version for {url}: {server_version}{Style.RESET_ALL}")
                    print(f"\n{Fore.YELLOW}Searching for exploits...{Style.RESET_ALL}")
                    exploits = search_exploits(server_version)
                    if exploits:
                        print(exploits)
                    else:
                        print(f"{Fore.GREEN}No exploits found.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Unable to determine the server version for {url}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
