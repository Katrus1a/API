from sqlalchemy.ext.asyncio import create_async_engine



engine = create_async_engine("sqlite+aiosqlite:///example.db", echo=True)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class Task0rm(Model):
    __tablename__="tasks"
    id: Mapped[int]=mapped_column(primary_key=False)
    name: Mapped[str]
    description: Mapped[Optional[str]]


    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Model.metadate.create_all)

    async def delete_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Model.metadate.drop_all)

