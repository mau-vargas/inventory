-- Create role if not exists
DO $$ BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'admin_user') THEN
        CREATE ROLE admin_user WITH LOGIN PASSWORD 'admin_password';
    END IF;
END $$;

-- Create database if not exists
DO $$ BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'inventory_db') THEN
        CREATE DATABASE inventory_db WITH OWNER admin_user;
    END IF;
END $$;

-- Connect to the newly created database
\c inventory_db;

-- Create table if not exists
CREATE TABLE IF NOT EXISTS inventory (
    product_id SERIAL PRIMARY KEY,
    code INT,
    name_product VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    available_quantity INT NOT NULL,
    unit_price VARCHAR(50) NOT NULL,
    supplier VARCHAR(50) NOT NULL,
    entry_date VARCHAR(50) NOT NULL,
    update_date VARCHAR(50) NOT NULL,
    detail VARCHAR(255) NOT NULL
);

-- Show tables to verify successful creation
\dt

-- Insert data into the inventory table
INSERT INTO inventory (code, name_product, category, available_quantity, unit_price, supplier, entry_date, update_date, detail) 
VALUES (1, 'Tornillo Phillips de 3/4 pulgada', 'Materiales de fijación', '500', '10', 'Ferretería González', '10-06-23', '10-06-23', 'Tornillo de cabeza Phillips con rosca de 3/4 de pulgada de longitud.');
