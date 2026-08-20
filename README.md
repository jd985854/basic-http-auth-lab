🎯 Learning Objectives

By completing this lab, I aim to understand the practical workflow of HTTP Basic Authentication and how authentication data is transmitted between a client and server.

Core Concepts
Understand HTTP Basic Authentication
Understand 401 Unauthorized
Understand WWW-Authenticate
Understand the realm parameter
Understand the Authorization header
Understand the Basic authentication scheme
Understand Base64 encoding and decoding
Understand why Base64 is not encryption
Understand credential verification
Understand authentication vs authorization
Understand the security risks of Basic Authentication over plain HTTP
Practical Skills
Create a local HTTP authentication server using Python
Send HTTP requests using curl
Manually construct an Authorization header
Encode and decode credentials using Base64
Analyze HTTP requests and responses
Use Burp Suite to inspect HTTP authentication
Understand how credentials are transmitted over HTTP
🛠️ Lab Requirements
Linux / Kali Linux
Python 3
curl
Burp Suite (optional)
A web browser (optional)

No external Python packages are required.


🚀 How to Run the Lab
1️⃣ Clone the Repository
git clone <YOUR-REPOSITORY-URL>
cd basic-auth-lab
2️⃣ Start the Server

Run the Python server:

python3 server.py

You should see:

[+] HTTP Basic Auth Lab running at http://127.0.0.1:8080
[+] Protected endpoint: http://127.0.0.1:8080/admin
[+] Username: john
[+] Password: 123456
3️⃣ Alternative: Use the Run Script

Make the script executable:

chmod +x run.sh

Start the lab:

./run.sh
🌐 Access the Protected Endpoint

Open:

http://127.0.0.1:8080/admin

The /admin endpoint is protected using HTTP Basic Authentication.

🧪 Practical Testing
1️⃣ Test Without Credentials

Run:

curl -i http://127.0.0.1:8080/admin

Expected response:

HTTP/1.0 401 Unauthorized
WWW-Authenticate: Basic realm="Admin"

This demonstrates the authentication challenge.

2️⃣ Test With Credentials

Run:

curl -i -u john:123456 http://127.0.0.1:8080/admin

Expected response:

HTTP/1.0 200 OK
Content-Type: text/html

The server should return the protected admin page.

🔄 HTTP Basic Authentication Flow
1️⃣ Client Requests Protected Resource
GET /admin HTTP/1.1
Host: 127.0.0.1:8080

The client requests /admin without credentials.

⬇️

2️⃣ Server Requests Authentication
HTTP/1.0 401 Unauthorized
WWW-Authenticate: Basic realm="Admin"

The server responds with:

401 Unauthorized

This means authentication is required.

WWW-Authenticate: Basic tells the client that the server expects HTTP Basic Authentication.

realm="Admin" identifies the protected authentication area.

⬇️

3️⃣ Client Sends Credentials
GET /admin HTTP/1.1
Host: 127.0.0.1:8080
Authorization: Basic am9objoxMjM0NTY=

The Base64 value represents:

john:123456

⬇️

4️⃣ Server Verifies Credentials
Authorization Header
        ↓
Basic <Base64>
        ↓
Base64 Decode
        ↓
john:123456
        ↓
Extract Username + Password
        ↓
Verify Credentials

⬇️

5️⃣ Authentication Result

If the credentials are correct:

HTTP/1.0 200 OK
Content-Type: text/html

The server provides the protected /admin page.

If the credentials are incorrect:

HTTP/1.0 401 Unauthorized
🔁 Complete Authentication Flow
Client
   |
   | GET /admin
   |---------------------------->
   |
   | 401 Unauthorized
   | WWW-Authenticate: Basic
   |<----------------------------
   |
   | Authorization: Basic <Base64>
   |---------------------------->
   |
   |          Server
   |             |
   |       Base64 Decode
   |             ↓
   |       john:123456
   |             ↓
   |      Verify Credentials
   |             |
   |       ┌─────┴─────┐
   |       ↓           ↓
   |    Correct      Wrong
   |       ↓           ↓
   |    200 OK        401
   |
🔐 Understanding Base64

HTTP Basic Authentication uses Base64 encoding.

For example:

john:123456

Encode it:

echo -n 'john:123456' | base64

Output:

am9objoxMjM0NTY=

This value is then used in:

Authorization: Basic am9objoxMjM0NTY=
🔓 Decode the Base64 Value

Base64 is reversible and can easily be decoded.

Run:

