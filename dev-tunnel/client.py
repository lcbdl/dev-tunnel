def receive_requests():
    # Listen for incoming requests from Server application
    while True:
        request_data = receive_request()
        # Forward request to local web server
        response = forward_request_to_local_server(request_data)
        # Send response back to Server application
        send_response_to_server(response)

def forward_request_to_local_server(request_data):
    # Construct request object based on request_data
    response = requests.request(**request_data)
    return response