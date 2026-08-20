# 🔐 HTTP Basic Authentication Lab

> A hands-on lab to understand HTTP Basic Authentication, Base64 encoding, and the security implications of transmitting credentials over HTTP.

---

## 🎯 Learning Objectives

By the end of this lab, you will:

- Understand the **HTTP Basic Authentication** workflow
- Interpret `401 Unauthorized` and `WWW-Authenticate` headers
- Work with the `Authorization` header and the `Basic` scheme
- Encode and decode credentials using **Base64**
- Recognise that **Base64 is not encryption**
- Compare **authentication vs. authorisation**
- Understand the **security risks** of using Basic Auth over plain HTTP
- Use **`curl`**, **Python**, and optionally **Burp Suite** to inspect the traffic

---

## 🛠️ Lab Requirements

- Linux / Kali Linux
- Python 3
- `curl`
- Burp Suite (optional)
- Web browser (optional)

> **No external Python packages are required** – the server uses only the standard library.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jd985854/basic-http-auth-lab
cd basic-auth-lab

2️⃣ Start the Server

```bash
python3 server.py

You should see:

[+] HTTP Basic Auth Lab running at http://127.0.0.1:8080
[+] Protected endpoint: http://127.0.0.1:8080/admin
[+] Username: john
[+] Password: 123456

3️⃣ Alternative: Run Script

```bash
chmod +x run.sh
./run.sh

🌐 Access the Protected Endpoint

Open in your browser:
text

http://127.0.0.1:8080/admin

The /admin route is protected with HTTP Basic Authentication.
🧪 Practical Tests
✅ Without Credentials

```bash
curl -i http://127.0.0.1:8080/admin

Expected response:


HTTP/1.0 401 Unauthorized
WWW-Authenticate: Basic realm="Admin"

This is the authentication challenge.
✅ With Credentials
```bash

curl -i -u john:123456 http://127.0.0.1:8080/admin

Expected response:


HTTP/1.0 200 OK
Content-Type: text/html
...

The protected page is returned.
✅ Manually Construct the Authorization Header

Instead of -u, send the header directly:
```bash
curl -i -H "Authorization: Basic am9objoxMjM0NTY=" http://127.0.0.1:8080/admin

The Base64 value am9objoxMjM0NTY= decodes to john:123456.
🔄 Authentication Flow
🔐 Understanding Base64

HTTP Basic Auth encodes credentials using Base64 – it does not encrypt them.
bash

echo -n 'john:123456' | base64

Output:

am9objoxMjM0NTY=

Decode it:
```bash
echo 'am9objoxMjM0NTY=' | base64 -d

Output:

john:123456

    ⚠️ Base64 is reversible – it provides no secrecy. Always use HTTPS to protect the credentials in transit.

🧠 Key Concepts
Concept	Description
HTTP Basic Auth 	Authenticates the user via Authorization: Basic <base64>
401 Unauthorized	Server asks for credentials
WWW-Authenticate	Tells the client which authentication scheme to use
realm	                Identifies the protected area
Base64	                Encoding (not encryption) for credentials
Authentication       	"Who is the user?"
Authorisation	       "What can the user do?"

🔬 Burp Suite Analysis

    Configure your browser to use Burp as a proxy.

    Access http://127.0.0.1:8080/admin.

    Observe the initial 401 response and the subsequent request with the Authorization header.

Example request:

GET /admin HTTP/1.1
Host: 127.0.0.1:8080
Authorization: Basic am9objoxMjM0NTY=

Decode the Base64 part in Burp’s Inspector or manually.

⚠️ Security Implications

    HTTP + Basic Auth = credentials are sent in plaintext (Base64 only, easily decoded)

    HTTPS + Basic Auth = credentials are encrypted by TLS while in transit

📚 What I Learned

    HTTP request/response analysis

    401 Unauthorized and WWW-Authenticate

    Authorization header and Basic scheme

    Base64 encoding/decoding

    Credential verification

    Using curl, Burp Suite

    The difference between authentication and authorisation

    Security risks of Basic Auth over plain HTTP

    The role of HTTPS/TLS in protecting credentials

🚀 Future Improvements

    Add HTTPS/TLS support

    Compare HTTP vs HTTPS traffic

    Support multiple users with password hashing

    Add authentication logging

    Provide a Docker environment

    Integrate automated tests

    Capture traffic with Wireshark for deeper analysis

⚠️ Disclaimer

This project is strictly for educational and authorised security testing purposes.
The server runs locally on 127.0.0.1 with dummy credentials:

    Username: john

    Password: 123456

Do not use these techniques against systems without explicit permission.
👨‍💻 Author

John Daniel
Cybersecurity Student | eJPT Certified | VAPT & Penetration Testing Enthusiast
