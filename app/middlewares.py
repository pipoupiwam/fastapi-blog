import logging
import time

# from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("blog-logger.middlewares")


class LogExecutionTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.debug(f"{request.method} {request.url} executed in {process_time:.5f} seconds")
        return response
