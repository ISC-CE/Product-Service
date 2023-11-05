Prerequisite - Python3 or higher 

1. Clone the git repository to your local machine
2. Go to product-service directory
3. Create and activate python virtual environment
    python3 -m venv venv

    To activate your virtual environment,
        In Windows: 
            venv\Scripts\activate
        In Mac:
            source venv/bin/activate
4. Install dependencies:
    pip3 install -r requirements.txt 
5. Run the Server:
    python3 manage.py runserver
6. Test with Postman:
    localhost:8000/api/Product

API documentation:

1. Product:

        {
            "product_name": "Sample Product",
            "product_description": "This is a sample Product",
            "price": "1.00",
            "stock_quantity": 1
        }

2. ProductImage:

        {
            "image_url": "https://m.media-amazon.com/images/I/612yrAXpo-L._AC_UY218_.jpg",
            "created_at": null,
            "product": 1
        }

3. ProductReview:

        {
            "user_id": null,
            "rating": 4,
            "review_title": "Test Review",
            "review_text": "Sample Review",
            "product": 3
        }


