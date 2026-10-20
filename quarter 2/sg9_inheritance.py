#defining the program

class Publication:                           #defining parent class/library materials
    def __init__(self, title, author):      #defining its attributes
        self.title = str(title)
        self.author = str(author)
    def display_info(self):                  #displays basic info of the class
        print(f"""Title: {self.title}
Author(s): {self.author}""")
        
class Book(Publication):                    #defining child class BOOK  of library materials
    def __init__(self, title, author, num_of_pages):      #defining its attributes
        self.title = str(title)
        self.author = str(author)
        self.__num_of_pages = int(num_of_pages)
    def set_num_of_pages(self, num):        #sets the number of pages of a book to a non-negative and non-zero number
        if num <= 0:
            print("Invalid number of pages. The number of pages must be positive.")
        else:
            self.__num_of_pages = num
    def display_info(self):                  #displays basic info of the child class
        Publication.display_info(self)
        print("Number of pages: ", end=" ")
    def get_number_of_pages(self):            #makes the private attribute number of pages accessible to use
        return self.__num_of_pages

class Magazine(Publication):                    #defining child class MAGAZINE of library materials
    def __init__(self, title, author, issue_number):      #defining its attributes
        self.title = str(title)
        self.author = str(author)
        self.__issue_number = int(issue_number)
    def display_info(self):                  #displays basic info of the child class
        Publication.display_info(self)
        print("Issue Number: ", end=" ")
    def get_issue_number(self):            #makes the private attribute number of pages accessible to use
        return self.__issue_number

#program proper

#defining and giving the object attributes their value
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#prints pub1 publication material and displays its information (name, author)
print("Publication Information: ")
pub1.display_info()

#prints book1 child BOOK publication material and displays its information (name, author, number of pages)
print("\nBook Information: ")
book1.set_num_of_pages(-310)            #tries to set a new number as the object's number of pages
book1.display_info()
print(book1.get_number_of_pages())        #prints private attribute number of pages

#prints mag1 child MAGAZINE publication material and displays its information (name, author, issue number)
print("\nMagazine Information: ")
mag1.display_info()
print(mag1.get_issue_number())          #prints private attribute issue number
