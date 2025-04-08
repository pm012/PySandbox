from typing import List, Dict, Union

def find_articles(articles: List[Dict[str, Union[str, int]]], key: str, case_sensitive: bool = False) -> List[Dict]:
    """
    Searches for articles by title or author containing the given key.
    
    :param articles: List of articles (dictionaries with title, author, year).
    :param key: Search key (substring to match).
    :param case_sensitive: Whether the search should be case sensitive (default False).
    :return: List of matching articles.
    """
    if not case_sensitive:
        key = key.lower()  # Normalize the search key
    
    # Use list comprehension for a cleaner approach
    return [
        article
        for article in articles
        if (key in article["title"] if case_sensitive else key in article["title"].lower()) or
           (key in article["author"] if case_sensitive else key in article["author"].lower())
    ]


if __name__ == "__main__":
    articles_dict = [
        {
            "title": "Endless ocean waters.",
            "author": "Jhon Stark",
            "year": 2019,
        },
        {
            "title": "Oceans of other planets are full of silver",
            "author": "Artur Clark",
            "year": 2020,
        },
        {
            "title": "An ocean that cannot be crossed.",
            "author": "Silver Name",
            "year": 2021,
        },
        {
            "title": "The ocean that you love.",
            "author": "Golden Gun",
            "year": 2021,
        },
    ]
    
    while True:
        case = input("Enter case: 's' - case sensitive, 'i' - case insensitive (or 'exit' to quit): ").lower()
        if case == "exit":
            break
        elif case not in ("s", "i"):
            print("Invalid choice. Please try again.")
            continue
        
        case_sensitive = case == "s"
        search_key = input("Enter the search key (or 'exit' to quit): ")
        if search_key.lower() == "exit":
            break
        
        results = find_articles(articles_dict, search_key, case_sensitive)
        print(f"\nSearch Results ({len(results)} found):")
        for article in results:
            print(f"- {article['title']} by {article['author']} ({article['year']})")
        print("\n")
