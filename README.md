### **Basic Project Setup for Your PostgreSQL Database**  

Since you’ll integrate this with a web app later, we’ll keep things simple and modular.  

#### **1. Project Directory Structure**
```
health_tracker/
│── db/                # Database-related files
│   ├── schema.sql     # SQL file to define tables
│   ├── seed.sql       # Optional: Initial test data
│   ├── db.py          # Python file to connect & interact with DB
│── scripts/           # Utility scripts
│   ├── insert_data.py # Sample script to insert data
│── .env               # Stores database credentials (git ignored)
│── main.py            # Entry point to test the setup
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
```

#### **2. Install PostgreSQL Locally**  
Make sure PostgreSQL is installed and running on your machine.  

- **Mac (Homebrew):**  
  ```sh
  brew install postgresql
  brew services start postgresql
  ```

- **Ubuntu:**  
  ```sh
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```

- **Windows (WSL Recommended):**  
  Install via [PostgreSQL official website](https://www.postgresql.org/download/).

#### **3. Create Your Database**
```sh
psql -U your_username -d postgres
CREATE DATABASE health;
```
Then, switch to it:
```sh
\c health
```

#### **4. Define Your Tables (`schema.sql`)**
```sql
CREATE TABLE entries (
    id SERIAL PRIMARY KEY,
    date DATE UNIQUE NOT NULL,
    weight DECIMAL(5,2) NOT NULL
);

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    entry_id INT REFERENCES entries(id) ON DELETE CASCADE,
    type TEXT CHECK (type IN ('run', 'dumbbells', 'walk')),
    duration_minutes INT NOT NULL,
    calories_burned INT NOT NULL
);

CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    exercise_id INT REFERENCES exercises(id) ON DELETE CASCADE,
    average_pace_per_mile DECIMAL(5,2),
    best_split_time DECIMAL(5,2)
);
```

#### **5. Load Schema into PostgreSQL**
Run:
```sh
psql -U your_username -d health -f db/schema.sql
```

#### **6. Python Setup**
Install dependencies:
```sh
pip install psycopg2 dotenv
```

Create a `.env` file:
```
DB_NAME=health
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Connect using Python (`db.py`):
```python
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
```

#### **7. Insert Sample Data (`insert_data.py`)**
```python
from db import get_connection

def insert_entry(date, weight):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO entries (date, weight) VALUES (%s, %s) ON CONFLICT (date) DO NOTHING;", (date, weight))
    conn.commit()
    cur.close()
    conn.close()

insert_entry('2025-03-30', 180.5)
```

#### **8. Verify Data**
```sh
psql -U your_username -d health -c "SELECT * FROM entries;"
```

This sets up a simple but functional PostgreSQL database with Python interaction. Later, you can expand this by adding a Flask/FastAPI backend for your web app.

Would you like any modifications to this setup?