Map My World API
Map My World API is a backend service designed to manage locations and categories, providing an interactive map for exploring and reviewing locations. This project is powered by FastAPI, Poetry, and Uvicorn.

Prerequisites
Before setting up and running the project, ensure you have the following installed on your system:

Python
Poetry (for dependency management)

Setup Instructions

1. Clone the repository
First, clone the project repository to your local machine:
git clone https://github.com/alejogil/map-my-world-api.git

2. Install Poetry
If you don't have Poetry installed, you can install it by running the following command:
curl -sSL https://install.python-poetry.org | python3 -

3. Install dependencies
Once Poetry is installed, use it to install the project dependencies:
poetry install

4. Running the Project
Now that everything is set up, you can run the project using Uvicorn. FastAPI uses Uvicorn as an ASGI server. To run the server with hot-reloading enabled, use:
poetry run uvicorn app.main:app --reload

This command will start the FastAPI application at http://127.0.0.1:8000 by default. You can now access the API and use the interactive documentation provided by Swagger at:
http://127.0.0.1:8000/docs