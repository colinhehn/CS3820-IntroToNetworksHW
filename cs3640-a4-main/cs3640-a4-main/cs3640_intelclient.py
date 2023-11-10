import argparse, socket, json

def run_client():
    # ArgumentParser configuration
    ap = argparse.ArgumentParser()
    ap.add_argument('intel_server_addr')
    ap.add_argument('intel_server_port')
    ap.add_argument('domain')
    ap.add_argument('service')
    
    args = ap.parse_args()
    
    # Ensure that the given arguments are valid.
    valid_services = ['IPV4_ADDR', 'IPV6_ADDR', 'TLS_CERT', 'HOSTING_AS', 'ORGANIZATION']
    if not isinstance(args.service, str):
        raise ValueError('Service value was of invalid type. Please ensure it is a string.')
    if not isinstance(args.domain, str):
        raise ValueError('Domain value was of invalid type. Please ensure it is a string.')
    if args.service not in valid_services:
        raise ValueError('Service value must be one of: %s' % (str)(valid_services))
    
    # AF_INET is IPv4, SOCK_STREAM is TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to intel server with user given address and port
        s.connect((args.intel_server_addr, (int)(args.intel_server_port)))
        
        try:
            # Send message containing DOMAIN and CLIENT COMMAND to server. Up to them to parse.
            message_to_send = json.dumps([args.domain, args.service])
            print('Message sending to server: %s' % message_to_send)
            s.sendall(bytes(message_to_send, 'utf-8'))
            
            # Read response from the intel server
            server_response = s.recv(8192)
            if server_response:
                response_output = json.loads(server_response)
                print('Server Response: %s' % response_output)
            else:
                print('Server response was None (NULL).')
        finally:
            s.close()
    return

if __name__ == "__main__":
    run_client()