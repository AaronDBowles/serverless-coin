import threading

chain = [] # TODO - add pulling chain from local storage and syncing with server

def start_node():
    sync()

def sync():
    threading.Timer(10.0, sync).start()
    validate_chain()

def validate_chain():
    # TODO - grab chain from network and create/validate our copy
    print('chain is valid!')
    return True

