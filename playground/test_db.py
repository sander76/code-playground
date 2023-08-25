import asyncio

import pytest
import pytest_asyncio
from alembic.config import main
from grid_insight_mrid_registry.dependencies import db_models
from grid_insight_mrid_registry.dependencies.db_models import (
    NameMridMapping,
    NameType,
    NameTypeAuthority,
)
from grid_insight_mrid_registry.settings import settings
from grid_insight_mrid_registry.v1 import models
from grid_insight_mrid_registry.v1.controller import Controller, NotAllowed
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="module")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="module")
def engine(with_postgres, event_loop):
    db_url = with_postgres.get_connection_url()

    assert db_url.endswith("test")

    db_url = db_url.replace("psycopg2", "asyncpg")
    _engine = create_async_engine(db_url, echo=True, future=True)

    yield _engine


@pytest.fixture()
def with_alembic(engine):
    # use the connection url from the test container.
    settings.db_url = str(engine.url)
    try:
        main(["--raiseerr", "upgrade", "head"])
        yield engine
    except Exception as err:
        print(err)
    finally:
        pass


@pytest_asyncio.fixture()
async def get_session(with_alembic):
    # assert settings.db_url.endswith("test")
    assert with_alembic.url.database.endswith("test")

    yield sessionmaker(with_alembic, expire_on_commit=False, class_=AsyncSession)

    async with with_alembic.begin() as connection:
        await connection.run_sync(db_models.Base.metadata.drop_all)
        await connection.execute(text("DROP TABLE alembic_version"))
