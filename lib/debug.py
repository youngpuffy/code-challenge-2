from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def debug():
    author = Author.find_by_id(1)
    if author:
        print(f"Author.{author.name}")

        print("\nArticles")
        for article in author.articles():
            print(f"- {article.title}")

        print("\nMagazines.")
        for magazine in author.magazines():
            print(f"{magazine.name}")


if __name__ == "__main__":
    debug()