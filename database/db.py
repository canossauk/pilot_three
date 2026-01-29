from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

# Database connection string using aiosqlite
DATABASE_URL = "sqlite+aiosqlite:///./database/school.db"

# Create the Async Engine
# echo=True is helpful for debugging, but we can turn it off for production
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async def init_db():
    """Initializes the database by creating tables."""
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all) # Uncomment to reset
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncSession:
    """Dependency for getting an AsyncSession."""
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
