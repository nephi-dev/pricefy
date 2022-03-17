from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_async_engine("sqlite+aiosqlite:///./database.db")
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


class Session:
    def __aenter__(self):
        self.session = async_session()
        return self.session

    def __aexit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
