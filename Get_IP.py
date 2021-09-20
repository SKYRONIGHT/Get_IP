#SKYRONIGHT

import socket

#Here You Need to Typy The Url Of A Website.

hostname = input("Please Enter The Website Url:\n")

print(f"The {hostname} IP Address is {socket.gethostbyname(hostname)}")
