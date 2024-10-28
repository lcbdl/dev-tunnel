# Requirements

- This includes a Client and a Server application.  
- The Client application runs on a local server, and the Server application runs on a public server.   
- The client application creates a secure tunnel with the server application.   
- The server application can accept http or https web requests that are sent from a browser.  
- Then the Server application forwards all the requests to the Client application through the secure tunnel.
- The Client application forward the received request to a local web server, for example a String-boot web application.
- The Client application received the response from the local web server, then forward it to the Server application through the secure tunnel. 
- The server received the response from the Client, then forward it back to the browser.


# How to run application in debug mode
```
python dev-tunnel/server.py --debug
```