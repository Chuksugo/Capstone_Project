Install the Token App: Make sure rest_framework and rest_framework.authtoken are included in the INSTALLED_APPS section of settings.py.

Migrate the Database: Run the migration command to create necessary database tables for the token authentication.

Configure URLs: Add the token authentication endpoint in your app's urls.py to make it accessible at /api/token/.

Test the Endpoint: Use Postman or a similar tool to send a POST request to /api/token/, including the username and password in the JSON body. Ensure the request header is set to Content-Type: application/json.

Receive Tokens: If successful, the response should include access and refresh tokens, which can be used for authenticating subsequent API requests.