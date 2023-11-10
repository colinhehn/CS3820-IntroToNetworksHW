# CS:3640 Assignment 3: Pings & Traceroutes

## Group Members
- Randy Zhang
- Lawrence Deng: https://research-git.uiowa.edu/lldeng/cs3640-a3
- Angelo Zamba: https://research-git.uiowa.edu/azamba/cs3640-a3
- Henry Krain: https://research-git.uiowa.edu/hkrain/cs3640-a3.git
- Colin Hehn

## Work Division
- Completed 3 methods for cs3640-ping.py -Randy 10/7/2023
- Created main program and edited 3 basic methods -Lawrence and Randy 10/8/2023
- Created traceroute program scaffolding + structured README -Colin Hehn 10/9/2023
- Wrote traceroute program logic (co-programming, just done on Colin's VM w/ screenshare) -Colin, Angelo, Henry, Lawrence 10/9/2023
- Debugged traceroute blockages, fine-tuning, MVP made! (same thing as above parenthesis) -Colin, Angelo, Henry, Lawrence 10/10/2023
- Went to Manisha's Office Hours to clarify any questions or concerns about the minor details - Angelo, Lawrence, Randy 10/11/2023
- Modified some smaller changes on the traceroute program to better resemble expected output - Angelo 10/11/23
- Small modifications to cs3640_ping.py for data (un)packing and outputs -Randy, Lawrence 10/12/2023


## Sources used for cs3640_ping.py file
### Sources used for make_icmp_socket method:
- Used this source as a starting point on how to format sockets: https://realpython.com/python-sockets/#background
- Used this source on what arguments I will need: https://docs.python.org/3/library/socket.html#creating-sockets
- This source helped me figure out which family and type I should use: https://www.qnx.com/developers/docs/6.5.0SP1.update/com.qnx.doc.neutrino_lib_ref/i/icmp_proto.html#:~:text=ICMP%20is%20the%20error%2D%20and,network%20monitoring%20and%20diagnostic%20functions.
- This source helped me confirm everything and figure out IPPROTO for ICMP: https://courses.cs.vt.edu/cs4254/fall04/slides/raw_1.pdf

- This source was used to find IP_TTL: https://www.ibm.com/docs/en/i/7.2?topic=ssw_ibm_i_72/apis/ssocko.htm
- This source was used to figure out how to set the time out: https://subscription.packtpub.com/book/cloud-and-networking/9781786463999/1/ch01lvl1sec08/setting-and-getting-the-default-socket-timeout#:~:text=You%20can%20make%20an%20instance,set%20a%20specific%20timeout%20value.

### Sources used for send_icmp_echo method:
- The following source was provided and used as a guideline to create our echo and icmp echo: https://jon.oberheide.org/blog/2008/08/25/dpkt-tutorial-1-icmp-echo/
- The following source was documentation for the dpkt.icmp: https://dpkt.readthedocs.io/en/latest/_modules/dpkt/icmp.html
- The following source was used to figure out how to send the icmp echo to an address: https://docs.python.org/3/library/socket.html#socket.socket.sendto

### Sources used for recv_icmp_response method:
- Used this source provided to get the response back:https://docs.python.org/3/library/socket.html#socket.socket.recvfrom
  - Set the buffer to 1028 because the source above said to set the buffer size to a power of 2 that is relatively small

### Sources used for main ping method:
- Used this to determine time out value because it wasn't given: https://stackoverflow.com/questions/31314328/connection-timeout-and-socket-timeout-advice
- Used this to install dpkt in virtual machine: https://stackoverflow.com/questions/21457250/error-while-using-dpkt-in-python
- Used this to figure out how to calculate round trip time: https://www.geeksforgeeks.org/program-calculate-round-trip-time-rtt/



## Sources used for cs3640_traceroute.py
- [Python Socket Documentation (specifically recvfrom function.)](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom)
- [GitHub Gist of someone with similar project, different spec.](https://gist.github.com/inaz2/78651ec593af1e0521be)
- [Medium article by someone making similar program, though with different packages.](https://abdesol.medium.com/lets-make-a-trace-routing-tool-from-scratch-with-python-f2f6f78c3c55)
- [Stack Overflow Article to help with VS Debugger](https://stackoverflow.com/questions/51244223/visual-studio-code-how-debug-python-script-with-arguments)


## Execution Instructions
### Ping (cs3640_ping.py)
1. Ensure you have a version of Python installed on your workstation.
2. Open a terminal and cd into directory containing the **cs3640_ping.py** file.
3. Run the following command:
    1. For Python 2 & below:
    
            sudo python cs3640_ping.py -destination [TARGET IP] -n [# OF PACKETS] -ttl [TIME TO LIVE]

    2. For Python 3:
    
            sudo python3 cs3640_ping.py -destination [TARGET IP] -n [# OF PACKETS] -ttl [TIME TO LIVE]

4. You should see output on your terminal!
    1. If something goes wrong, check the error message and your input. If it still blows up, let the entire class know about it at the next lecture.

### Traceroute (cs3640_traceroute.py)
1. Ensure you have a version of Python installed on your workstation.
2. Open a terminal and cd into directory containing the **cs3640_traceroute.py** file.
3. Run the following command:
    1. For Python 2 & below:

            sudo python cs3640_traceroute.py -destination [TARGET IP] -n_hops [MAX # OF HOPS]

    2. For Python 3:
    
            sudo python3 cs3640_traceroute.py -destination [TARGET IP] -n_hops [MAX # OF HOPS]

4. You should see output on your terminal!
    1. If something goes wrong, check the error message and your input. If it still blows up, let the entire class know about it at the next lecture.
