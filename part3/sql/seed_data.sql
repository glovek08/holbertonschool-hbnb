-- insert into db with this command: 
-- mysql -u <username> -p -h <host> < <absolute_path_to_seed_data.sql>

CREATE DATABASE IF NOT EXISTS hbnb_v1;

USE hbnb_v1;

-- remove all data first.
DELETE FROM users;
DELETE FROM amenities;

-- inject user admin.
INSERT INTO users (id, email, first_name, last_name, password, is_admin, created_at, updated_at)
VALUES (
    UUID(),
    'admin@hbnb.io',
    'Admin',
    'HBnB',
    '$2a$12$mi0ECvslyF3X5Wnen/h4cevTNcYqR9Lkb.2jzS9JR2fJyuXFkjkny', -- manually hashed 'admin1234'.
    TRUE,
    NOW(),
    NOW()
);

-- inject some amenities.
INSERT INTO amenities (id, name, created_at, updated_at) VALUES
(UUID(), 'WiFi', NOW(), NOW()),
(UUID(), 'Swimming Pool', NOW(), NOW()),
(UUID(), 'Air Conditioning', NOW(), NOW());
