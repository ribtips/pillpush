import socket
import re
import subprocess

s = socket.socket()
ssh_location = 'XXXXXXXXXXXXXXX:html/' #replace with something like bobsmith @ bobsmith.com

s.bind(('0.0.0.0',8091))
s.listen(0)

regex = re.compile("press")

while True:
	client, addr = s.accept()
	while True:
		content = client.recv(32)
		print("The content is something ")
		print(content)
		content=content.decode('ASCII')
		match = re.search(r'---',content)
		if match:
			f=open("status.txt","a+")
			f.write(content)
			f.write("\n")
			f.close()
			subprocess.run(["/usr/bin/python3","start_of_week2.py"])
			subprocess.run(["rsync","-avzhe","ssh","data.json",ssh_location])
		if len(content) == 0:
			break
	print("Closing connection")
	client.close()
