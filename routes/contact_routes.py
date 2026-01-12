from fastapi import APIRouter, status
from schemas.contact_schema import ContactForm
from services.contact_service import sendContactEmail


contactRouter = APIRouter(prefix="/api/v1", tags=['ContactPage'])

@contactRouter.post("/contact", status_code=status.HTTP_200_OK)
async def contact(form: ContactForm):
    await sendContactEmail(form)