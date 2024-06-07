import beerpy as bp

if __name__ == "__main__":
    print(bp.get_language_list())
    print(bp.get_author_list())
    print(bp.get_author_list("eng"))
    print(bp.get_random_quote())
    print(bp.get_quotes_from_author("chatgpt", language="eng"))
    print(bp.get_random_quote_from_author("chatgpt", language="eng"))