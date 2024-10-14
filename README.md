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
cd {repository-name}

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

The Django server will be accessible on http://localhost:8000 once the containers are running.

6. Running CLI Commands and API Requests

The app comes with preloaded information for all items (users, rewards, redemptions) so from the begining you can check information and load data too.

To run CLI commands, run a terminal and then position yourself within app_cli folder (placed inside thanx root folder), and run the following command:

python3 cli.py {command-name}

for instance:

python3 cli.py list-users

* if you don't have python3 installed you can run it with python instead of python3.

In addition to CLI commands, you can interact with the application using API requests via Postman or the browser.

Below are the CLI commands with their equivalent API routes and methods:

The following are the commands and their payloads:


1-List Users

CLI Command: python3 cli.py list-users

API Endpoint: GET /user/users/

Example: http://localhost:8000/user/users/


2-Create User

CLI Command: python3 cli.py create-user user@example.com John Doe --country_code +1 --phone 1234567890 --document_type passport --document_number A12345678 --address "123 Main St" --nationality USA --gender male --civil_state single

API Endpoint: POST /user/users/
Example Payload:
{ "email": "user@example.com", "first_name": "John", "last_name": "Doe", "country_code": "+1", "phone": "1234567890", "document_type": "passport", "document_number": "A12345678", "address": "123 Main St", "nationality": "USA", "gender": "male", "civil_state": "single" }

Example: http://localhost:8000/user/users/


3-Get User Points Balance

CLI Command: python3 cli.py get-user-points-balance 1

API Endpoint: GET /user/users/{id}/points-balance/

Example: http://localhost:8000/user/users/1/points-balance/


4-List Rewards

CLI Command: python3 cli.py list-rewards

API Endpoint: GET /reward/rewards/

Example: http://localhost:8000/reward/rewards/


5-List Available Rewards

CLI Command: python3 cli.py list-available-rewards

API Endpoint: GET /reward/available-rewards/

Example: http://localhost:8000/reward/available-rewards/


6-Create Reward

CLI Command: python3 cli.py create-reward "Free Coffee" 100 --description "Redeem for a free coffee at the café."

API Endpoint: POST /reward/rewards/
Example Payload:
{ "name": "Free Coffee", "points_required": 100, "description": "Redeem for a free coffee at the café." }

Example: http://localhost:8000/reward/rewards/


7-List Redemptions

CLI Command: python3 cli.py list-redemptions

API Endpoint: GET /reward/redemptions/

Example: http://localhost:8000/reward/redemptions/


8-List Redemptions by User

CLI Command: python3 cli.py list-redemptions-by-user 1

API Endpoint: GET /reward/redemptions/user/{id}/

Example: http://localhost:8000/reward/redemptions/user/1/


9-Redeem Reward

CLI Command: python3 cli.py redeem-reward --user-id 1 --reward-id 2

API Endpoint: POST /reward/redemptions/
Example Payload:
{ "user_id": 1, "reward_id": 2 }

Example: http://localhost:8000/reward/redemptions/


10-List Transactions

CLI Command: python3 cli.py list-transactions

API Endpoint: GET /transaction/transactions/

Example: http://localhost:8000/transaction/transactions/


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

9. Running tests:

To run the tests for the project, follow these steps:

Position yourself within the root folder (where manage.py lives).

Execute the following command to run the tests inside the Docker container:

Tests command: docker-compose exec app python manage.py test