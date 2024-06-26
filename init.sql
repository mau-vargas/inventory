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
VALUES (1, 'Tornillo Phillips de 3/4 pulgada', 'Materiales de fijación', '500', '10', 'Ferretería González', '10-06-23', '10-06-23', 'Tornillo de cabeza Phillips con rosca de 3/4 de pulgada de longitud.'),
(2, 'Martillo de carpintero', 'Herramientas', '150', '120', 'Herramientas López', '11-06-23', '11-06-23', 'Martillo de carpintero con mango de madera y cabeza de acero.'),
(3, 'Taladro eléctrico 500W', 'Herramientas eléctricas', '75', '950', 'Eléctricos S.A.', '12-06-23', '12-06-23', 'Taladro eléctrico de 500W con control de velocidad y función de impacto.'),
(4, 'Llave inglesa ajustable', 'Herramientas', '200', '80', 'Ferretería Central', '13-06-23', '13-06-23', 'Llave inglesa ajustable de 10 pulgadas con mango antideslizante.'),
(5, 'Cinta métrica de 5 metros', 'Medición', '300', '50', 'Mediciones Precisas', '14-06-23', '14-06-23', 'Cinta métrica de 5 metros con carcasa de plástico resistente.'),
(6, 'Destornillador plano de 6 pulgadas', 'Herramientas', '250', '20', 'Herramientas López', '15-06-23', '15-06-23', 'Destornillador plano de 6 pulgadas con mango ergonómico.'),
(7, 'Caja de clavos de 2 pulgadas', 'Materiales de fijación', '5000', '5', 'Ferretería González', '16-06-23', '16-06-23', 'Caja de clavos de 2 pulgadas para carpintería y construcción.'),
(8, 'Sierra circular de 1400W', 'Herramientas eléctricas', '60', '1200', 'Eléctricos S.A.', '17-06-23', '17-06-23', 'Sierra circular de 1400W con disco de corte de 7 pulgadas.'),
(9, 'Juego de llaves Allen', 'Herramientas', '180', '100', 'Herramientas López', '18-06-23', '18-06-23', 'Juego de llaves Allen de diversos tamaños en estuche portátil.'),
(10, 'Pintura acrílica blanca 1L', 'Pinturas', '250', '150', 'Pinturas y Decoración', '19-06-23', '19-06-23', 'Pintura acrílica blanca de 1 litro para interiores y exteriores.'),
(11, 'Cerradura de seguridad', 'Herrajes', '100', '300', 'Ferretería Central', '20-06-23', '20-06-23', 'Cerradura de seguridad para puerta principal con 3 llaves.');
