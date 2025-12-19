CREATE TABLE IF NOT EXISTS notes (
  id SERIAL PRIMARY KEY,
  content TEXT NOT NULL
);

INSERT INTO notes (content) VALUES
('test note 1'),
('test note 2');
