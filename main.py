import fun_carrier
print("Hello Welcome to the data center")
while True:
	print("""What would you like to do?
		1. Check details
		2. update any email
		3. update any password
		4. add new data
		5. Delete a row
		6. Delete the table
		7. exit""")
	try:
		choice = int(input("Enter your choice\n"))
		if (choice not in [1,2,3,4,5,6,7]):
			print("choose only between 1-7")
			continue
	except:
		print("Invalid input, choose a number between 1-6")
		continue
	if choice == 7:
		print("Thanks for using our service")
		break
	if choice == 1:
		print("Here is your requested data sir")
		fun_carrier.show_all()
	elif choice == 2:
		curr_email = input("Enter your current email sir: ")
		new_email = input("Enter your new email sir: ")
		fun_carrier.email_update(curr_email, new_email)
		print("current table status: ")
		fun_carrier.show_all()
	elif choice == 3:
		curr_email = input("Enter your email sir: ")
		fun_carrier.pass_update(curr_email)
		print("current table status: ")
		fun_carrier.show_all()
	elif choice == 4:
		fun_carrier.add_data()
		print("current table status: ")
		fun_carrier.show_all()
	elif choice == 5:
		inp_email = input("Enter the email about which you want to delete data: ")
		confirm = input("Once something is deleted its gone forever, are you sure? (Y/N)").lower()
		if confirm == "y":
			fun_carrier.drop_row(inp_email)
			print(f"The data on {inp_email} is deleted, if it ever existed")
			print("current table status: ")
			fun_carrier.show_all()
		else:
			print(f"Row with {inp_email} not deleted")
			print("current table status: ")
			fun_carrier.show_all()
	else:
		print("All the data from the table will be gone forever, are you sure?")
		confirm = input("enter '--terminate-data' to confirm deleting: ").lower()
		if confirm == "--terminate-data":
			fun_carrier.drop_table()
			print("Entire table is dropped. \n since there is no table to work with, the program will terminate")
			print("It was nice meeting you...")
			break
		else:
			print("Termination of table stopped")
			print("current table status: ")
			fun_carrier.show_all()