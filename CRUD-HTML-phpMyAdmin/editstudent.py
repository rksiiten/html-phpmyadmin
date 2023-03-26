#!C:\Users\krist\AppData\Local\Programs\Python\Python38-32\python.exe
#import modules for CGI and pymysql handling
import cgi, pymysql
#part of HTTP header which is sent to the browser to understand the content
print("Content-type:text/html\r\n\r\n")
print("""<!DOCTYPE html>            
<html>                              
  <head>                            
    <title>Edit Student</title>     
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
    table { 
      width: 100%;
    }
    th {
      width: 45%;
    }        
    p {
      text-align: right;
    }
  </style>
    
  <body>                            
    <div>                           
      <h1>EDIT STUDENT</h1><hr>     
""")
#create instance of FieldStorage
file = cgi.FieldStorage()
#get data from field
#use only the id because id has the other info
id = file.getvalue("id")
#open database connection
#"dbstudent" database in phpmyadmin
db = pymysql.connect("localhost","root","","dbstudent")
#prepare a cursor object using cursor() method
cursor = db.cursor()
#prepare SQL query to SELECT required records
sql = """SELECT * FROM tblstudent 
        WHERE id=%s""" % (id)
#execute SQL command
cursor.execute(sql)
#fetch a single row using fetchone() method
#instead of just one variable put all the variables so no need for for loop
#applicable only for fetching single row
id,StudentNo,Lastname,Firstname,Middlename,Birthday,age,address = cursor.fetchone()
#disconnect from server
db.close()
#form action-where to send; method when sending; post-inputdata dont show in url
print("""
<form action="updatestudent.py" method="post">      
    
  <input name="id" type="hidden" value="%s">        
  
  <table>                                           
    <tr>                                            
      <th>                                          
        <p><b>Student Number: </b></p>              
      </th>                                         
      <td>&emsp;&emsp;                              
        <input name="stnum" type="text" value="%s">
      </td>
    </tr>
    
    <tr>
      <th>
        <p><b>Last Name: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="lname" type="text" value="%s">
      </td>
    </tr>
    
    <tr>
      <th>
        <p><b>First Name: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="fname" type="text" value="%s">
      </td>
    </tr>
    
    <tr>
      <th>
        <p><b>Middle Name: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="mname" type="text" value="%s">
      </td>
    </tr>

    <tr>
      <th>
        <p><b>Birthday: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="bday" type="date" value="%s">
      </td>
    </tr>

    <tr>
      <th>
        <p><b>Age: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="age" type="number" value="%s">
      </td>
    </tr>

    <tr>
      <th>
        <p><b>Address: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="address" type="text" value="%s">
      </td>
    </tr>
  </table>
    
  <p style="text-align:center"><input type="submit" value="SUBMIT"></p>
     
""" % (id,StudentNo,Lastname,Firstname,Middlename,Birthday,age,address))
#placeholders for substituting the value in string
#use values so the info given in createstudent.py will remain in the form

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
#*28 - table style
#*29 - table width size
#*31 - table header style
#*32 - table header width size
#*34 - paragraph style
#*35 - center align the text for paragraph
#*37 - end tag for style

#*39 - start tag for body
#*40 - start tag for div; section in a document
#*41 - contains HTML heading
#*42 - close the print

#*44 - create instance of FieldStorage
#*47 - get data from field; id only because it contains other info
#*50 - open database connection; "dbstudent" database in phpmyadmin
#*52 - prepare a cursor object using cursor() method
#*54 - prepare SQL query to SELECT from tblstudent
#*55 - WHERE is to get only specific record
#*57 - #execute SQL command
#*61 - fetch a single row using fetchone() method; single row only; put all the variables so no need for for loop
#*63 - disconnect from server

#*65 - print as multiline docstring
#*66 - form action-define where to send; method-HTTP method to use when sending; post-entered data dont show in url; this is where user input data
#*68 - hide input id because it only needs as variable

#*70 - start tag for table; create a table; for organization of data
#*71 - table row st(start tag)
#*72 - table heading st
#*73 - label for Student Number
#*74 - table heading end tag(et)
#*75 - table cell st; &emps; - tab
#*76 - field to enter data; name - variable for student number; type - text as input type
#*77 - table cell et
#*78 - table row et

#*80 - table row st(start tag)
#*81 - table heading st
#*82 - label for Last Name
#*83 - table heading end tag(et)
#*84 - table cell st; &emps; - tab
#*85 - field to enter data; name - variable for last name; type - text as input type
#*86 - table cell et
#*87 - table row et

#*89 - table row st(start tag)
#*90 - table heading st
#*91 - label for First Name
#*92 - table heading end tag(et)
#*93 - table cell st; &emps; - tab
#*94 - field to enter data; name - variable for first name; type - text as input type
#*95 - table cell et
#*96 - table row et

#*98 - table row st(start tag)
#*99 - table heading st
#*100 - label for Middle Name
#*101- table heading end tag(et)
#*102 - table cell st; &emps; - tab
#*103 - field to enter data; name - variable for middle name; type - text as input type
#*104 - table cell et
#*105 - table row et

#*107 - table row st(start tag)
#*108 - table heading st
#*109 - label for Birthday
#*110- table heading end tag(et)
#*111 - table cell st; &emps; - tab
#*112 - field to enter data; name - variable for Birthday; type - date as input type; date picker
#*113 - table cell et
#*114 - table row et

#*116 - table row st(start tag)
#*117 - table heading st
#*118 - label for Age
#*119 - table heading end tag(et)
#*120 - table cell st; &emps; - tab
#*121 - field to enter data; name - variable for Age; type - number as input type
#*122 - table cell et
#*123 - table row et

#*125 - table row st(start tag)
#*126 - table heading st
#*127 - label for Address
#*128 - table heading end tag(et)
#*129 - table cell st; &emps; - tab
#*130 - field to enter data; name - variable for Address; type - text as input type
#*131 - table cell et
#*132 - table row et
#*133 - table et
#*135 - create a submit button and redirect to file that indicated in form action

#*137 - sustitute the placeholder in values in all input; values from loop in readstudent.py

#end tags of HTML
#*142 - print as multiline docstring
#*143 - div et
#*144 - body et
#*145 - html et
#*146 - close the print