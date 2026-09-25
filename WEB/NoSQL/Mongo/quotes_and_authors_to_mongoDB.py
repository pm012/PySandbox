# load_data.py
import json
import os
from dotenv import load_dotenv
from mongoengine import connect
from models import Author, Quote

load_dotenv()  # Load environment variables from .env file
# Replace with your actual MongoDB Atlas connection string
MONGO_URI = os.getenv("MONGO_URI")
authors_file = os.path.join(os.path.dirname(__file__), 'authors.json')
quotes_file = os.path.join(os.path.dirname(__file__), 'quotes.json')

def import_data():
    # 1. Connect to MongoDB Atlas
    connect(host=MONGO_URI)

    # Clear existing collections to avoid duplicates on re-runs
    Author.objects.delete()
    Quote.objects.delete()

    # 2. Load and insert Authors
    with open(authors_file, 'r', encoding='utf-8') as f:
        authors_data = json.load(f)
        for data in authors_data:
            author = Author(
                fullname=data.get('fullname'),
                born_date=data.get('born_date'),
                born_location=data.get('born_location'),
                description=data.get('description')
            )
            author.save()

    print("Authors successfully imported.")

    # 3. Load and insert Quotes
    with open(quotes_file, 'r', encoding='utf-8') as f:
        quotes_data = json.load(f)
        for data in quotes_data:
            # Find the referenced author document by name
            author_obj = Author.objects(fullname=data.get('author')).first()
            if author_obj:
                quote = Quote(
                    tags=data.get('tags', []),
                    author=author_obj,  # Stores the ObjectId reference automatically
                    quote=data.get('quote')
                )
                quote.save()

    print("Quotes successfully imported.")

if __name__ == '__main__':
    import_data()