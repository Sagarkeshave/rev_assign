# FastAPI Supabase Integration

This FastAPI application provides a simple API endpoint to update the available copies of a book in a Supabase database. It utilizes the Supabase Python client for database operations.

## Prerequisites

Make sure you have the following installed in your system:

- Python 3.9
- FastAPI
- Uvicorn
- Supabase Python Client

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/Sagarkeshave/rev_assign.git
```

```
cd SAGAR_KESHAVE_OCT/TASK_2
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```


## Usage

1. Run the FastAPI application using Uvicorn:

```
uvicorn main:app --reload
```


2. Open your web browser or a tool like [curl](https://curl.se/) to make a PUT request to update the available copies of a book:

```
curl -X PUT -H "Content-Type: application/json" -d '{"book_id": 1, "new_update_copies": 400}' http://localhost:10000/
```

**Note**
  - Make sure you have a database in supabase with books table with columns ["id", "available_copies"] and replace env variables with proper credentials



