# Clone the repository
git clone url

# Navigate to the project directory
cd BOOKREVIEWSYSTEM
# Create a virtual environment (optional but recommended)
python -m venv envbook

# Activate the virtual environment (Windows)
.\envbook\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser account for administrative access
python manage.py createsuperuser

# Start the development server
python manage.py runserver

Certainly! Here are the API endpoints for your Book Review System:

### Books

- **List Books:**
  - Method: GET
  - Endpoint: [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/)

- **Create Book:**
  - Method: POST
  - Endpoint: [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/)

### Reviews

- **List Reviews:**
  - Method: GET
  - Endpoint: [http://127.0.0.1:8000/reviews/](http://127.0.0.1:8000/reviews/)

- **Create Review:**
  - Method: POST
  - Endpoint: [http://127.0.0.1:8000/reviews/](http://127.0.0.1:8000/reviews/)

Feel free to copy and paste these URLs. Make sure your development server is running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for these endpoints to work.

Certainly! Here are example URLs for your Django app with the implemented filters:

### Filter Books by Author

```bash
curl http://127.0.0.1:8000/books/?author=YourAuthorName
```

Replace `YourAuthorName` with the desired author's name.

### Filter Books by Publication Year

```bash
curl http://127.0.0.1:8000/books/?publication_year=2022
```

Replace `2022` with the desired publication year.

### Filter Reviews by Book Title

```bash
curl http://127.0.0.1:8000/reviews/?book=YourBookTitle
```

Replace `YourBookTitle` with the desired book title.

