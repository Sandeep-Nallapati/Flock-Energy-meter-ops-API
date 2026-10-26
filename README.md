# Flock Energy — Urja Meter Ops API Service

A clean, documented, and lightweight REST API wrapper built over the legacy **Urja Meter Ops** internal utility portal (`https://urja-ops.flockenergy.tech`).

---

## 🚀 Overview
The legacy Urja portal provides vital smart-meter information to field and operations staff but lacks a public API. This service acts as a robust programmatic bridge, consuming the portal's internal endpoints and exposing a clean, structured REST interface complete with automated OpenAPI documentation.

---

## 📁 Repository Structure

```
FlockEnergyAssignment/
├── api/
│   ├── main.py          # FastAPI application & route handlers
│   ├── urja_client.py   # HTTP adapter connecting to the Urja portal
│   └── requirements.txt # Python dependencies
├── PROTOCOL.md          # Technical discovery write-up of the legacy portal
├── REFLECTION.md        # Answers to assignment reflection prompts
└── README.md            # Main documentation & run instructions
```

---

## 🛠️ Installation & Running Locally

### 1. Prerequisites
- Python 3.10+ installed on your system.

### 2. Install Dependencies
```bash
cd api
pip install -r requirements.txt
```

### 3. Run the API Server
```bash
python main.py
```
The server will start locally at `http://127.0.0.1:8000`.

---

## 📖 API Documentation & Exploration

Once the server is running, you can explore and test the interactive API documentation:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **OpenAPI JSON Spec**: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

### Sample Request (cURL)

To query meters through your wrapper, pass your session token via the `X-Session-Token` header:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/meters?page=1&q=' \
  -H 'accept: application/json' \
  -H 'X-Session-Token: YOUR_SESSION_TOKEN_HERE'
```

---

## 💡 Design Decisions & Trade-offs
- **FastAPI Choice**: Chosen because it automatically generates OpenAPI documentation (`/openapi.json`) and interactive Swagger UI out of the box with minimal boilerplate.
- **Header-Based Session Injection**: The client passes cookies directly to the legacy portal, keeping the service lightweight and stateless.

---

## 🚧 What Was Intentionally Skipped
- Automated credential-based login in the wrapper (left as header injection to keep session scope clean and avoid credential storage risks in v1).

---

## 🚀 What We'd Improve With More Time
- Implement server-side session caching with automatic background re-authentication.
- Expose downstream endpoints for meter consumption metrics and network hierarchy trees.
