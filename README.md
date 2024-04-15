# p2p

This is a simple chatroom system implemented using Python's socket module.

## Server

The server script (`server.py`) sets up a server that listens for incoming connections on port 8000. It handles each client connection in a separate thread and broadcasts messages from one client to all other connected clients.

To start the server, run the following command:

python server.py

## Client

The client script (`client.py`) connects to the server on localhost port 8000. It allows users to send messages to the server and receive messages from other connected clients.

To start a client, run the following command:

python client.py


## Usage

1. Start the server by running `python server.py`.
2. Start one or more clients by running `python client.py`.
3. Enter your username when prompted.
4. Start chatting!

## Dependencies

- Python 3.x
- No additional dependencies required.
