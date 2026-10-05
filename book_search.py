# book_search.py (Student A - Issue #1)
#this is the list of books!!
BOOKS = [
    {"title": "Software Engineering", "author": "Ian Sommerville"},
    {
        "title": "Software Engineering: A Practitioner's Approach",
        "author": "Roger Pressman",
    },
    {"title": "Clean Code", "author": "Robert C. Martin"},
]


def search_books(keyword, books=BOOKS):
    """Return books whose title or author contains the keyword (case-insensitive)."""
    if not keyword or not keyword.strip():
        raise ValueError("Keyword cannot be empty")

    k = keyword.strip().lower()
    return [
        b
        for b in books
        if k in b["title"].lower() or k in b["author"].lower()
    ]
