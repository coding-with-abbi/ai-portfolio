"""
Base class and utilities shared by every external-API tool in the pipeline.

Provides:
* ``RateLimiter`` -- token-bucket rate limiter (thread-safe).
* ``BaseAPITool``  -- abstract base with automatic retry + exponential backoff.
"""

import logging
import threading
import time
from abc import ABC, abstractmethod
from typing import Any

logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------- #
#  Rate limiter                                                                #
# --------------------------------------------------------------------------- #

class RateLimiter:
    """Thread-safe token-bucket rate limiter.

    Parameters
    ----------
    calls_per_minute : int
        Maximum number of calls allowed per 60-second window.
    """

    def __init__(self, calls_per_minute: int = 60) -> None:
        self.calls_per_minute = calls_per_minute
        self.interval = 60.0 / calls_per_minute
        self._lock = threading.Lock()
        self._last_call: float = 0.0

    def wait(self) -> None:
        """Block the calling thread until the next call is permitted."""
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_call
            if elapsed < self.interval:
                time.sleep(self.interval - elapsed)
            self._last_call = time.monotonic()


# --------------------------------------------------------------------------- #
#  Abstract base tool                                                          #
# --------------------------------------------------------------------------- #

class BaseAPITool(ABC):
    """Abstract base for any tool that wraps an external API call.

    Sub-classes must implement :pymeth:`run`.  Callers should invoke
    :pymeth:`execute_with_retry` to benefit from automatic retries with
    exponential back-off.
    """

    def __init__(
        self,
        calls_per_minute: int = 60,
        max_retries: int = 3,
        retry_delay: float = 2.0,
    ) -> None:
        self.rate_limiter = RateLimiter(calls_per_minute)
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    # -- public entry point ------------------------------------------------- #

    def execute_with_retry(self, *args: Any, **kwargs: Any) -> Any:
        """Call :pymeth:`run` with automatic retries and exponential back-off.

        Returns whatever ``run()`` returns on the first successful attempt.

        Raises:
            Exception: Re-raises the last exception after all retries are
                       exhausted.
        """
        last_exception: Exception | None = None

        for attempt in range(1, self.max_retries + 1):
            try:
                self.rate_limiter.wait()
                return self.run(*args, **kwargs)
            except Exception as exc:
                last_exception = exc
                if attempt < self.max_retries:
                    delay = self.retry_delay * (2 ** (attempt - 1))
                    logger.warning(
                        "Attempt %d/%d failed (%s). Retrying in %.1fs ...",
                        attempt,
                        self.max_retries,
                        exc,
                        delay,
                    )
                    time.sleep(delay)
                else:
                    logger.error(
                        "All %d attempts failed. Last error: %s",
                        self.max_retries,
                        exc,
                    )

        raise last_exception  # type: ignore[misc]

    # -- to be implemented by sub-classes ----------------------------------- #

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the actual API call. Must be overridden."""
