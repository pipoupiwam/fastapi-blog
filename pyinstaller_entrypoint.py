import uvicorn

from app.main import app

"""
This file is used by pyinstaller to build the distributable binary file.
It is at the project root folder to make sure that imports work properly.
"""

def serve():
    """Serve the web application."""
    uvicorn.run(app, port=8000)  # or whatever port number you want.


if __name__ == "__main__":
    serve()
