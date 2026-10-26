# REFLECTION.md — Flock Energy Take-Home Reflection

## 1. What assumptions did you make?
- **Stateless Proxy Model**: Assumed that clients calling our API wrapper will supply their own valid session token via request headers (`X-Session-Token`), delegating session lifetime management to the underlying Urja portal.
- **API Stability**: Assumed that the JSON response schemas discovered during reconnaissance (`/portal/meters/search`) represent the primary data contract used by the legacy frontend.

## 2. Which part was the most difficult, and how did you get unstuck?
- **Discovering the Under-the-Hood API**: Initially, legacy portals can appear purely server-rendered (HTML). By systematically inspecting browser network traffic during page reloads and searches, we uncovered clean underlying JSON endpoints (`/portal/meters/search`), avoiding fragile HTML scraping (BeautifulSoup/Cheerio).

## 3. If you had another day, what would you improve?
- **Automated Login & Session Caching**: Implement an automated login handler (`POST /portal/login`) in the wrapper so consumers don't need to manually extract cookies from their browser.
- **Expanded Endpoints**: Fully map out consumption history (`/portal/meters/{id}/consumption`) and network hierarchy (`/portal/hierarchy`) endpoints.
- **Robust Caching / Rate Limiting**: Add Redis-based caching to reduce redundant calls to the ageing legacy portal and protect it from overload.

## 4. What mistake did you make while solving this?
- Initially considered parsing raw HTML pages for meter data until network inspection revealed the hidden `/portal/meters/search` JSON endpoint. Recognizing this early saved hours of brittle regex/DOM selector work.

## 5. If you were reviewing your own submission, what would you criticise?
- The current implementation relies on the user providing a manual session cookie. While secure and simple, an automated login flow that caches session tokens server-side would provide a much smoother developer experience.
