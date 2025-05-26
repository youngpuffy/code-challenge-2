from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def run():
    author1 = Author.create("turi vile")
    author2 = Author.create("esther wakini")
    author3 = Author.create("rebecca wangari")

    mag1 = Magazine.create("tech today", "technology")
    mag2 = Magazine.create("health weekly", "health")

    article1 = author1.add_article(mag1, "the future of ai")
    article2 = author1.add_article(mag2, "wellness in 2024")
    article3 = author1.add_article(mag1, "cybersecurity basics")
    article4 = author1.add_article(mag1, "cloud computing")


    print(f"Articles by {author1.name}")
    for article in author1.articles():
        print(f"- {article.title} (Magazine ID: {article.magazine_id})")


    print(f"\nMagazines {author1.name} has contributed to:")
    for mag in author1.magazines():
        print(f"- {mag.name} ({mag.category})")

    print(f"\nContributors to {mag1.name}:")
    for contributor in mag1.contributors():
        print(f"- {contributor.name}")
    
    print(f"\nAuthors contributing more than 2 articles to {mag1.name}:")
    for author in mag1.contributing_authors():
        print(f"- {author.name}")

    print(f"\nArticle title in {mag2.name}:")
    for title in mag2.article_titles():
        print(f"- {title}")

    top_mag = Magazine.top_publisher()
    if top_mag:
        print(f"\nTop publishing magazine: {top_mag.name} ({top_mag.category})")


if __name__ == "__main__":
    run()

    