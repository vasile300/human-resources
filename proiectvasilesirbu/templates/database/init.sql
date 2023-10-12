CREATE TABLE candidati (
  id serial primary key,
  username varchar(20),
  name varchar(20),
  curriculum_vitae varchar(20)
);

INSERT INTO candidati (username, name, curriculum_vitae)
VALUES
  ('Ion', 'Popescu', 'phyton,java'),
  ('Maria', 'Ionescu', 'PostgresSQL,c++'),
  ('Andrei', 'Vasilescu', 'React,css3'),
  ('Anna', 'Mihai', 'html5,django'),
  ('Alexandru', 'Stanescu', 'firewalls,criptare');
