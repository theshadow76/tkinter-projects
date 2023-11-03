import cgi
import cgitb

print ('Content-type: text/html\n\n')

form = cgi.FieldStorage()

email = form.getvalue('email')
print(email)