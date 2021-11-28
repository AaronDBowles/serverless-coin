import jsonrpclib

def run_command(node, cmd, params ,is_secure = False):
    connection = jsonrpclib.Server(f'{"https" if is_secure else "http"}://{node}')
    return connection._request(cmd,params)
