import sys
def check(Ip): 
	a = Ip.split(".")
	if int(a[0]) in range(0,256) and int(a[1]) in range(0,256) and int(a[2]) in range(0,256) and int(a[3]) in range(0,256):
		print("The IP address is valid,") 
		if int(a[0]) in range(1,9) and int(a[1]) in range(0,256) and int(a[2]) in range(0,256) and int(a[3]) in range(1,256):                                                                                             
		    print("And is publically assignable")
		elif int(a[0]) in range(11,127) and int(a[1]) in range(0,256) and int(a[2]) in range(0,256) and int(a[3]) in range(1,256):
		    print("And is publically assignable")
		elif int(a[0]) in range(127,128) and int(a[1]) in range(0,1) and int(a[2]) in range(0,1) and int(a[3]) in range(1,256):
		    print("And is publically assignable")
		elif int(a[0]) in range(128,239) and int(a[1]) in range(0,256) and int(a[2]) in range(0,256) and int(a[3]) in range(1,256):
		    print("And is publically assignable")
		else:
			print("But is not publically assignable")
	else: 
		print("Invalid Ip address") 
# Driver Code 
if __name__ == '__main__' : 
	sys.stdout.write("Enter IP address: ")
	sys.stdout.flush()
Ip = sys.stdin.readline()
check(Ip)