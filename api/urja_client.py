import httpx

class UrjaClient:
    def __init__(self, session_token: str):
        self.base_url = "https://urja-ops.flockenergy.tech"
        # We will inject the token at runtime
        self.client = httpx.Client(
            base_url=self.base_url,
            cookies={"__Secure-better-auth.session_token": session_token},
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"}
        )

    def search_meters(self, page: int = 1, query: str = ""):
        response = self.client.get("/portal/meters/search", params={"page": page, "q": query})
        response.raise_for_status()
        return response.json()
