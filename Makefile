run:
	uvicorn app.main:app --reload

schema_migration:
	alembic revision --autogenerate -m "_to_rename_"

schema_migrate:
	alembic upgrade head

test:
	pytest

init-pyinstaller:
	pyinstaller pyinstaller_entrypoint.py --name api --hidden-import=asyncpg.pgproto.pgproto --onefile

build-executable:
	pyinstaller api.spec


clean:
	find . | grep -E "\(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

clean-build:
	rm -rf build/ dist/

full-clean: clean clean-build

