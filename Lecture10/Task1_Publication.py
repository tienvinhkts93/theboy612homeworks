class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication: {self.name}")

class Book(Publication):
    def __init__(self,name,author,page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Pages: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}\n")

Donal_Duck = Magazine("Donal Duck", "Aki Hyyppä")
Compartment = Book ("Compartment no.6","Rosa Liksom",192)

Donal_Duck.print_information()
Compartment.print_information()