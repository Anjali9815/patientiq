import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from core.config import DATABASE_URL
from core.database import Base
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    connectable = create_async_engine(DATABASE_URL)
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

import asyncio
asyncio.run(run_migrations_online())