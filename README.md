# Testing Fast API
Simple Blog APIs based on FastAPI and SqlAlchemy.

## Setup

- Create a virtualenv `virtualenv venv -p python3.10`
- install requirements `pip install -r requirements.txt`

## Makefile

A Makefile provides a set of commands to work with the project

- `make run` : Start the project in development mode 
- `make schema_migration` : Generate database migrations. Do not forget to rename the migration with an explicit name
- `make schema_migrate` : Apply the migrations on the database
- `make test` : Launch the test suit
- `make init-pyinstaller` : Init pyinstaller and create an `api.spec` file
- `make build-executable` : Build an executable, to be used in AWS Lamda. 
- `make clean` : clean the work directory

SnapshotTest is used for testing, to generate snapshots 
```bash
pytest --snapshot-update
```


