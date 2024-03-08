import mysql.connector
from PIL import Image
import io

x = mysql.connector.connect(
    host="localhost", user="root",password="Rudra@360" ,database="criminal"
)
y = x.cursor()

def insert_data():
    filepath = input("Enter the path of the file: ")
    name = input("Enter the Name of Criminal: ")
    type = input("Enter the Type: ")
    desc = input("Enter the Description: ")
    date = input("Enter the Date of incident: ")
    adhar_id = input("Enter the Adhar_id: ")

    try:
        with open(filepath, "rb") as file:
            image_binary = file.read()
            sql = "INSERT INTO CRIMINAL (CRIMINAL_PHOTO, CRIMINAL_NAME, TYPE, DESCRIPTION, DATEOFCRIME, ADHAR_ID) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (image_binary, name, type, desc, date, adhar_id)
            y.execute(sql, data)
            x.commit()
            print("Information inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

def retrieve_image():
    Adhar_id=input("Enter the Adhar_id :")
    try:
        sql = "SELECT CRIMINAL_PHOTO FROM CRIMINAL WHERE Adhar_ID = %s"
        y.execute(sql, (Adhar_id,))
        result = y.fetchone()
        if result:
            image_binary = result[0]
            image = Image.open(io.BytesIO(image_binary))
            image.show()
        else:
            print("No image found for the specified ID.")
    except Exception as e:
        print(f"Error retrieving image: {str(e)}")

# def retrieve_image(id):
#     try:
#         sql = "SELECT CRIMINAL_PHOTO FROM CRIMINAL WHERE id = %s"
#         y.execute(sql, (id,))
#         result = y.fetchone()
#         if result:
#             image_binary = result[0]
#             image = Image.open(io.BytesIO(image_binary))
#             image.show()
#         else:
#             print("No image found for the specified ID.")
#     except Exception as e:
#         print(f"Error retrieving image: {str(e)}")

# def insert_type():
#     data = []
#     data.append(input("Enter the Type :"))
#     try:
#         sql = "INSERT INTO CRIMINAL (TYPE) VALUES (%s)"
#         y.execute(sql, (data))
#         x.commit()
#         print("Type inserted successfully!")
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def Print_type(id):
#     try:
#         sql = "SELECT TYPE FROM CRIMINAL WHERE ID=" + str(id)
#         y.execute(sql)
#         rows = y.fetchall()
#         x.commit()
#         for row in rows:
#             print(row)
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def Insert_Desc():
#     data = []
#     data.append(input("Enter the Description:"))
#     try:
#         sql = "INSERT INTO CRIMINAL (DESCRIPTION) VALUES (%s)"
#         y.execute(sql, (data))
#         x.commit()
#         print("Type inserted successfully!")
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def Print_desc(id):
#     try:
#         sql = "SELECT DESCRIPTION FROM CRIMINAL WHERE ID=" + str(id)
#         y.execute(sql)
#         rows = y.fetchall()
#         x.commit()
#         for row in rows:
#             print(row)
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def Insert_Name():
#     data = []
#     data.append(input("Enter the Name of Criminal :"))
#     try:
#         sql = "INSERT INTO CRIMINAL (CRIMINAL_NAME) VALUES (%s)"
#         y.execute(sql, (data))
#         x.commit()
#         print("NAME inserted successfully!")
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def Print_name(id):
#     try:
#         sql = "SELECT CRIMINAL_NAME FROM CRIMINAL WHERE ID=" + str(id)
#         y.execute(sql)
#         rows = y.fetchall()
#         x.commit()
#         for row in rows:
#             print(row)
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def Insert_adhar_id():
#     data = []
#     data.append(input("Enter the Adhar_id :"))
#     try:
#         sql = "INSERT INTO CRIMINAL (Adhar_id) VALUES (%s)"
#         y.execute(sql, (data))
#         x.commit()
#         print("Adhar_id inserted successfully!")
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def Print_adhar_id(id):
#     try:
#         sql = "SELECT Adhar_id FROM CRIMINAL WHERE ID=" + str(id)
#         y.execute(sql)
#         rows = y.fetchall()
#         x.commit()
#         for row in rows:
#             print(row)
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def Insert_date():
#     data = []
#     data.append(input("Enter the Date of incident :"))
#     try:
#         sql = "INSERT INTO CRIMINAL (DATE_INCIDENT) VALUES (%s)"
#         y.execute(sql, (data))
#         x.commit()
#         print("date_incident inserted successfully!")
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

# def print_date(id):
#     try:
#         sql = "SELECT DATE FROM CRIMINAL WHERE ID=" + str(id)
#         y.execute(sql)
#         rows = y.fetchall()
#         x.commit()
#         for row in rows:
#             print(row)
#     except Exception as e:
#         print(f"Error inserting data: {str(e)}")

def Search_by_name(Name):
    try:
        sql = "SELECT CRIMINAL_NAME, TYPE, DESCRIPTION, DATEOFCRIME, ADHAR_ID FROM CRIMINAL WHERE CRIMINAL_NAME = %s"
        y.execute(sql, (Name,))
        rows = y.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error searching by name: {str(e)}")


# print("1 -----> Read image")
# print("2 -----> Insert image")
# print("3 -----> Insert Type")
# print("4-------> Print Type")
# print("5-------> Insert Desc")
# print("6-------> Print Desc")
# print("7-------> Insert Name")
# print("8-------> Print Name")
# print("9-------> Insert Adhar_id")
# print("10-------> Print Adhar_id ")
# print("11------> Insert Date_incident")
# print("12-------> Print Date_incident")
# print("13-------> Search by Name")

# choice = int(input("Enter choice: "))

# if choice == 2:
#     id = int(input("Enter the ID: "))
#     retrieve_image(id)
# elif choice == 1:
#     insert_image()
# elif choice == 3:
#     insert_type()
# elif choice == 4:
#     id = int(input("Enter the ID: "))
#     Print_type(id)
# elif choice == 5:
#     Insert_Desc()
# elif choice == 6:
#     id = int(input("Enter the ID: "))
#     Print_desc(id)
# elif choice == 8:
#     id = int(input("Enter the ID: "))
#     Print_name(id)
# elif choice == 10:
#     id = int(input("Enter the ID: "))
#     Print_adhar_id(id)
# elif choice == 12:
#     id = int(input("Enter the ID: "))
#     print_date(id)
# elif choice == 7:
#     Insert_Name()
# elif choice == 9:
#     Insert_adhar_id()
# elif choice == 11:
#     Insert_date()
# elif choice == 13:
#     Name = input("Give the name of criminal :")
#     Search_by_name(Name)
print("2 -----> Read information")
print("3 -----> Read Image of  Criminal")
print("1 -----> Insert information")

choice=int(input("Enter the choice :"))
if(choice==2):
    name=input("Enter the name of criminal:")
    Search_by_name(name)
elif choice == 3:
    retrieve_image()
else:
    insert_data()
y.close()
x.close()