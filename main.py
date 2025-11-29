from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.contact_routes import contactRouter
from config import settings, ALLOWED_ORIGINS
app = FastAPI()

# Configure CORS to allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(contactRouter)

@app.get("/")
async def root():
    return {"message": "Welcome to E. Alam Fabricator API"}

if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=settings.APP_PORT, log_level="info", reload=True)

