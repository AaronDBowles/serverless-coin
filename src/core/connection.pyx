
from jsonrpclib import ServerProxy

cdef run_command(node_url: str, cmd: str, params: {} ,is_secure: bool = False):
    connection = ServerProxy(f'{"https" if is_secure else "http"}://{node_url}')
    connection._request_notify(cmd,params)
