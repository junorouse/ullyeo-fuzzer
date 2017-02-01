from server import WebSocketServer

"""
TODO: Make handle function.
"""

if __name__ == '__main__':
    ws = WebSocketServer()
    ws.start_server(8787)
