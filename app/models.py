from sqlalchemy import ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from loadenv import envi

print(envi.db_url)

engine = create_async_engine(url=envi.db_url,
                             echo=True)
    
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    black_list = mapped_column(Boolean)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)