from pydantic import BaseModel

class participantBase(BaseModel):
    name: str
    email: str
    role: str = "attendee"

class participantCreate(participantBase):
    pass

class participantResponse(participantBase):
    id: int

    class Config:
        from_attributes = True