import sqlite3

A = sqlite3.connect('Database.db') #creation of variable 'A' as shortform to connect to database "Database.db'

with A: #opens connection to database
    B = A.cursor() #variable 'B' for short form to utilize 'A.cursor()' 
    B.execute("CREATE TABLE IF NOT EXISTS tbl_file(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )") #creation of table in database with associated column
    A.commit() #commits the changes to the database
A.close() #always ensure to close connection to avoid data leaks

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

A = sqlite3.connect('Database.db')

with A:
    B = A.cursor()
    for file in fileList:
        if file.endswith('.txt'):
            B.execute("INSERT INTO tbl_file(col_fname) VALUES(?)", (file,))
            print (file)
            A.commit()
A.close()
                      
              
