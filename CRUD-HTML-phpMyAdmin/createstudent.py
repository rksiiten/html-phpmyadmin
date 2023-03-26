#!C:\Users\krist\AppData\Local\Programs\Python\Python38-32\python.exe
#part of HTTP header which is sent to the browser to understand the content
print ("Content-type:text/html\r\n\r\n")
print("""<!DOCTYPE html>
<html>
  <head>
    <title>Register Student</title>
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
      <h1>REGISTER STUDENT</h1><hr>
""")
#form action-where to send; method when sending; get-inputdata show in url
print("""
<form action="process.py" method="get">
    
  <table>
    <tr>
      <th>
        <p><b>Student Number: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="stnum" type="text">
      </td>
    </tr>

    <tr>
      <th>
        <p><b>Last Name: </b></p>  
      </th>
      <td>&emsp;&emsp;
        <input name="lname" type="text">
      </td>
    </tr>

    <tr>
       <th>
        <p><b>First Name: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="fname" type="text">
      </td>
    </tr>

    <tr>
      <th>
        <p><b>Middle Name: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="mname" type="text">
      </td>
    </tr>

    <tr>
      <th>
        <p><b>Birthday: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="bday" type="date">
      </td>
    </tr>

    <tr>
      <th>
        <p><b>Age: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="age" type="number">
      </td>
    </tr>

    <tr>
      <th>
        <p><b>Address: </b></p>
      </th>
      <td>&emsp;&emsp;
        <input name="address" type="text">
      </td><!--hello-->
    </tr>
  </table>

  <p style="text-align:center"><input type="submit" value="SUBMIT"></p>

</form>
""")

print("""
    </div>
  </body>
</html>
""")

#COMMENTS PER LINE:

#*1 - shell convention that tells the shell which program can execute the script
#*3 - part of HTTP header which is sent to the browser to understand the content
#*4 - print as multiline docstring; DOCTYPE html defines the document type
#*5 - start tag for html
#*6 - start tag for head
#*7 - this appear on tab
#*8 - end tag for head

#*10 - start tag for style; style information for a document
#*11 - h1 styl; HTML heading
#*12 - center align the text for h1
#*14 - body style
#*15 - bg image link that show in webpage
#*16 - Helvetica as font for the body
#*17 - color of text in body white
#*19 - div style
#*20 - bg color
#*21 - width of div section
#*22 - border size and color of div section
#*23 - padding size
#*24 - margin auto so it depends on the size of the page
#*26 - table style
#*27 - table width size
#*29 - table header style
#*30 - table header width size
#*32 - paragraph style
#*33 - center align the text for paragraph
#*35 - end tag for style

#*37 - start tag for body
#*38 - start tag for div; section in a document
#*39 - contains HTML heading
#*40 - close the print

#*42 - print as multiline docstring
#*43 - form action-define where to send; method-HTTP method to use when sending; get-entered data show in url; this is where user input data
#*45 - start tag for table; create a table; for organization of data

#*46 - table row st(start tag)
#*47 - table heading st
#*48 - label for Student Number
#*49 - table heading end tag(et)
#*50 - table cell st; &emps; - tab
#*51 - field to enter data; name - variable for student number; type - text as input type
#*52 - table cell et
#*53 - table row et

#*55 - table row st(start tag)
#*56 - table heading st
#*57 - label for Last Name
#*58 - table heading end tag(et)
#*59 - table cell st; &emps; - tab
#*60 - field to enter data; name - variable for last name; type - text as input type
#*61 - table cell et
#*62 - table row et

#*64 - table row st(start tag)
#*65 - table heading st
#*66 - label for First Name
#*67 - table heading end tag(et)
#*68 - table cell st; &emps; - tab
#*69 - field to enter data; name - variable for first name; type - text as input type
#*70 - table cell et
#*71 - table row et

#*73 - table row st(start tag)
#*74 - table heading st
#*75 - label for Middle Name
#*76 - table heading end tag(et)
#*77 - table cell st; &emps; - tab
#*78 - field to enter data; name - variable for middle name; type - text as input type
#*79 - table cell et
#*80 - table row et

#*82 - table row st(start tag)
#*83 - table heading st
#*84 - label for Birthday
#*85 - table heading end tag(et)
#*86 - table cell st; &emps; - tab
#*87 - field to enter data; name - variable for Birthday; type - date as input type; date picker
#*88 - table cell et
#*89 - table row et

#*91 - table row st(start tag)
#*92 - table heading st
#*93 - label for Age
#*94 - table heading end tag(et)
#*95 - table cell st; &emps; - tab
#*96 - field to enter data; name - variable for Age; type - number as input type
#*97 - table cell et
#*98 - table row et

#*100 - table row st(start tag)
#*101 - table heading st
#*102 - label for Address
#*103 - table heading end tag(et)
#*104 - table cell st; &emps; - tab
#*105 - field to enter data; name - variable for Address; type - text as input type
#*106 - table cell et
#*107 - table row et

#*108 - table et

#*110 - create a submit button and redirect to file that indicated in form action

#*112 - form et
#*113 - close the print

#end tags
#*115 - print as multiline docstring
#*116 - div et
#*117 - body et
#*118 - html et
#*119 - close the print