CREATE TABLE entries (
    id SERIAL PRIMARY KEY,
    date DATE UNIQUE NOT NULL,
    weight DECIMAL(4,1) NOT NULL
);

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    entry_id INT REFERENCES entries(id) ON DELETE CASCADE,
    type TEXT CHECK (type IN ('run', 'dumbbells', 'walk')),
    duration_minutes INT,
    calories_burned INT
);

CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    exercise_id INT REFERENCES exercises(id) ON DELETE CASCADE,
    average_pace_per_mile DECIMAL(5,2),
    best_split_time DECIMAL(5,2)
);
