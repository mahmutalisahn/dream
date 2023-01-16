import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.responses import Response
from lop.v1.router.booking_router import BookingRouter
from lop.v1.router.service_router import ServiceRouter

from lop.v1.router.user_router import UserRouter
from lop.v1.router.calendar_router import CalendarRouter

VERSION = "1.0.6"

app = FastAPI(
    title="DREAM BACKEND",
    version=VERSION,
    description="This is a backend service of LAP-CALENDAR",
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sub_app = FastAPI(
    title="DREAM BACKEND",
    version=VERSION,
    description="This is a backend service of LAP-CALENDAR",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

sub_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sub_app.include_router(
    UserRouter().get_router(), prefix="/user_service", tags=["User"]
)
sub_app.include_router(
    CalendarRouter().get_router(), prefix="/calendar_service", tags=["Calendar"]
)
sub_app.include_router(
    BookingRouter().get_router(), prefix="/booking_service", tags=["Booking"]
)
sub_app.include_router(
    ServiceRouter().get_router(), prefix="/service_service", tags=["Service"]
)

app.mount("/v1/editor_backend", sub_app)


@sub_app.exception_handler(Exception)
async def catch_exceptions_middleware(request: Request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    # Change here to LOGGER
    return JSONResponse(
        status_code=400, content={"message": f"{base_error_message}. Detail: {err}"}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
