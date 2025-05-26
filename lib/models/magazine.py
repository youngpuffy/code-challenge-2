from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.author import Author

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category =category


    @classmethod
    def create(cls, name, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        magazine_id = cursor.lastrowid
        conn.close()
        return cls(magazine_id, name, category)
    

    @classmethod
    def find_by_id(cls, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["id"], row["name"], row["category"]) if row else None
    
    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id))
        rows = cursor.fetchall()
        conn.close()
        return [Article(row["id"], row["title"], row["author_id"], row["magazine_id"]) for row in rows]
    
    def contributors(self):
        from lib.models.author import Author

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT DISTINCT a.* FROM authors a JOIN articles ar ON a.id = ar.author_id WHERE ar.magazine_id = ?""", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(row["id"], row["name"]) for row in rows]
    

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [row["title"] for row in rows]
    
    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT a.*, COUNT(ar.id) as article_count FROM authors a JOIN articles ar ON a.id = ar.author_id WHERE ar.magazine_id = ? GROUP BY a.id HAVING article_count > 2""", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(row["id"], row["name"]) for row in rows]
    
    @classmethod
    def top_publisher(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT m.*, COUNT(a.id) as article_count FROM magazines m JOIN articles a ON m.id = a.magazine_id GROUP BY m.id ORDER BY article_count DESC LIMIT 1""")
        row = cursor.fetchone()
        conn.close()
        return cls(row["id"], row["name"], row["category"]) if row else None