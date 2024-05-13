## Overview
The solution consists of the following elements:
- Database - SQLite
- REST API Server - Flask app
- FE Client - Vue.js

## Justifications
### Database
- Lightweight: SQLite is a lightweight database engine, making it suitable for small to medium-sized applications where resource usage is a concern.
- Easy to set up: SQLite does not require a separate server process or complex configuration, making it easy to set up and use. This especially reduces the overhead of having another container running the database.
- Cross-platform compatibility

### Connexion-Flask API
- Easy integration: Connexion provides seamless integration between Flask and OpenAPI specifications, allowing you to easily build and document your API.
- Automatic request validation: Connexion automatically validates incoming requests against the defined API schema, ensuring data integrity and reducing the risk of errors.
- Swagger UI support: Connexion generates a Swagger UI interface for your API, making it easy to explore and test your endpoints without the need for additional tools.

## Architecture
- The dev setup is dockerized so that it can be easily be made available through container registries.
- The containers are further orchestrated by `docker-compose`.
- The setup can be deployed easily to any of the major CSPs.

## Additional Feature 
### 1. User favorited properties
The backend work for this has already been done as you can see in the schema. It would be a very nice and obvious feature where there is an additional page/route for the app where each user can view their favorited properties. See [datamodel](./datamodel.md) for details.

### 2. Additional Filters and Ranges
The user should be able to filter through the properties through a variety of criteria such as a sale price range, area range, city etc.
