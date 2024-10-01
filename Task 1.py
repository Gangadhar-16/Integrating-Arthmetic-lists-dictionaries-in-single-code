print("\t \t \t TASK-1")

def arithmetic_operations():
    num1 = int(input("Enter First Value:"))
    num2 = int(input("Enter Second value:"))
    print("Addition",num1+num2)
    print("Subtraction",num1-num2)
    print("Division",num1/num2)
    print("Multipliction",num1*num2)
    print("To the Power",num1**num2)


def list_operations():
    print("\t DIFFERENT OPERATIONS ON LISTS")
    #creating list by user6
    my_list = list(input("enter DATA:"))
    print("Given list :",my_list)
    #giving data from user to add some data in list
    num1 = str(input("enter the adding data:"))
    my_list.append(num1)
    print("Updated list after adding some data",my_list)
    #for remmoving unwanted data from updated list
    num2 = str(input("Enter Data to Remove From Updated List :"))
    my_list.remove(num2)
    print("Updated list after removing unwanted data from list:",my_list)
    #replaceing data of updated list
    num3 = int(input("Enter Position of data to replace:"))
    my_list[num3] = str(input("enter data:"))
    print("updated list",my_list)
    num4 = int(input("Enter the Postion to Insert Data:"))
    num5 = str(input("enter data to insert"))
    my_list.insert(num4,num5)
    print("update list",my_list)

def participant_data_operations():

 participents = []

 while True:
    name = str(input("Enter Student Name: "))
    number = int(input("Enter Student ID: "))
    college = str(input("Enter College Name: "))
    city = str(input("Enter College Location: "))

    # Create a dictionary for the current student
    student_data = {
        'Student': name,
        'ID': number,
        'College Name': college,
        'City': city
    }
    # Add the dictionary to the list
    participents.append(student_data)

    # Ask if the user wants to continue
    cont = input("Do you want to add another student? (yes/no): ").lower()
    if cont != 'yes':
        break
 # Print all student data after the loop
 print("Student Data:")

 print(participents)

 coloum = str(input("Enter new coloum name:"))
 new = str(input("data:"))
 student_data[coloum] = new
 print("Details of Participents:",participents)
 col_name= input("Enter column name to delete: ")
 if col_name in student_data:
     del student_data[col_name]
     print("Updated Details of Participant:", participents)

#Main choice interface
while True:
    print("\nMENU")
    print("1. Arithmetic Operations")
    print("2. List Operations")
    print("3. Participant Data Operations")
    print("4. Exit")
    
    choice = int(input("Choose an option (1-4): "))
    
    if choice == 1:
        arithmetic_operations()
    elif choice == 2:
        list_operations()
    elif choice == 3:
        participant_data_operations()
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please select again.")
