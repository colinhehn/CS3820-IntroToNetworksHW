import time
import socket
import dpkt
import argparse
# Named cs3640_ping.py instead of cs3640-ping.py to make importing into cs3640_traceroute.py easier (Discussed with Manisha)

def make_icmp_socket(ttl: int, timeout: int) -> socket:
    
    # create a new raw socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    # Setting created socket to have a time to live of ttl
    s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)

    # setting the time out value to be timeout
    s.settimeout(timeout)

    #Return the socket
    return s

def send_icmp_echo(socket: socket, payload, id, seq, destination):

    # creating an echo
    echo = dpkt.icmp.ICMP.Echo()
    echo.id = id
    echo.seq = seq

    # Changed the data to bytes before we sent it due to errors we were getting
    echo.data = payload.encode('utf-8')

    # Creating an ICMP
    icmp = dpkt.icmp.ICMP()
    icmp.type = dpkt.icmp.ICMP_ECHO

    # setting the ICMP data as echo
    icmp.data = echo
    packedICMP = icmp.pack()

    # Made a tuple for the destination value from the input string
    destination_tuple = (destination, 0)
    #Use the socket.sendto() method for sending the packed ICMP
    socket.sendto(packedICMP, destination_tuple)

    #Return the ICMP (discussed with Manisha and she said it was fine)
    return icmp

def recv_icmp_response():
    #Create a new socket for receiving the ICMP response
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    
    #Use the socket.recvfrom() method with a buffer 1028 to receive the packet, and store its data and address.
    data, address = s.recvfrom(1028)

    #Unpack and store the data from the packet
    unpackedData = dpkt.icmp.ICMP(data)

    #Close the socket
    s.close()

    #Return the unpacked data and the address
    return unpackedData, address

def main():

    # Parser to get the arguments provided in the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-destination", type=str, required=True)
    parser.add_argument("-n", type=int, required=True)
    parser.add_argument("-ttl", type=int, required=True)
    args = parser.parse_args()

    # creating an icmp socket with the arguments and a timeout value of 3 seconds. 
    # We chose 3 seconds based off this article: https://stackoverflow.com/questions/31314328/connection-timeout-and-socket-timeout-advice (discussed with Manisha)
    s = make_icmp_socket(args.ttl, 3)
    
    # Initalizing variables to keep track of successful pings, total pings, and total time taken
    successfulPings = 0
    totalPings = args.n
    totalTime = 0

    #for every packet from 0 to n-1, as specified by the command line argument:
    for i in range(totalPings):
        #Record the current time in t1 before sending an ICMP echo, storing the ICMP that is created.
        #We set the payload to an arbitrary string 'test payload' (Discussed with Manisha)
        t1 = time.time()
        icmp = send_icmp_echo(s, 'test payload', i, i, args.destination)
        
        #Call recv_icmp_response() to get the echo back, and store the returned values in data and address.
        data, address = recv_icmp_response()
        #Record the time right after we have received a responsein t2, and calculate the roundtrip time using t1 and t2. Multiply by 1000 for milliseconds
        #and round to 2 decimal places
        t2 = time.time()
        rtt = round((t2 - t1) * 1000, 2)

        #If the address of the packet we get back is our original destination address, the ping was successful, so increment the count of successful pings.
        if address[0] == args.destination:
            successfulPings +=1

        #Add the roundtrip time of the current packet the total time for all packets (used for calculating the average rtt)
        totalTime += rtt
        #Print out the destination, seq, id, ttl, and rtt of the packet.
        print("destination = %s; icmp_seq = %s; icmp_id = %s; ttl = %s; rtt = %s ms" %(args.destination, icmp.data.seq, icmp.data.id, args.ttl, rtt))
    
    #Calculated the average time using the totalTime and totalPings and round to 2 decima places.
    avgTime = round(totalTime / totalPings, 2)
    
    #Print out the average rtt and the number of successful pings out of the total number of pings.
    print("Average rtt: %s ms; %s/%s successful pings." %(avgTime, successfulPings, totalPings))

if __name__ == "__main__":
    main()
