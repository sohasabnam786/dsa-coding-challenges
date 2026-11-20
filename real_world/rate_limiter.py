"""
Rate Limiter
Implement different rate limiting algorithms.

Algorithms: Token Bucket, Sliding Window, Fixed Window.
"""
import time
from collections import deque


class TokenBucket:
    """Token Bucket Rate Limiter.
    Allows bursts up to capacity, refills at a constant rate.
    """
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = now

    def allow_request(self) -> bool:
        self._refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


class SlidingWindowLog:
    """Sliding Window Log Rate Limiter.
    Tracks individual request timestamps.
    """
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = deque()

    def allow_request(self) -> bool:
        now = time.time()
        cutoff = now - self.window

        while self.requests and self.requests[0] < cutoff:
            self.requests.popleft()

        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False


class FixedWindowCounter:
    """Fixed Window Counter Rate Limiter."""
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window = window_seconds
        self.current_count = 0
        self.window_start = time.time()

    def allow_request(self) -> bool:
        now = time.time()
        if now - self.window_start >= self.window:
            self.window_start = now
            self.current_count = 0

        if self.current_count < self.max_requests:
            self.current_count += 1
            return True
        return False


if __name__ == "__main__":
    limiter = TokenBucket(capacity=5, refill_rate=1.0)
    for i in range(10):
        allowed = limiter.allow_request()
        print(f"Request {i+1}: {'Allowed' if allowed else 'Denied'}")
