# pyWebcamSteg
*An annoymising proxy through your webcam*
---
![Information flow in system](/informationFlow.png)
## How it works
The system works by encoding and encrypting your request in your webcam feed (this can be a pre-recorded video sequence to preserve your anonymity). This is then sent to a proxy server, before being encoded inside the proxy server's webcam streams which your client will then access before decoding and displaying the webpage.

## Dependancies
- outguess 
- openCV (if using live webcam capturing) 

## Running
Simply start the server.py file on your proxy server:

    python server.py

You can then navigate to the server on port 80 to see the fake webcam site generated.

On the client side, when you want to browse the web using the proxy, run:

    python client.py

Then set a mannual proxy in your browser at localhost on the port specified (4125 by default)
