#!C:\Users\krist\AppData\Local\Programs\Python\Python38-32\python.exe
#import modules for CGI and pymysql handling
import cgi, pymysql
#part of HTTP header which is sent to the browser to understand the content
print("Content-type:text/html\r\n\r\n")
print("""<!DOCTYPE html>
<html>
  <head>
    <title>Registered Students</title>
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
      width: 75%;
      border: 10px solid white;
      padding: 60px;
      margin: auto;
    }
    table, th, td { 
      width: 100%;
      border: 2px solid white;
      border-collapse: collapse;     
    }
    th, td {
      width: 10px;
    }
    th {
      font-size: 18px;
    }
    p {
      text-align: center;
    }
    a {
      color:yellow;
    }
    a:hover {
      color: blue;
    }
  </style>
    
  <body>
    <div>
      <h1>REGISTERED STUDENTS</h1><hr>
""")

print("<table>")

print("""
    <tr>
    <th>ID</th>
    <th>Student Number</th>
    <th>Last Name</th>
    <th>First Name</th>
    <th>Middle Name</th>
    <th>Birthday</th>
    <th>Age</th>
    <th>Address</th>
    <th></th>
    </tr>
""")
#open database connection; "dbstudent" database in phpmyadmin
db = pymysql.connect("localhost","root","","dbstudent") 
#prepare a cursor object using cursor() method
cursor = db.cursor() 
#prepare SQL query to SELECT from tblstudent
sql = """SELECT * FROM tblstudent""" 
#execute SQL command
cursor.execute(sql) 
#fetch all the rows in a list of lists
result = cursor.fetchall() 
#disconnect from server
db.close()
#loop to access the data in result
for row in result:
    id = row[0]
    StudentNo = row[1]
    Lastname = row[2]
    Firstname = row[3]
    Middlename = row[4]
    Birthday = row[5]
    age = row[6]
    address = row[7]
    print("""
        <tr>
        <td>%d</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%d</td>
        <td>%s</td>
        <td>
        <a href="editstudent.py?id=%s">Edit</a>
        <a href="deletestudent.py?id=%s">Delete</a>
        </td>
        </tr>
        """ %(id,StudentNo,Lastname,Firstname,Middlename,Birthday,age,address,id,id))    

print("</table>")
#hyperlink redirect to createstudent.py to register another student
print("<p><a href='createstudent.py' style='font-size:20px'>Register Another Student</a></p>")
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
#*28 - table, table header, table cell style
#*29 - table, th, td width size
#*30 - table, th, td border size and color
#*31 - border collapse so no space between border
#*33 - table header, table cell style
#*34 - th, td width size
#*36 - table header style
#*37 - th font size
#*39 - paragraph style
#*40 - center align the text for paragraph
#*42 - a(hyperlink) style
#*43 - hyperlink color
#*45 - hyperlink hover style
#*46 - hyperlink color
#*48 - end tag for style

#*50 - start tag for body
#*51 - start tag for div; section in a document
#*52 - contains HTML heading
#*53 - close the print

#*55 - create table for organization of data

#Label in first row define what data below it
#*57 - print as multiline docstring
#*58 - table row st
#*59 - table header contains ID
#*60 - th contains Student Number
#*61 - th contains Last Name
#*62 - th contains First Name
#*63 - th contains Middle Name
#*64 - th contains Birthday
#*65 - th contains Age
#*66 - th contains Address
#*67 - th contains nothing
#*68 - table row et
#*69 - close print

#*71 - open database connection; "dbstudent" database in phpmyadmin
#*73 - prepare a cursor object using cursor() method
#*75 - prepare SQL query to SELECT from tblstudent
#*77 - execute SQL command

#*79 - fetch all the rows in a list of lists
#*81 - disconnect from server
#loop to access the data in result
#*83 - for in loop to get the data from the result
#*84 - get id from row in result
#*85 - get StudentNo from row in result
#*86 - get Lastname from row in result
#*87 - get Firstname from row in result
#*88 - get Middlename from row in result
#*89 - get Birthday from row in result
#*90 - get Age from row in result
#*91 - get Address from row in result
#*92 - print inside the loop
#*93 - table row st
#*94 - table cell contains placeholder for id
#*95 - table cell contains placeholder for StudentNo
#*96 - table cell contains placeholder for Lastname
#*97 - table cell contains placeholder for Firstname
#*98 - table cell contains placeholder for Middlename
#*99 - table cell contains placeholder for Birthday
#*100 - table cell contains placeholder for Age
#*101 - table cell contains placeholder for Address
#*102 - table cell st
#*103 - hyperlink redirect to editstudent.py
#*104 - hyperlink redirect to deletestudent.py
#*105 - table cell et
#*106 - table row et
#*107 - variables to insert in values placeholder
#*109 - table et
#*111 - hyperlink redirect to createstudent.py to register another student

#end tags of HTML
#*113 - print as multiline docstring
#*114 - div et
#*115 - body et
#*116 - html et
#*117 - close the print