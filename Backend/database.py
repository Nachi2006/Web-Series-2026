from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

db= "sqlite:///./workshop.db"
engine=create_engine(
    db,connect_args={"check_same_thread":False}
    )

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()