#!/bin/bash

poetry run python -m api.migrate_cloud_db
poetry run alembic upgrade head

poetry run uvicorn api.main:app --host 0.0.0.0
