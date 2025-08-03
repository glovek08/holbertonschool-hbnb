-- Use command: mysql -u <username> -p -h localhost < seed_data.sql
CREATE DATABASE IF NOT EXISTS hbnb_v1;

USE hbnb_v1;

SET FOREIGN_KEY_CHECKS = 0;

DELETE FROM users;
DELETE FROM amenities;
DELETE FROM places;
DELETE FROM reviews;

SET FOREIGN_KEY_CHECKS = 1;

-- @block
INSERT INTO users (id, email, first_name, last_name, password, is_admin, created_at, updated_at)
VALUES
(UUID(), 'admin@hbnb.io', 'Admin', 'HBnB', '$2a$12$mi0ECvslyF3X5Wnen/h4cevTNcYqR9Lkb.2jzS9JR2fJyuXFkjkny', TRUE, NOW(), NOW()), -- password: admin1234
(UUID(), 'john.doe@hbnb.io', 'John', 'Doe', '$2a$12$mi0ECvslyF3X5Wnen/h4cevTNcYqR9Lkb.2jzS9JR2fJyuXFkjkny', FALSE, NOW(), NOW()), -- password: admin1234
(UUID(), 'minecraft6969@hbnb.io', 'Ignacio', 'Capezzolo', '$2a$12$mi0ECvslyF3X5Wnen/h4cevTNcYqR9Lkb.2jzS9JR2fJyuXFkjkny', FALSE, NOW(), NOW()), -- password: admin1234
(UUID(), 'alice.wonder@hbnb.io', 'Alice', 'Wonder', '$2a$12$mi0ECvslyF3X5Wnen/h4cevTNcYqR9Lkb.2jzS9JR2fJyuXFkjkny', FALSE, NOW(), NOW()), -- password: admin1234
(UUID(), 'maestropanadero96@hbnb.io', 'Federico', 'Paganini', '$2a$12$mi0ECvslyF3X5Wnen/h4cevTNcYqR9Lkb.2jzS9JR2fJyuXFkjkny', FALSE, NOW(), NOW()), -- password: admin1234
(UUID(), 'redrogsoviet@hbnb.io', 'Yamandu', 'Orsi', '$2a$12$mi0ECvslyF3X5Wnen/h4cevTNcYqR9Lkb.2jzS9JR2fJyuXFkjkny', FALSE, NOW(), NOW()); -- password: admin1234

-- @block
INSERT INTO amenities (id, name, description, created_at, updated_at) VALUES
(UUID(), 'WiFi', "Fast AF Internet", NOW(), NOW()),
(UUID(), 'Swimming Pool', "Don't pee in the pool, no sex allowed", NOW(), NOW()),
(UUID(), 'Air Conditioning', "Doesn't work but we'll charge you for the placebo effect",NOW(), NOW()),
(UUID(), 'Parking', NULL, NOW(), NOW()),
(UUID(), 'Gym', NULL, NOW(), NOW()),
(UUID(), 'Pet Friendly', "No kids allowed, just dogs",NOW(), NOW());

-- @block
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at) VALUES
(UUID(), 'Cozy Apartment in NYC', 'A beautiful apartment in the heart of New York City.', 150, 40.7128, -74.0060, (SELECT id FROM users WHERE email = 'john.doe@hbnb.io'), NOW(), NOW()),
(UUID(), 'Beach House in Miami', 'A luxurious beach house with stunning ocean views.', 300, 25.7617, -80.1918, (SELECT id FROM users WHERE email = 'maestropanadero96@hbnb.io'), NOW(), NOW()),
(UUID(), 'Cabin in the Woods', 'A peaceful cabin surrounded by nature.', 120, 34.0522, -118.2437, (SELECT id FROM users WHERE email = 'alice.wonder@hbnb.io'), NOW(), NOW()),
(UUID(), 'Modern Loft in San Francisco', 'A stylish loft in downtown San Francisco.', 200, 37.7749, -122.4194, (SELECT id FROM users WHERE email = 'minecraft6969@hbnb.io'), NOW(), NOW()),
(UUID(), 'Villa in Tuscany', 'A charming villa in the beautiful countryside of Tuscany.', 400, 43.7711, 11.2486, (SELECT id FROM users WHERE email = 'redrogsoviet@hbnb.io'), NOW(), NOW()),
(UUID(), 'Penthouse in Tokyo', 'A luxurious penthouse with a breathtaking city view.', 500, 35.6895, 139.6917, (SELECT id FROM users WHERE email = 'admin@hbnb.io'), NOW(), NOW()),
(UUID(), 'Cottage in the Cotswolds', 'A cozy cottage in the picturesque Cotswolds.', 180, 51.8333, -1.8333, (SELECT id FROM users WHERE email = 'john.doe@hbnb.io'), NOW(), NOW()),
(UUID(), 'Lake House in Canada', 'A serene lake house perfect for a relaxing getaway.', 250, 44.2312, -76.4860, (SELECT id FROM users WHERE email = 'maestropanadero96@hbnb.io'), NOW(), NOW()),
(UUID(), 'Desert Retreat in Arizona', 'A unique retreat in the heart of the Arizona desert.', 220, 34.0489, -111.0937, (SELECT id FROM users WHERE email = 'alice.wonder@hbnb.io'), NOW(), NOW());

