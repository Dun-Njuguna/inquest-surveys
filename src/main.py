from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from src.utils.app_lifespan import lifespan
from src.utils.exception_handlers import global_exception_handler, global_http_exception_handler, validation_exception_handler
from src.utils.auth_middleware import AuthMiddleware

# Import routers from your controllers
from src.controllers.survey_controller import router as survey_router
from src.controllers.user_survey_controller import router as user_survey_router
from src.controllers.form_controller import router as form_router

app = FastAPI(
        lifespan=lifespan,
        docs_url="/docs", 
        redoc_url="/redoc"
    )

# List of routes to exempt from authentication
exempt_paths = ["/auth/", "/docs", "/redoc", "/openapi.json"]

# Add the AuthMiddleware
app.add_middleware(AuthMiddleware, exempt_paths=exempt_paths)

app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(HTTPException, global_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Register controllers
app.include_router(survey_router, prefix="/survey", tags=["Surveys"])
app.include_router(user_survey_router, prefix="/user-survey", tags=["User Survey"])
app.include_router(form_router, prefix="/form", tags=["Form"])


# Root endpoint, useful for health checks
@app.get("/")
def read_root():
    return {"message": "Welcome to the Survey Microservice"}


# Entry point for running the app directly
if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI app using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
