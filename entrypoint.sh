#!/bin/sh

# Executa migrações do banco de dados
poetry run alembic upgrade head

# Inicia a aplicação
poetry run fastapi run fast_zero/app.py --host 0.0.0.0