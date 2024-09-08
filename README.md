# Survey Microservice

This microservice handles survey management for inquest, including user interactions with surveys (joining, submitting, leaving) and form generation and retrieval.

## Features

- Join surveys
- Submit survey responses
- Leave surveys
- Generate and retrieve forms

## Getting Started

### Prerequisites

- Python 3.9+
- Poetry or pip

### Installation

1. **Clone the repo**:
   ```bash
   git clone <repository-url>
   cd surveys-service
   ```

2. **Set up the environment**:
   ```bash
   poetry install
   poetry shell
   ```

   Or using pip:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure the database**: Update `.env` with your database settings.

4. **Apply migrations**:
   ```bash
   alembic upgrade head
   ```

## Running the Application

Start the FastAPI app with Uvicorn:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## Configuration

Set these environment variables in `.env.example`:

- `DATABASE_URL`
- `SECRET_KEY`
- `ACCESS_TOKEN_EXPIRE_MINUTES`

## License

MIT License. See the [LICENSE](LICENSE) file for details.

---