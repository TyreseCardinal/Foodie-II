-- Insert sample data into client
INSERT INTO client (username, password, email, first_name, last_name) VALUES
('john_doe', 'hashed_password1', 'john.doe@example.com', 'John', 'Doe'),
('jane_smith', 'hashed_password2', 'jane.smith@example.com', 'Jane', 'Smith');

-- Insert sample data into restaurant
INSERT INTO restaurant (name, address, phone, email) VALUES
('The Great Restaurant', '123 Food Street, Flavor Town', '555-1234', 'contact@greatrestaurant.com'),
('Bistro Delights', '456 Culinary Road, Taste City', '555-5678', 'info@bistrodelights.com');

-- Insert sample data into menu_item
INSERT INTO menu_item (restaurant_id, name, description, price) VALUES
(1, 'Cheeseburger', 'A juicy cheeseburger with all the fixings.', 9.99),
(1, 'Caesar Salad', 'Fresh Caesar salad with homemade dressing.', 7.99),
(2, 'Spaghetti Bolognese', 'Traditional Italian pasta with a rich meat sauce.', 11.99),
(2, 'Tiramisu', 'Classic Italian dessert with coffee and mascarpone.', 6.99);

-- Insert sample data into order
INSERT INTO `order` (client_id, restaurant_id, status) VALUES
(1, 1, 'Pending'),
(2, 2, 'Completed');

-- Insert sample data into order_menu_item
INSERT INTO order_menu_item (order_id, menu_item_id, quantity, price) VALUES
(1, 1, 2, 19.98),
(1, 2, 1, 7.99),
(2, 3, 1, 11.99),
(2, 4, 1, 6.99);
