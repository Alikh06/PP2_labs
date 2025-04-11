CREATE TABLE IF NOT EXISTS "user" (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS user_score (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES "user"(id),
  score INTEGER DEFAULT 0,
  level INTEGER DEFAULT 1
);