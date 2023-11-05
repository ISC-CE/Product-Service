CREATE TABLE product (
  product_id INT PRIMARY KEY AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT CHECK (stock_quantity >= 0) NOT NULL DEFAULT = 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE product_images (
  image_id INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT,
  image_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE product_reviews (
  review_id INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT,
  user_id = INT CHECK (user_id >= 0) NOT NULL DEFAULT = 0,
  rating INT CHECK (rating >= 0),
  review_title TEXT,
  review_text TEXT,
  review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES product (product_id)
);




















