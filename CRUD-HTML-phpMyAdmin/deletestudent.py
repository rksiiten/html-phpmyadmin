#!C:\Users\krist\AppData\Local\Programs\Python\Python38-32\python.exe
#import modules for CGI and pymysql handling
import cgi, pymysql
#part of HTTP header which is sent to the browser to understand the content
print("Content-type:text/html\r\n\r\n")
print("""<!DOCTYPE html>            
<html>                              
  <head>                            
    <title>Delete</title>           
  </head>
                                    
  <style>                           
    h1 {
      text-align: center;           
    }
    body {
      background-image: url(https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700462770.jpg);
      font-family: Helvetica;
      color: #FFFFFF;
    }
    div {
      background-color: maroon;
      width: 50%;
      border: 10px solid white;
      padding: 50px;
      margin: auto;
    }
    p {
      text-align: center;
    }
    a {
      color: yellow;
      font-size: 20px;
    }
    a:hover {
      color: blue;
    }
  </style>

  <body>                            
    <div>                           
      <h1>STUDENT DELETED</h1><hr>  
""")
#create instance of FieldStorage
file = cgi.FieldStorage()
#get data from FieldStorage
#use only the id because id has the other info
id = file.getvalue("id")
#open database connection
#"dbstudent" database in phpmyadmin
db = pymysql.connect("localhost","root","","dbstudent")
#prepare a cursor object using cursor() method
cursor = db.cursor()
#prepare SQL query to DELETE required records
sql = """DELETE FROM tblstudent
        WHERE id=%s""" % (id)
#execute SQL command
cursor.execute(sql)
#commit changes
db.commit()
#disconnect from server
db.close()
#hyperlink redirect to readstudent.py
print("<p><a href='readstudent.py'>Back</a></p>")
#end tags of HTML
print("""
    </div>
  </body>
</html>
""")

#COMMENTS PER LINE:

#*1 - shell convention that tells the shell which program can execute the script
#*3 - import modules for CGI and pymysql handling
#*5 - part of HTTP header which is sent to the browser to understand the content
#*6 - print as multiline docstring; DOCTYPE html defines the document type
#*7 - start tag for html
#*8 - start tag for head
#*9 - this appear on tab
#*10 - end tag for head

#*12 - start tag for style; style information for a document
#*13 - h1 styl; HTML heading
#*14 - center align the text for h1
#*16 - body style
#*17 - bg image link that show in webpage
#*18 - Helvetica as font for the body
#*19 - color of text in body white
#*21 - div style
#*22 - bg color
#*23 - width of div section
#*24 - border size and color of div section
#*25 - padding size
#*26 - margin auto so it depends on the size of the page
#*28 - paragraph style
#*29 - center align the text for paragraph
#*31 - a(hyperlink) style
#*32 - hyperlink color
#*33 - hyperlink font size
#*35 - hyperlink hover style
#*36 - hyperlink color
#*38 - end tag for style

#*40 - start tag for body
#*41 - start tag for div; section in a document
#*42 - contains HTML heading
#*43 - close the print

#*45 - create instance of FieldStorage
#get data from FieldStorage; var inside () is from input name in editstudent.py
#*47 - get value for id
#*48 - get value for student number
#*49 - get value for last name
#*50 - get value for first name
#*51 - get value for middle name
#*52 - get value for birthday
#*53 - get value for age
#*54 - get value for address

#*56 - open database connection; "dbstudent" database in phpmyadmin
#*58 - prepare a cursor object using cursor() method
#*60 - prepare SQL query to UPDATE the tblstudent - table in dbstudent
#*61 - StudentNo var in phpmyadmin = placeholder
#*62 - Lastname var in phpmyadmin = placeholder
#*63 - Firstname var in phpmyadmin = placeholder
#*64 - Middlename var in phpmyadmin = placeholder
#*65 - Birthday var in phpmyadmin = placeholder
#*66 - age var in phpmyadmin = placeholder
#*67 - address var in phpmyadmin = placeholder
#*68 - WHERE - get specific record which is id that contains all info of one student
#*69 - variables to insert in values placeholder; variables from form in editstudent.py
#*71 - execute SQL command
#*73 - commit changes
#*75 - disconnect from server

#*77 - hyperlink redirect to readstudent.py

#end tags
#*79 - print as multiline docstring
#*80 - div et
#*81 - body et
#*82 - html et
#*82 - close the print