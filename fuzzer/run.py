from server import WebSocketServer

if __name__ == '__main__':
    ws = WebSocketServer()
    ws.start_server(8787)
