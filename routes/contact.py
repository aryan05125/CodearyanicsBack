from fastapi import APIRouter
from models.contact_model import Contact
from db import db

contact_router = APIRouter()

@contact_router.post("/contact")
async def submit_contact(contact: Contact):
    data = contact.dict()
    await db["contacts"].insert_one(data)
    return {"status": "saved"}
