class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type


# Dictionaries to store data
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 45},
    {"name": "Monitor", "price": 200},
    {"name": "Headset", "price": 80}
]

employees = [
    {"name": "Alice", "job_title": "Developer"},
    {"name": "Bob", "job_title": "Designer"},
    {"name": "Charlie", "job_title": "Manager"},
    {"name": "Diana", "job_title": "HR Specialist"},
    {"name": "Eve", "job_title": "Intern"}
]

books = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Moby Dick", "author": "Herman Melville"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"}
]

universities = [
    {"name": "MIT", "location": "Cambridge, MA"},
    {"name": "Harvard", "location": "Cambridge, MA"},
    {"name": "Stanford", "location": "Stanford, CA"},
    {"name": "UC Berkeley", "location": "Berkeley, CA"},
    {"name": "Caltech", "location": "Pasadena, CA"}
]

restaurants = [
    {"name": "Chez Panisse", "cuisine_type": "French"},
    {"name": "Pizzeria Bianco", "cuisine_type": "Italian"},
    {"name": "Nobu", "cuisine_type": "Japanese"},
    {"name": "Joe's BBQ", "cuisine_type": "Barbecue"},
    {"name": "Gjelina", "cuisine_type": "Californian"}
]

# Access and print product details
print("Products:")
for product in products:  # Iterate through the list of dictionaries
    print(f"Name: {product['name']}, Price: ${product['price']}")

# Access and print employee details
print("\nEmployees:")
for employee in employees:
    print(f"Name: {employee['name']}, Job Title: {employee['job_title']}")

# Access and print book details
print("\nBooks:")
for book in books:
    print(f"Title: {book['title']}, Author: {book['author']}")

# Access and print university details
print("\nUniversities:")
for university in universities:
    print(f"Name: {university['name']}, Location: {university['location']}")

# Access and print restaurant details
print("\nRestaurants:")
for restaurant in restaurants:
    print(f"Name: {restaurant['name']}, Cuisine: {restaurant['cuisine_type']}")