-- @block
INSERT INTO place_amenities (place_id, amenity_id) VALUES
((SELECT id FROM places WHERE title = 'Cozy Apartment in NYC'), (SELECT id FROM amenities WHERE name = 'WiFi')),
((SELECT id FROM places WHERE title = 'Cozy Apartment in NYC'), (SELECT id FROM amenities WHERE name = 'Air Conditioning')),
((SELECT id FROM places WHERE title = 'Beach House in Miami'), (SELECT id FROM amenities WHERE name = 'Swimming Pool')),
((SELECT id FROM places WHERE title = 'Beach House in Miami'), (SELECT id FROM amenities WHERE name = 'WiFi')),
((SELECT id FROM places WHERE title = 'Cabin in the Woods'), (SELECT id FROM amenities WHERE name = 'Pet Friendly')),
((SELECT id FROM places WHERE title = 'Cabin in the Woods'), (SELECT id FROM amenities WHERE name = 'Parking')),
((SELECT id FROM places WHERE title = 'Modern Loft in San Francisco'), (SELECT id FROM amenities WHERE name = 'WiFi')),
((SELECT id FROM places WHERE title = 'Modern Loft in San Francisco'), (SELECT id FROM amenities WHERE name = 'Gym')),
((SELECT id FROM places WHERE title = 'Villa in Tuscany'), (SELECT id FROM amenities WHERE name = 'Pet Friendly')),
((SELECT id FROM places WHERE title = 'Villa in Tuscany'), (SELECT id FROM amenities WHERE name = 'Parking')),
((SELECT id FROM places WHERE title = 'Penthouse in Tokyo'), (SELECT id FROM amenities WHERE name = 'WiFi')),
((SELECT id FROM places WHERE title = 'Penthouse in Tokyo'), (SELECT id FROM amenities WHERE name = 'Air Conditioning')),
((SELECT id FROM places WHERE title = 'Cottage in the Cotswolds'), (SELECT id FROM amenities WHERE name = 'Parking')),
((SELECT id FROM places WHERE title = 'Cottage in the Cotswolds'), (SELECT id FROM amenities WHERE name = 'Pet Friendly')),
((SELECT id FROM places WHERE title = 'Lake House in Canada'), (SELECT id FROM amenities WHERE name = 'WiFi')),
((SELECT id FROM places WHERE title = 'Lake House in Canada'), (SELECT id FROM amenities WHERE name = 'Swimming Pool')),
((SELECT id FROM places WHERE title = 'Desert Retreat in Arizona'), (SELECT id FROM amenities WHERE name = 'Air Conditioning')),
((SELECT id FROM places WHERE title = 'Desert Retreat in Arizona'), (SELECT id FROM amenities WHERE name = 'WiFi'));

-- @block
ALTER TABLE reviews MODIFY COLUMN rating FLOAT NOT NULL DEFAULT 0;
INSERT INTO reviews (id, owner_id, place_id, comment, created_at, updated_at) VALUES
(UUID(), (SELECT id FROM users WHERE email = 'john.doe@hbnb.io'), (SELECT id FROM places WHERE title = 'Cozy Apartment in NYC'), 'Great place, I cant believe this used to be a meth house!', NOW(), NOW()),
(UUID(), (SELECT id FROM users WHERE email = 'alice.wonder@hbnb.io'), (SELECT id FROM places WHERE title = 'Beach House in Miami'), 'Great place! I wonder if its going to be featured in GTA 6!!', NOW(), NOW()),
(UUID(), (SELECT id FROM users WHERE email = 'maestropanadero96@hbnb.io'), (SELECT id FROM places WHERE title = 'Cabin in the Woods'), 'Smells nice in the morning, avoid the guy with a chainsaw', NOW(), NOW()),
(UUID(), (SELECT id FROM users WHERE email = 'redrogsoviet@hbnb.io'), (SELECT id FROM places WHERE title = 'Modern Loft in San Francisco'), 'Great place, you almost forget about all the junkies in the street', NOW(), NOW()),
(UUID(), (SELECT id FROM users WHERE email = 'minecraft6969@hbnb.io'), (SELECT id FROM places WHERE title = 'Villa in Tuscany'), 'Absolutely stunning villa!', NOW(), NOW()),
(UUID(), (SELECT id FROM users WHERE email = 'admin@hbnb.io'), (SELECT id FROM places WHERE title = 'Penthouse in Tokyo'), 'Tokyo sucks!!!', NOW(), NOW()),
(UUID(), (SELECT id FROM users WHERE email = 'john.doe@hbnb.io'), (SELECT id FROM places WHERE title = 'Cottage in the Cotswolds'), 'Charming and cozy, perfect for a weekend getaway.', NOW(), NOW()),
(UUID(), (SELECT id FROM users WHERE email = 'alice.wonder@hbnb.io'), (SELECT id FROM places WHERE title = 'Lake House in Canada'), 'Beautiful location and very serene.', NOW(), NOW()),
(UUID(), (SELECT id FROM users WHERE email = 'maestropanadero96@hbnb.io'), (SELECT id FROM places WHERE title = 'Desert Retreat in Arizona'), 'I got bitten by a snake right on the tip of my dick, thankfully my mom sucked the venom out! she saves my life bro!!:D', NOW(), NOW());

-- -- @block
-- CREATE OR REPLACE VIEW place_amenities_view AS
-- SELECT
--     p.id AS place_id,
--     p.title AS place_title,
--     a.name AS amenity_name
-- FROM
--     places p
-- JOIN
--     place_amenities pa ON p.id = pa.place_id
-- JOIN
--     amenities a ON pa.amenity_id = a.id;

-- -- @block
-- CREATE OR REPLACE VIEW place_reviews_view AS
-- SELECT
--     p.id AS place_id,
--     p.title AS place_title,
--     r.rating AS review_rating,
--     r.comment AS review_comment
-- FROM
--     places p
-- JOIN
--     reviews r ON p.id = r.place_id;