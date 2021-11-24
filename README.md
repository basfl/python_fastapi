
# virtualenv 
 * py -3 -m venv venv
 * activate.bat

# FastAPI

* [FastAPI resource](https://fastapi.tiangolo.com/tutorial/first-steps/)


* Start server :   uvicorn app.main:app --reload


# Alembic 

  * [Alembic resource](https://alembic.sqlalchemy.org/en/latest/)

  * Setting up :

    | env.py  | alembic.ini  |
    | ----------- | ----------- |
    | config.set_main_option  | sqlalchemy.url =  |
    | target_metadata = Base.metadata  | N/A | 

  * commands :

    * alembic init {dirname}
    * alembic revision -m {msg}
    * alembic upgrade {revisionId}
    * alembic revision --autogenerate  -m "auto_vote"