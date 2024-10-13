Thanx Project Setup Guide

Project Overview

This project contains two main components:

1. App: A Django web application that runs the server.
2. CLI App: A command-line interface (CLI) tool used to interact with the app.

Both components are set up using Docker, making it easy to get up and running without installing dependencies directly on your local machine.

Prerequisites

Ensure you have the following tools installed:

- Git: For cloning the repository.
- Docker and Docker Compose: For setting up and running the project in isolated containers.
- DBeaver (Optional): If you want to connect to the PostgreSQL database using a GUI tool.

Steps to Set Up the Project Locally

1. Clone the Repository

Clone the repository to your local machine:

git clone https://github.com/matibraun/thanx.git
cd <repository-name>

2. Set Up Environment Variables

Create a .env file in the root folder of the project with the following environment variables (or modify them according to your needs):

POSTGRES_DB=thanx
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

3. Build Docker Containers

Build the Docker containers using the following command:

docker-compose up --build

This will build the Docker images for both app (Django server) and cli_app (CLI tool), and start all necessary services, including the PostgreSQL database.

4. Run Migrations

Once the containers are up and running, run the database migrations to set up the necessary tables.

docker-compose run app python manage.py migrate

5. Running the Application

The Django server will be accessible on http://localhost:8000 once the containers are running. You can access the API or admin panel by navigating to this URL in your browser.

To view the logs or troubleshoot, you can run:

docker-compose logs -f app

6. Running CLI Commands

To run CLI commands, use Docker Compose to execute commands from the cli_app container. For example:

docker-compose run cli_app python cli.py <command-name>

This will run your CLI app commands within the container.

7. Accessing PostgreSQL Database

To connect to the PostgreSQL database from a tool like DBeaver, use the following connection details:

- Host: localhost
- Port: 5432
- Database: thanx
- Username: postgres
- Password: postgres

8. Shutting Down the Containers

When you're done working with the project, you can shut down the Docker containers:

docker-compose down

This will stop and remove all containers, networks, and volumes created by Docker Compose.

