## 🔄 HTTP Basic Authentication Flow

The lab demonstrates the complete HTTP Basic Authentication workflow.

### 1️⃣ Client Requests Protected Resource

```http
GET /admin HTTP/1.1
Host: 127.0.0.1:8080# 🔐 HTTP Basic Authentication Lab

A hands-on cybersecurity lab demonstrating how **HTTP Basic Authentication** works at the HTTP protocol level.

This lab simulates a protected `/admin` endpoint and demonstrates the complete authentication flow:

```text
Client
   ↓
GET /admin
   ↓
401 Unauthorized
   ↓
WWW-Authenticate: Basic
   ↓
Authorization: Basic <Base64>
   ↓
Base64 decoding
   ↓
Username + Password verification
   ↓
┌───────────────┐
│               │
Correct        Wrong
  ↓               ↓
200 OK          401
```

The lab is designed to help understand the difference between:

* HTTP authentication
* Base64 encoding
* Encryption
* Authentication vs authorization
* HTTP vs HTTPS/TLS
* HTTP request/response headers
* Credential transmission
* Basic Authentication security risks

> ⚠️ **Educational Lab:** This project is intended for learning and testing on a local environment. The credentials used in this lab are dummy credentials and should never be used for real systems.

## 🎯 Goal

The goal of this lab is to understand what actually happens when a client accesses a resource protected by **HTTP Basic Authentication**, rather than simply using a browser login prompt without understanding the underlying HTTP communication.
