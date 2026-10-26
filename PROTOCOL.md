# PROTOCOL.md — Urja Meter Ops Legacy Portal Protocol

This document details the reverse-engineering and protocol discovery findings for the legacy internal web portal **"Urja Meter Ops"** (`https://urja-ops.flockenergy.tech`).

---

## 1. Authentication Mechanism

- **Type**: Cookie-based session authentication using **Better Auth**.
- **Primary Session Cookie**: `__Secure-better-auth.session_token`
- **Login Flow**:
  1. Users authenticate via a standard login page with username (`operator@urja.local`) and password (`urja-ops-2026`).
  2. Upon successful authentication, the server sets the secure session token cookie.
  3. Subsequent API calls and page loads include this cookie in the request headers (`cookie: __Secure-better-auth.session_token=...`).

---

## 2. Discovered Internal Endpoints

Through browser network inspection (DevTools > Network tab), the following internal JSON endpoints were discovered:

### A. Search & List Meters
- **Endpoint**: `/portal/meters/search`
- **Method**: `GET`
- **Query Parameters**:
  - `q`: Search string (e.g. meter ID or serial number)
  - `page`: Page number (integer, starting at 1)
- **Response Format**:
  ```json
  {
      "data": [
          {
              "meterId": "J100000",
              "serialNo": "SE33962",
              "make": "HPL",
              "phaseType": "single",
              "installStatus": "Decommissioned",
              "dtCode": "DT-001"
          }
      ],
      "total": 403,
      "page": 1,
      "pageSize": 20
  }
  ```

---

## 3. Quirks, Observations & Anomalies

1. **JSON vs. HTML Mixed Architecture**: While some pages load raw HTML templates, core data grids are powered by clean backend JSON endpoints (like `/portal/meters/search`), which makes building an API wrapper much cleaner and less fragile than screen-scraping HTML DOM structures.
2. **Session Expiry**: Sessions time out after inactivity, returning `401 Unauthorized` or redirecting to the login flow. Our wrapper intercepts and surfaces these cleanly to API consumers.
