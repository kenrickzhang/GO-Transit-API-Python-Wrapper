class APIError(Exception):
    def __init__(self, response):
        self.status_code = response.status_code
        self.message = response.text
        super().__init__(f"APIError {self.status_code}: {self.message}")
