# CS:3640 Assignment 4: Building a Network Intelligence Service

## Group Members
- Randy Zhang
- Lawrence Deng
- Angelo Zamba
- Henry Krain
- Colin Hehn

## Timeline
- **(11/5/23):** Wrote bulk of intelserver. - Angelo, Randy, Lawrence, Henry
- **(11/7/23):** Wrote bulk of intelclient, created README structure. - Colin
- **(11/7/23):** Added documentation, code cleanup, and some error handling to intelserver. - Lawrence
- **(11/8/23):** Refined intelclient, wrote intelserver client listening + message processing logic, general debugging - Colin
- **(11/9/23):** Fixed dns import bug and added onto error
handling. -Lawrence
- **(11/9/23):** Debugged and refactored all client commands, fixed server/client buffer size error - Randy, Lawrence, Angelo, Henry, Colin

## Sources used for Intel Client + Server Interfacing
- [Client / Server Echo Example](https://pymotw.com/2/socket/tcp.html)
- [Client / Server Echo Example Two](https://realpython.com/python-sockets/#echo-server)
- [Serializing message data to JSON](https://stackoverflow.com/questions/7245827/python-string-to-list)

## Sources used for Intel Server Logic
- [DNS Python Resolver Class](https://dnspython.readthedocs.io/en/stable/resolver-class.html)
- [link title](actual link)

<br>

## Execution Instructions
### Intel Server Setup
1. Ensure you have a version of Python installed on your workstation.
2. Open a terminal and cd into directory containing the **cs3640_intelserver.py** file.
3. Run the following command:
    
        sudo python cs3640_intelserver.py
    - If running Python 3 or higher, replace "python" with "python3" in the above command.

4. The terminal should hover on the next line with no output. The server is running!
    1. As client-side commands are ran, you should see information printed on the terminal.
5. To stop the server, press Ctrl+C or Cmd+C on your keyboard while tabbed in the terminal window.

### Intel Client
1. Ensure you have a version of Python installed on your workstation.
2. Open a terminal and cd into directory containing the **cs3640_intelclient.py** file.
3. Run the following command:
    
        sudo python cs3640_intelclient.py [INTEL_SERVER_ADDR] [INTEL_SERVER_PORT] [DOMAIN] [SERVICE TO EXECUTE]
    - If running Python 3 or higher, replace "python" with "python3" in the above command.

4. You should see output on your terminal!
    1. If something goes wrong, check the error message and your input. If it still blows up, let the entire class know about it at the next lecture.
