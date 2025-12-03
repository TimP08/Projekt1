class Book:
    def __init__(self, title, author, borrowed,):
        self.title = title
        self.author = author
        self.borrowed = bool(int(borrowed))


    def __str__(self):
        return f"{self.title}, {self.author}, {self.borrowed}"

    def to_file_line(self):
        return f"{self.title}, {self.author}, {int(self.borrowed)}"