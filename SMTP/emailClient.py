import base64
from socket import *
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
# mailserver = ("smtp.gmail.com", 587)  # Fill in start # Fill in end
mailServ = "smtp.comcast.net"
portNumber = 587
mailserver = (mailServ, portNumber)

sender = "sender@comcast.net"
recipient = "receiver@yahoo.com"

# Username and Password for Mail server authentication
username = "account@comcast.net"
password = "password"

# Create socket called clientSocket and establish a TCP Connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end

recv = clientSocket.recv(1024).decode()
print("CONNECT:\t" + recv)
if recv[:3] != '220':
    print('CONNECT:\t220 reply not received from server.')

# Enable TLS for the socket.
clientSocket.send("STARTTLS\r\n".encode())
recv = clientSocket.recv(1024).decode()
print(recv)

securedSocket = ssl.wrap_socket(clientSocket)

# Send HELO command and print server response.
securedSocket.write("HELO Comcast\r\n".encode())
recv = securedSocket.read(1024).decode()
print("HELO:\t" + recv)

base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
securedSocket.write(authMsg)
recv = securedSocket.read(1024).decode()
print(recv)
if recv[:3] != '235':
    print('235 reply not received from server')


# Send MAIL FROM command and print server response
# Fill in start
mailFromCommand = "MAIL FROM: <" + sender + ">\r\n"
securedSocket.write(mailFromCommand.encode())
recv = securedSocket.read(1024).decode()
print('MAIL FROM:\t' + recv)
if recv[:3] != '250':
    print('MAIL FROM:\t250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response
# Fill in start
rcptTo = "RCPT TO: <" + sender + ">\r\n"
securedSocket.write(rcptTo.encode())
recv = securedSocket.read(1024).decode()
print('RCPT TO:\t' + recv)
if recv[:3] != '250':
    print('RCPT TO:\t250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
# clientSocket.send(data.encode())
securedSocket.write("DATA\r\n".encode())
recv = securedSocket.read(1024).decode()
print('DATA:\t' + recv)
if recv[:3] != '354':
    print('DATA:\t354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
securedSocket.write(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
securedSocket.write(endmsg.encode())
recv = securedSocket.read(1024).decode()
print('MSG:\t' + recv)
if recv[:3] != '250':
    print('MSG:\t250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit = "QUIT \r\n"
securedSocket.write(quit.encode())
recv = securedSocket.read(1024).decode()
print("QUIT:\t" + recv)
if recv[:3] != '221':
    print('QUIT:\t221 reply not received from server.')
# # Fill in end
