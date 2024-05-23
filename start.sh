#!/bin/bash

# change to server directory
cd backend

# activate virtualenv
source $(poetry env info --path)/bin/activate

# install dependencies and start fastapi server
poetry install

alembic -c alembic_local.ini upgrade head

cd app
uvicorn main:app --reload &

# change to client directory
cd ../../frontend

# install dependencies and start react app
npm install && npm run dev &

# return to root directory
cd ..

# The end of the script
echo "React and FastAPI applications have been started."
