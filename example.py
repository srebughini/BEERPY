import beerpy as bp

if __name__ == "__main__":
    # Extract list of authors
    author_list = bp.get_author_list()

    # Extract a random quote
    random_quote = bp.get_random_quote(language="eng")

    # Extract quotes of a specific author
    author_quotes = bp.get_quotes_from_author("Benjamin Franklin")

    # Extract a random quote of a specific author
    random_author_quote = bp.get_random_quote_from_author("W. C. Fields")

    print("Author list:        ", author_list)
    print("Random quote:       ", random_quote)
    print("Author quotes:      ", author_quotes)
    print("Author random quote:", random_author_quote)