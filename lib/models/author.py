from lib.db.connection import get_connection
from lib.models.article import Article


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name


    @classmethod
    def create(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        author_id =cursor.lastrowid
        conn.close()
        return cls(author_id, name)
    

    @classmethod
    def find_by_id(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["id"], row["name"]) if row else None
    
    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(row["id"], row["title"], row["author_id"], row["magazine_id"]) for row in rows]
    
    def magazines(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT DISTINCT m.* FROM magazines m JOIN articles a ON m.id = a.magazine_id WHERE a.author_id = ?""", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(row["id"], row["name"], row["category"]) for row in rows]
    

    def add_article(self, magazine, title):
        return Article.create(title, self.id, magazine.id)
    
    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT DISTINCT m.category  FROM magazines m JOIN articles a ON m.id = a.magazine_id WHERE a.author_id = ?""", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [row["category"] for row in rows]