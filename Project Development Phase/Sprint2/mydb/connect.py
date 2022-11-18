import ibm_db

def list_all():
   sql= "SELECT * from userregister"
   stmt = ibm_db.exec_immediate(conn, sql)
   dictionary = ibm_db.fetch_both(stmt)
   while dictionary != False:
     print ("The Name is : ",  dictionary["NAME"])
     print ("The email is : ", dictionary["EMAIL"])
     print ("The password is : ", dictionary["PASSWORD"])
     print ("The phone number is : ", dictionary["mobile number"])
     dictionary = ibm_db.fetch_both(stmt)

def insert_values(name,email,password,mobilenumber):
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zhc67031;PWD=cMrI3QzWfo581pJ2;", "", "")
    sql = "INSERT INTO USERREGISTER VALUES('{}','{}','{}','{}')".format(name,email,password,mobilenumber)
    stmt = ibm_db.exec_immediate(conn,sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
   conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;PROTOCOL=TCPIP;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zhc67031;PWD=cMrI3QzWfo581pJ2;", "", "")
   print("yes")
   list_all()
except:
   print("not")