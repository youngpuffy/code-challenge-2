from lib.models.author import Author
from lib.models.magazine import Magazine


def seed_data():
    author1 = Author.create("levi muturi")
    author2 = Author.create("esther wakini")
    author3 = Author.create("rebecca wangari")
    print(f"created author: {author1.name}")


    mag1 = Magazine.create("tech today", "technology")
    mag2 = Magazine.create("health weekly", "Health")
    mag3 = Magazine.create("travel explorer", "travel")
    print(f"created magazines: {mag1.name}, {mag2.name}, {mag3.name}")

    author1.add_article(mag1, "AI in 2026")
    author1.add_article(mag1, "healthy living tips")
    author2.add_article(mag1, "quantum computing")
    author2.add_article(mag3, "top 10 destinations")
    author3.add_article(mag2, "nutrition facts")
    author3.add_article(mag2, "workout routines")
    author3.add_article(mag2, "mental health awareness")

    print("seed data added successfully.")

if __name__== "__main__":
    seed_data()