echo 'am9objoxMjM0NTY=' | base64 -d

Output:

john:123456

Therefore:

Base64 is encoding, NOT encryption.

🧪 Manually Send the Authorization Header

Instead of using:

curl -u john:123456 http://127.0.0.1:8080/admin

we can manually send the Authorization header:

curl -i \
-H "Authorization: Basic am9objoxMjM0NTY=" \
http://127.0.0.1:8080/admin

Expected response:

HTTP/1.0 200 OK
Content-Type: text/html

This demonstrates how the browser/client sends the Base64-encoded credentials inside the Authorization header.

🔬 Burp Suite Analysis

Burp Suite can be used to observe the HTTP authentication flow.

Configure the browser to use Burp Suite as a proxy.

Then access:

http://127.0.0.1:8080/admin

The first request should look similar to:

GET /admin HTTP/1.1
Host: 127.0.0.1:8080

The server responds:

HTTP/1.0 401 Unauthorized
WWW-Authenticate: Basic realm="Admin"

After authentication, observe:

GET /admin HTTP/1.1
Host: 127.0.0.1:8080
Authorization: Basic am9objoxMjM0NTY=

The important part is:

Authorization: Basic am9objoxMjM0NTY=

Decode the Base64 value:

am9objoxMjM0NTY=
        ↓
john:123456

This demonstrates how HTTP Basic Authentication works at the request/response level.

⚠️ Security Implications

HTTP Basic Authentication does not encrypt the username and password itself.

The credentials are only Base64 encoded.

Username + Password
        ↓
Base64 Encoding
        ↓
Authorization Header

Base64 can easily be decoded.

Therefore, using Basic Authentication over plain HTTP can expose credentials to an attacker who is able to observe the network traffic.

🔐 HTTP vs HTTPS
HTTP Basic Authentication
Username + Password
        ↓
Base64 Encoding
        ↓
Authorization Header
        ↓
Server Verification

Basic Authentication itself provides no encryption.

HTTPS / TLS

When Basic Authentication is used over HTTPS:

Username + Password
        ↓
Base64 Encoding
        ↓
Authorization Header
        ↓
TLS Encryption
        ↓
Protected Transmission
        ↓
Server Verification

HTTPS/TLS protects the HTTP communication while it travels between the client and server.

🧠 Key Takeaways
HTTP Basic Authentication
Authenticates the user
Uses the Authorization header
Uses Base64 encoding
Base64 is not encryption
Server verifies the supplied credentials
401 Unauthorized indicates authentication is required or failed
200 OK can indicate successful authentication and authorization to the requested resource
HTTPS/TLS
Primarily authenticates the server
Uses a server certificate
Provides encryption for data in transit
Provides integrity protection
Protects HTTP communication while traveling across the network
Important Difference
HTTP Basic Authentication
        ↓
"Who is the user?"


HTTPS / TLS
        ↓
"Am I communicating with the genuine server?"
        +
"Can I protect the communication?"
📸 Screenshots

The screenshots/ directory can contain evidence from the practical lab.

Recommended screenshots:

01-401-challenge.png

Showing the 401 Unauthorized response.

02-basic-auth-200.png

Showing successful authentication and 200 OK.

03-base64-decode.png

Showing Base64 encoding and decoding.

04-burp-request.png

Showing the Authorization header in Burp Suite.

⚠️ Disclaimer

This project is created strictly for educational and authorized security testing purposes.

The server is designed to run locally using:

127.0.0.1

The credentials used in this lab are dummy credentials:

Username: john
Password: 123456

Do not use this technique against systems, accounts, or networks without proper authorization.

📚 What I Learned

Through this lab, I learned how HTTP Basic Authentication works from the protocol level instead of only using a browser login form.

I practiced:

HTTP request/response analysis
401 Unauthorized
WWW-Authenticate
Authorization
Basic Authentication
Base64 encoding and decoding
Credential verification
curl
Burp Suite
HTTP security
HTTPS/TLS security concepts

This lab helped me connect HTTP, authentication, Base64, encryption, TLS, and web security into one practical workflow.

🚀 Future Improvements

Possible improvements for this lab:

Add HTTPS/TLS support
Compare HTTP and HTTPS traffic
Add multiple users
Add password hashing
Add authentication logging
Add a Docker environment
Add automated tests
Analyze the traffic using Wireshark
Perform controlled security testing against the lab
⭐ Author

John Daniel

Cybersecurity Student | eJPT Certified | VAPT & Penetration Testing Enthusiast
