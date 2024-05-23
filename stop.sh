#!/bin/bash

# stop the fastapi server
kill $(lsof -t -i:8000)

# stop the react app
kill $(lsof -t -i:3000)

echo "React and FastAPI applications have been stopped."
