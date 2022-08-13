#!/usr/bin/env python3
import os
import sys
def check_reboot():
	""" Returns  True if  Computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

def main():
	if check_reboot():
		print ("Pending reboot")
		sys.exit(1)
		
	print ("Everything is  ok.")
	sys.exit(0)

main()
