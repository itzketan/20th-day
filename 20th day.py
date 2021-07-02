import mysql.connector
mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "@mysqlketangurav22",
                               database = "employees")
dbase = mydb.cursor()
sql = "Select Salary from employees " \
      "where Salary = ( select MIN(Salary) from employees);"
dbase.execute(sql)
myresult = dbase.fetchone()
print("Minimum Salary : ", myresult)

dbase = mydb.cursor()
sql = "Select Salary from employees " \
      "where Salary = ( select MAX(Salary) from employees);"
dbase.execute(sql)
myresult= dbase.fetchone()
print("Maximum Salary : ", myresult)

dbase = mydb.cursor()
sql = "Select count(*) from employees;"
dbase.execute(sql)
myresult = dbase.fetchone()
print("Number Of Employees : ", myresult)

dbase = mydb.cursor()
sql = "Select substring(employee_name,1,3) from employees;"
dbase.execute(sql)
myresult = dbase.fetchall()
print("First 3 Characters of First Name : ", myresult)



