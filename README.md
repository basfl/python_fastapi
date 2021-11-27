
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

# Heroku :
  # project URL : 
  * [project URL](https://basfl-fastapi.herokuapp.com/)
  * [api documentation](https://basfl-fastapi.herokuapp.com/docs)
  
  # commands :
    * heroku create {}
    * git push heroku 
    * heroku addons:create heroku-postgresql:hobby-dev
    * heroku ps:restart

# Docker :
  *  DEV :
      *  docker-compose -f docker-compose-dev.yml up 
  * PROD :
    * docker-compose -f docker-compose-prod.yml up