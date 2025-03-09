-- DO $$ 
-- BEGIN
--    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname='admin') THEN
--       CREATE USER admin WITH PASSWORD 'admin123';
--    END IF;
-- END $$;

CREATE USER admin WITH PASSWORD 'admin123';

-- Create database `admin` 
CREATE DATABASE admin;

-- Grant all privileges on database `admin` to user `admin`
GRANT ALL PRIVILEGES ON DATABASE admin TO admin;

-- Set the owner of schema `public` to user `admin`
\c admin;
ALTER SCHEMA public OWNER TO admin;
GRANT ALL ON ALL TABLES IN SCHEMA public TO admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO admin;


-- CREATE TABLE IF NOT EXISTS tasks (
--     id SERIAL PRIMARY KEY,
--     title VARCHAR(100) NOT NULL,
--     description TEXT,
--     is_complete BOOLEAN DEFAULT FALSE
-- );

-- INSERT INTO tasks (title, description, is_complete) VALUES 
-- ('Task 1', 'Description 1', FALSE),
-- ('Task 2', 'Description 2', TRUE);
