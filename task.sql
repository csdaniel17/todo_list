-- table for tasks:
CREATE TABLE task (
  id serial PRIMARY KEY,
  task varchar NOT NULL,
  completed boolean
);
