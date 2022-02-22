from websocket_server import WebsocketServer
import json
import random

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	#server.send_message_to_all("Hey all, a new client has joined us")
	#send a JSON message
	temperature = random.uniform(1, 5)
	msg_return = json.dumps({"id":"sensordata","temp":random.uniform(1, 5),"light":random.uniform(1, 5),"test":random.uniform(1, 5)}, separators=(',', ':'))
	server.send_message_to_all(msg_return)

# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	#json formatted message
	msg_parsed = json.loads(message)
	print(type(msg_parsed))
	print(msg_parsed["Command"])


	#send the sensordata each time a command is received
	msg_return = json.dumps({"id":"sensordata","temp":random.uniform(1, 5),"light":random.uniform(1, 5),"test":random.uniform(1, 5)}, separators=(',', ':'))
	#msg_return = 'temp:2;l:-5;j:18'
	server.send_message_to_all(msg_return)
	
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))



PORT=9001
server = WebsocketServer(port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()