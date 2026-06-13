from sqlalchemy import Integer,Column,String
from database import Base

class Participant(Base):
    __tablename__ = "participants"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String,unique=True)
    role=Column(String,default="attendees")