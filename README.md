
# Travel Blog Django Project

This is a travel blog application built with Django. The project allows users to share their travel experiences through blog posts. The application is equipped with an API and a serializer for managing blog content.

## Requirements

- Python 3.x
- Django==5.1.7
- asgiref==3.8.1
- pillow==11.2.0
- sqlparse==0.5.3
- tzdata==2025.2

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/travel-blog.git
   cd travel-blog
Create a virtual environment:
bash
python -m venv env
Activate the virtual environment:
On Windows:
bash
.\env\Scripts\activate
On macOS/Linux:
bash
source env/bin/activate

Install the required packages:
bash
pip install -r requirements.txt
Apply migrations:

This will create the necessary database tables, including the auth_user table for user authentication.

bash
python manage.py migrate
Create a superuser (optional):

If you want to access the Django admin panel, you can create a superuser account:

bash
python manage.py createsuperuser
Run the development server:

Start the development server to see the project in action:

bash
python manage.py runserver

The application will be available at http://127.0.0.1:8000/.

Features
Blog posts: Users can create, update, and delete travel blog posts.

API: The project includes a REST API to manage blog content. The API is serialized for easy data exchange.

Authentication: Users can log in, register, and manage their accounts.

API Endpoints
GET /api/posts/: List all blog posts.

POST /api/posts/: Create a new blog post.

GET /api/posts/{id}/: Retrieve a specific blog post.

PUT /api/posts/{id}/: Update a blog post.

DELETE /api/posts/{id}/: Delete a blog post.

License
This project is licensed under the MIT License - see the LICENSE file for details.
