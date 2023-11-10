import dns.resolver, dns.exception, ssl, socket, json

# Returns the IPv4 address of the specified domain or an
# error message if the address could not be retrieved.
def IPV4_ADDR(domain):
    try:
        resolver = dns.resolver.Resolver()
        # Set the resolver's namerservers to Cloudfare DNS Server
        resolver.nameservers = ['1.1.1.1', '1.0.0.1']
        # Get the 'A' record for the domain, and return its first
        # element for the IPv4 address
        answers = dns.resolver.resolve(domain, 'A')
        return str(answers[0])
    # Handle the possible errors that may arise with the query
    # and return the error as a string:
    except dns.resolver.NXDOMAIN:
        return "Error: The domain does not exist."
    except dns.resolver.NoAnswer:
        return "Error: No IPv4 address was found for the domain."
    except dns.exception.Timeout:
        return "Error: The DNS query timed out."
    except Exception as error:
        return f"Error: {str(error)}"

# Returns the IPv6 address of the specified domain or an
# error message if the address could not be retrieved.
def IPV6_ADDR(domain):
    try:
        resolver = dns.resolver.Resolver()
        # Set the resolver's namerservers to Cloudfare DNS Server
        resolver.nameservers = ['1.1.1.1', '1.0.0.1']
        # Get the 'AAAA' record for the domain, and return its first
        # element for the IPv6 address
        answers = dns.resolver.resolve(domain, 'AAAA')
        return str(answers[0])
    # Handle the possible errors that may arise with the query
    # and return the error as a string:
    except dns.resolver.NXDOMAIN:
        return "Error: The domain does not exist."
    except dns.resolver.NoAnswer:
        return "Error: No IPv6 address was found for the domain."
    except dns.exception.Timeout:
        return "Error: The DNS query timed out."
    except Exception as error:
        return f"Error: {str(error)}"

# Returns the TLS/SSL certificate of the specified domain or an
# error message if the certificate could not be retrieved.
def TLS_CERT(domain):
    try:
        # Create a default context for the SSL
        context = ssl.create_default_context()
        # Create a TCP socket and wrap it with the SSL context
        sock = socket.create_connection((domain, 443))
        ssock = context.wrap_socket(sock, server_hostname=domain)
        certificate = ssock.getpeercert()
        if certificate is None:
            return "There is no certificate for the peer on the other end."
        else:
            return certificate
    # Handle the possible errors that may arise in retrieving the
    # certificate and return the error as a string:
    # ***NEED TO HANDLE SPECIFIC ERRORS FOR THIS COMMAND***
    except ssl.CertificateError:
        return "This certificate was not validated"
    except ssl.SSLEOFError:
        return "Error: This connection was abruptly closed"
    except socket.timeout:
        return "Error: The socket timed out"
    except Exception as error:
        return f"Error: {str(error)}"
    # we gotta handle errors

# returns the name of the AS that hosts the IP addy associated with the domain specified
def HOSTING_AS(domain):
    #resolver = dns.resolver.Resolver()
    #resolver.nameservers = ['1.1.1.1', '1.0.0.1'] # cloudfare dns server
    #ip_address = dns.resolver.resolve(domain, 'A')[0].to_text()
    
    # DOUBLE CHECK THAT THIS IS OK (Using IPV4-ADDR()).
    # Get IPv4 address of the domain using IPV4_ADDR().
    ipv4_address = IPV4_ADDR(domain)

    try:
        # Set up and perform a WHOIS query, storing the response
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.cymru.com", 43))
        s.sendall(f"-v {ipv4_address}\n".encode())
        response = s.recv(4096).decode("utf-8")
        if response is None:
            return "No response from query received."

        # Extract the AS info by splitting and stripping the response.
        response_lines = response.split('\n')
        as_info = response_lines[1].strip().split('|')
        
        # Make sure that as_info is valid and returnable to the user.
        if len(as_info) < 7:
            return 'No Autonomous System Found.'
        
        #Return the AS Number and Name from the 0th and 4th index, respectively
        return f"AS Number: {as_info[0].strip()}, AS Name: {as_info[6].strip()}"
    # ***NEED TO HANDLE SPECIFIC ERRORS FOR THIS COMMAND***
    except Exception as error:
        return f"Error: {str(error)}"

# returns the name of the org associated with the domain specified
def ORGANIZATION(domain):
    # socket = socket.create_connection((domain, 443))
    # ssl_socket = ssl.SSLSocket(socket) # not sure if necessary
    # peer_certificate = ssl_socket.getpeercert()

    # Grab the certificate using TLS_CERT()
    peer_certificate = TLS_CERT(domain)
    
    # Make sure the TLS Certificate was validated.
    if not isinstance(peer_certificate, dict):
        return 'No TLS Certificate was found to check for Organization Name.'
    
    # Extract and return the organization name.
    # First search 'subject' of TLS Certificate for Org Name.
    response_subject = peer_certificate['subject']
    for subject in response_subject:
        for attribute in subject:
            if attribute[0] == 'organizationName':
                return attribute[1]
            
    # If no Org Name in 'subject', check 'issuer' in TLS Certificate.
    response_issuer = peer_certificate['issuer']
    for issuer in response_issuer:
        for attribute in issuer:
            if attribute[0] == 'organizationName':
                return attribute[1]
            
    # If STILL no Org Name found, let the client know.
    return 'No Organization Name Found in SUBJECT or ISSUER.'

def process_client_message(client_message):
    parsed_message = json.loads(client_message)
    # Make sure deserialized json gives us the tuple of [domain, CLIENT COMMAND]
    if not isinstance(parsed_message, list):
        return ValueError('Received message not of type: List.')
    
    # Extract values from message, call respective functions and return.
    domain = parsed_message[0]
    client_command = parsed_message[1]
    
    match client_command:
        case 'IPV4_ADDR':
            return IPV4_ADDR(domain)
        case 'IPV6_ADDR':
            return IPV6_ADDR(domain)
        case 'TLS_CERT':
            return TLS_CERT(domain)
        case 'HOSTING_AS':
            return HOSTING_AS(domain)
        case 'ORGANIZATION':
            return ORGANIZATION(domain)
        
    # If we made it here, the CLIENT COMMAND is invalid.
    return RuntimeError('CLIENT COMMAND did not match specified options.')

def server_startup():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET is IPv4, SOCK_STREAM is TCP
    host_ip = '127.0.0.1'
    port = 5555
    server_socket.bind((host_ip, port))
    
    # Start listening for client messages!
    server_socket.listen(1)
    while True:
        connection, client_address = server_socket.accept()
        try:
            # Connection detected!
            print('Connection from: %s' % ((str)(client_address)))
            
            # Receive message data from client, send to processing function.
            while True:
                client_message = connection.recv(2048)
                if client_message:
                    print('Message from Intel Client: %s' % ((str)(client_message)))
                    response = process_client_message(client_message)
                    
                    # Send response to intel client
                    print('Message sending to Intel Client: %s' % (str)(response))
                    send_to_client = json.dumps(response)
                    connection.sendall(bytes(send_to_client, 'utf-8'))
                else:
                    break
        finally:
            connection.close()

# Server will not exit/shutdown unless Ctrl+C or Cmd+C is issued on host machine (I think.)
if __name__ == '__main__':
    server_startup()