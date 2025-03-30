from db.db import get_connection
from datetime import datetime, date

def insert_entry(date: date, weight: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO entries (date, weight) VALUES (%s, %s) ON CONFLICT (date) DO NOTHING;", (date, weight))
    conn.commit()
    cur.close()
    conn.close()

date_entry = input("Is this for today? Y/N:")

while True:
    try:
        if date_entry == "Y":
            input_date: date = datetime.today().date()
            break
        else:
            date_input: str = input("What is the date? MM-DD-YYYY format only")
            input_date = datetime.strptime(date_input, "%m-%d-%Y").date()
            break
    except ValueError:
        print("Invalid input, try again in this format: MM-DD-YYYY")

while True:
    try:
        weight: float = float(input("Weight? ###.# format only:"))
        break
    except ValueError:
        print("Invalid input, try again in this format: ###.#")


insert_entry(input_date, weight)