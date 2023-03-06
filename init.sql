CREATE TABLE IF NOT EXISTS Categories(
    id BIGSERIAL PRIMARY KEY,
    category_name VARCHAR(32)
);

CREATE TABLE IF NOT EXISTS Products(
    id SERIAL PRIMARY KEY,
    category_id BIGSERIAL,
    product_name VARCHAR(255),
    product_description VARCHAR(255),
    product_price BIGSERIAL
);