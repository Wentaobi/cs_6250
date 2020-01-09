from Message import *

        	          
class Switch(object):

    def __init__(self, idNum, topolink, neighbors):
		self.switchID = idNum
		self.topology = topolink
		self.links = neighbors
		self.connections = {}
		self.root = idNum
		self.distance = 0

        #TODO: Define a data structure to keep track of which links are part of / not part of the spanning tree.
    def verify_neighbors(self):
        ''' Verify that all your neighbors has a backlink to you. '''
        for neighbor in self.links:
            if self.switchID not in self.topology.switches[neighbor].links:
                raise Exception(neighbor + " does not have link to " + self.switchID)

    def send_initial_messages(self):
		for neighbor in self.links:
			initial_message=Message(self.switchID, self.distance, self.switchID, neighbor)
			self.topology.send_message(initial_message)
        #TODO: This function needs to create and send the initial messages from this switch.

    def process_message(self, message):

		if message.root < self.root:
			self.root = message.root
			self.distance == message.distance+1
			if len(str(message.destination)) ==1:
				checkKey1 = str(message.origin)+"$"+"0"+str(message.destination)
			else:
				checkKey1 = str(message.origin)+"$"+str(message.destination)
			if len(str(message.origin)) == 1:
				checkKey2 = str(message.destination)+"$"+"0"+str(message.origin)
			else:
				checkKey2 = str(message.destination)+"$"+str(message.origin)
			if checkKey1 not in self.connections:
				self.connections[checkKey1] = 1
			if checkKey2 not in self.connections:
				self.connections[checkKey2] = 1
			for neighbor in self.links:
				message2 = Message(self.root, self.distance, self.switchID, neighbor)
				self.topology.send_message(message2)
		if message.root == self.root:
			if message.distance < self.distance:
				self.root = message.root
				self.distance == message.distance+1
				if len(str(message.destination)) ==1:
					checkKey1 = str(message.origin)+"$"+"0"+str(message.destination)
				else:
					checkKey1 = str(message.origin)+"$"+str(message.destination)
				if len(str(message.origin)) == 1:
					checkKey2 = str(message.destination)+"$"+"0"+str(message.origin)
				else:
					checkKey2 = str(message.destination)+"$"+str(message.origin)
				if checkKey1 not in self.connections:
					self.connections[checkKey1] = 1
				if checkKey2 not in self.connections:
					self.connections[checkKey2] = 1
				for neighbor in self.links:
					message2 = Message(self.root, self.distance, self.switchID, neighbor)
					self.topology.send_message(message2)
