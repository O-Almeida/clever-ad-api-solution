# Clever Interview Exercise

A interview excercise application built with Python to process Excel census data and store it in a MySQL database using Docker.

## Prerequisites

- **Docker** and **Docker Compose**
- **Python 3.8** or higher
- **pip** for managing Python packages

## Configure Environment Variables

Crate a `.env` file with the following content (choose the values you want to use):
```env
# MySQL credentials
MYSQL_ROOT_PASSWORD=
MYSQL_DATABASE=
MYSQL_USER=
MYSQL_PASSWORD=

# Application database connection details
DB_HOST=db
DB_USER=
DB_PASSWORD=
DB_NAME=

# Log Configuration
LOG_LEVEL=DEBUG
```

## Start the Docker Container

```bash
docker-compose up -d
```

## License

[MIT](https://choosealicense.com/licenses/mit/)