from QChat.server import QChatServer
import time

# Sleep for 10 seconds to allow Bob to spin up first
time.sleep(10)

# Instantiate the server and sleep for 2 seconds to allow initialization
s = QChatServer("Alice")
time.sleep(2)

# Send a message to Bob
s.sendQChatMessage("Bob", "Hello!")
