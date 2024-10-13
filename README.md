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

To run CLI commands, position yourself within app_cli folder (placed inside root folder), and run the following command:

python3 cli.py <command-name>

for instance:

python3 cli.py list-users

* if you don't have python3 installed you can run it with python instead of python3

The app comes with preload information for all items (users, rewards, redemptions, and so) so from the begining you can check information or load data too.

The following are the commands and their payloads:

    1. list-users
    Description: Lists all users.
    Payload: None.

    Command: python cli.py list-users

    2. create-user
    Description: Creates a new user with the given details.
    Payload:
    email: User email.
    first_name: User's first name.
    last_name: User's last name.
    country_code: Country code (optional, default: empty string).
    phone: Phone number (optional, default: empty string).
    document_type: Document type.
    document_number: Document number.
    address: User address (optional, default: empty string).
    nationality: User nationality (optional, default: empty string).
    gender: Gender (optional, default: empty string).
    civil_state: Civil state (optional, default: empty string).

    Command: python cli.py create-user user@example.com John Doe --country_code +1 --phone 1234567890 --document_type passport --document_number A12345678 --address "123 Main St" --nationality USA --gender male --civil_state single

    3. get-user-points-balance
    Description: Retrieves a user's points balance.
    Payload:
    user_id: User ID to retrieve points balance for.

    Command: python cli.py get-user-points-balance 1

    4. list-rewards
    Description: Lists all rewards available.
    Payload: None.

    Command: python cli.py list-rewards

    5. list-available-rewards
    Description: Lists rewards that are available to be redeemed.
    Payload: None.

    Command: python cli.py list-available-rewards

    6. create-reward
    Description: Creates a new reward.
    Payload:
    name: Name of the reward.
    points_required: Points required to redeem the reward.
    description: Description of the reward (optional).

    Command: python cli.py create-reward "Free Coffee" 100 --description "Redeem for a free coffee at the café."

    7. list-redemptions
    Description: Lists all redemptions.
    Payload: None.

    Command: python cli.py list-redemptions

    8. list-redemptions-by-user
    Description: Lists redemptions for a specific user.
    Payload:
    user_id: User ID to list redemptions for.

    Command: python cli.py list-redemptions-by-user 1

    9. redeem-reward
    Description: Redeems a reward for a user.
    Payload:
    user_id: ID of the user redeeming the reward.
    reward_id: ID of the reward being redeemed.

    Command: python cli.py redeem-reward --user-id 1 --reward-id 2

    10. list-transactions
    Description: Lists all transactions.
    Payload: None.

    Command: python cli.py list-transactions

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

