import grpc

cdef run_command(node_url: str, cmd: str, params: {}):
    with grpc.insecure_channel(node_url) as connection:
        uu = connection.unary_unary(cmd)
        return uu.__call__(params)
