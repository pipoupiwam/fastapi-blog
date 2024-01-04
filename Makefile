run:
	uvicorn app.main:app --reload

schema_migration:
	alembic revision --autogenerate -m "_to_rename_"

schema_migrate:
	alembic upgrade head

