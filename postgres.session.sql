-- Create Cuisine table
CREATE TABLE Cuisine (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

INSERT INTO Cuisine (name) VALUES 
    ('Indian'),
    ('Thai'),
    ('Italian');

-- Create Category table
CREATE TABLE Category (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

-- Insert sample categories
INSERT INTO Category (name) VALUES 
    ('Appetizer'),
    ('Dessert'),
    ('Main Dish'),
    ('Drink'); -- Add more categories as needed

-- Create MenuItems table
CREATE TABLE MenuItems (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    spicy_level INTEGER,
    category_id INTEGER REFERENCES Category(id),
    cuisine_id INTEGER REFERENCES Cuisine(id),
    CONSTRAINT fk_category
        FOREIGN KEY (category_id)
        REFERENCES Category (id),
    CONSTRAINT fk_cuisine
        FOREIGN KEY (cuisine_id)
        REFERENCES Cuisine (id)
);

--Food
INSERT INTO MenuItems (title, description, price, spicy_level, category_id, cuisine_id)
VALUES
    ('Paneer Tikka', 'Marinated and grilled cottage cheese', 10.99, 2, 1, 1),
    ('Tom Yum Soup', 'Spicy Thai soup with shrimp and herbs', 8.75, 3, 1, 2),
    ('Margherita Pizza', 'Classic Italian pizza with tomato and mozzarella', 12.50, 1, 3, 3),
    ('Samosa', 'Deep-fried pastry filled with spiced potatoes and peas', 5.99, 2, 1, 1),
    ('Pad Thai', 'Stir-fried Thai noodles with shrimp and peanuts', 9.50, 4, 1, 2),
    ('Ravioli al Funghi', 'Italian mushroom-filled pasta with cream sauce', 14.25, 2, 3, 3),
    ('Gulab Jamun', 'Indian sweet dumplings in sugar syrup', 6.99, 1, 2, 1),
    ('Green Curry', 'Thai green curry with chicken and vegetables', 11.50, 3, 3, 2),
    ('Lasagna', 'Layered Italian pasta with meat and cheese', 13.75, 2, 3, 3),
    ('Chicken Tikka Masala', 'Indian spiced chicken in creamy tomato sauce', 12.99, 3, 3, 1),
    ('Tiramisu', 'Classic Italian coffee-flavored dessert', 7.50, 1, 2, 3),
    ('Spring Rolls', 'Crispy Thai spring rolls with vegetables and shrimp', 8.25, 2, 1, 2),
    ('Caprese Salad', 'Italian salad with tomatoes, mozzarella, and basil', 9.99, 1, 1, 3),
    ('Mango Sticky Rice', 'Thai dessert with sweet sticky rice and mango', 6.50, 1, 2, 2),
    ('Chole Bhature', 'Indian chickpea curry with fried bread', 11.25, 2, 3, 1);

-- Drinks
INSERT INTO MenuItems (title, description, price, spicy_level, category_id, cuisine_id)
VALUES
    ('Iced Coffee', 'Chilled coffee served with ice', 4.50, NULL, 4, 3),
    ('Mojito', 'Refreshing lime and mint cocktail', 6.75, NULL, 4, 2),
    ('Lemonade', 'Classic freshly squeezed lemonade', 3.99, NULL, 4, 1),
    ('Smoothie', 'Mixed fruit smoothie', 5.25, NULL, 4, 2),
    ('Soda', 'Assorted sodas', 2.50, NULL, 4, 1),
    ('Mocktail', 'Non-alcoholic mixed drink', 4.99, NULL, 4, 3),
    ('Iced Tea', 'Chilled sweetened tea', 3.75, NULL, 4, 1),
    ('Cappuccino', 'Italian coffee with equal parts espresso, steamed milk, and milk foam', 5.50, NULL, 4, 3),
    ('Hot Chocolate', 'Warm chocolate drink topped with whipped cream', 4.25, NULL, 4, 3),
    ('Fruit Punch', 'Mixed fruit punch', 4.75, NULL, 4, 2),
    ('Lime Soda', 'Carbonated lime-flavored drink', 3.25, NULL, 4, 1),
    ('Mango Lassi', 'Indian mango yogurt drink', 5.99, NULL, 4, 1),
    ('Iced Green Tea', 'Chilled green tea with ice', 3.50, NULL, 4, 2),
    ('Sparkling Water', 'Fizzing sparkling water', 2.75, NULL, 4, 1),
    ('Hot Tea', 'Steaming cup of hot tea', 3.25, NULL, 4, 2);
