from unittest.mock import AsyncMock

import pytest
from fastapi import status, Response

from app.middlewares import LogExecutionTimeMiddleware


@pytest.mark.asyncio
async def test_log_execution_time_middleware(async_client):
    """
    Ensure that the middleware is called when a request is made to the API
    """
    middleware = LogExecutionTimeMiddleware.dispatch = AsyncMock(return_value=Response(status_code=200, content="{}"))
    ret = await async_client.get("/healthcheck")
    assert ret.status_code == status.HTTP_200_OK
    assert middleware.called

