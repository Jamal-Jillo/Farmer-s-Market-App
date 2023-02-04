# Farmers Market App [Mazao]

This project is part of the Alx-Software Engineering course and aims to create a web application for farmers to sell their products directly to consumers.

## Problem Statement

Small-scale farmers often face difficulties in reaching a large customer base and marketing their products effectively. This project aims to create a platform for these farmers to connect with consumers and sell their products directly, increasing their exposure and sales.

## Project Scope

The scope of this project is to create a web application where farmers can create a profile, list their products, and market information. Consumers can search for products, view market information, and place orders.

### The project will include the following features

1. User registration and login
2. Product listing and management
3. Market information display
4. User role management system
5. Order placement and management
6. Payment integration
7. User profile management
8. User dashboard
9. Admin dashboard

## Technology Stack

- Flask (server-side)
- JavaScript (Frontend)
- Python (server-side)
- HTML/CSS (Frontend)
- Bootstrap (Frontend)
- SQL for database management (MySQL)
- SQLAlchemy for database management/ORM (Object Relational Mapping)

## API's

- Stripe API for payment integration
- Google Maps API for market information display
- Twilio API for SMS notifications **(optional)**
- Auth0 or Firebase for user authentication
- KAMIS API for market information display **(To display live market information)**

## Project Structure

The project is structured as follows:
--- to be updated

## Deployment

The app will be deployed on a cloud server for optimal scalability and reliability.

## Project Setup

To run the project locally, you need to have Python, Flask, and PostgreSQL installed on your machine.

1. Clone the repository

        git clone https://github.com/[username]/farmers-market-app.git

2. Create a virtual environment and activate it

        python -m venv venv
        source venv/bin/activate

3. Install the required dependencies

        pip install -r requirements.txt

4. Set up the database

            python
    
            from app import db
            db.create_all()
            exit()

5. Set the environment variables

            export FLASK_APP=app
            export FLASK_ENV=development

6. Run the development server

            flask run

Access the application at:

        http://localhost:5000

## Contributing

If you would like to contribute to the project, please create a fork of the repository, make your changes, and submit a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License

This project is licensed under the MIT License. See LICENSE for more information.

## Authors

Jamal Jillo
