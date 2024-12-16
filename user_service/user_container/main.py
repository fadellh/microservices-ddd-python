from fastapi import FastAPI
from user_service.user_application.rest.user_controller import user_controller


app = FastAPI()

app.include_router(user_controller)