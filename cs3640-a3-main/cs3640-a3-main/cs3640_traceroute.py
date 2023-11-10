from cs3640_ping import make_icmp_socket, send_icmp_echo
import time
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-destination", type=str, required=True)
    parser.add_argument("-n_hops", type=int, required=True)
    args = parser.parse_args()
    
    # Initial config vars
    timeout = 3
    ttl = 1
    output_string = ''
    
    # TRACEROUTE LOGIC
    #   1. send out a packet with TTL = 1.
    #   2. receive ICMP error packet of type TTL EXCEEDED from first hop.
    #   3. increment TTL by 1. repeat above process, preparing to receive error packet from hop 2.
    #   4. repeat process until destination is reached (packet we get back will be different), or TTL > n_hops.
    #   
    #   Need to print out the latency data from each hop as specified in assignment desc.

    while ttl <= args.n_hops:
        # - create socket with current ttl, document current time, send an echo
        socket = make_icmp_socket(ttl, timeout)
        t1 = time.time()
        icmp = send_icmp_echo(socket, 'test payload', 0, 0, args.destination)
        
        # - receive one back hopefully -> Didn't use the method from ping because it broke the program.
        # - Discussed this with Manisha and she said it was ok!
        data, address = socket.recvfrom(512)
        
        t2 = time.time()
        rtt = round((t2-t1)*1000, 2)
        
        # if we've made it this far, we are at a hop and need to keep going.
        # - add the response info (hop IP, rtt) to a big string to be printed at end.
        output_string += 'destination = %s; hop %s = %s; rtt = %s ms\n'%(args.destination, ttl, str(address[0]), rtt)
        # check current ip address with destination address :D way easier and works!
        if str(address[0]) == str(args.destination):
            break
        # - increment our TTL value.
        ttl += 1
    
    # Final cleanup!
    socket.close()
    print(output_string)

if __name__ == "__main__":
    main()