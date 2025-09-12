import sqlite3
def show_all():
	connect = sqlite3.connect('Database.db')
	cursor = connect.cursor()
	cursor.execute("SELECT rowid, * FROM students")
	items = cursor.fetchall()
	for item in items:
		print(item)
	connect.close()

def email_update(curr_email, new_email):
	connect = sqlite3.connect('Database.db')
	cursor = connect.cursor()
	cursor.execute("UPDATE students SET email = ? WHERE email = ?", (new_email, curr_email))
	connect.commit()
	connect.close()

def pass_update(curr_email):
	connect = sqlite3.connect('Database.db')
	cursor = connect.cursor()
	while True:
		curr_pass = input("Enter your current password: ")
		cursor.execute("SELECT * FROM students WHERE email = ?", (curr_email,))
		items = cursor.fetchall()
		if not items:
			print("Your email doesnt, exist in the data base, go to add_data() to create data on your email")
			connect.close()
			return
		if curr_pass == items[0][2]:
			while True:
				new_pass = input("Enter yoru new password sir: ")
				conf_password = input("Confirm your pasword: ")
				if new_pass != conf_password:
					print("your entered password and confirmation password dont match \n please recheck")
					continue
				if len(new_pass) < 8:
					print("Your password if too short, please enter a longer one")
					continue
				if new_pass == curr_pass:
					print("You enter the same password again")
					continue
				break
			cursor.execute("UPDATE students SET password = ? WHERE email = ?", (new_pass, curr_email))
			print("Data updated")
			connect.commit()
			connect.close()
			break
		else:
			print("Incorrect password")
			continue

def add_data():
	connect = sqlite3.connect('Database.db')
	cursor = connect.cursor()
	data_list = []
	while True:
		name = input("Enter the full name: ")
		email_id = input("Enter users email id: ")
		while True:
			password = input("Enter your password: ")
			conf_password = input("Confirm your pasword: ")
			if password != conf_password:
				print("your entered password and confirmation password dont match \n please recheck")
				continue
			if len(password) < 8:
				print("Your password if too short, please enter a longer one")
				continue
			break
		data_list.append((name, email_id, password))
		choice = input("Do you have more data to add ?? (Y/N)").lower()
		if choice == "n":
			break
	cursor.executemany("INSERT INTO students VALUES (?,?,?)", data_list)
	connect.commit()
	connect.close()

def drop_table():
	connect = sqlite3.connect('Database.db')
	cursor = connect.cursor()
	cursor.execute("DROP TABLE students")
	connect.commit()
	connect.close()

def drop_row(email):
	connect = sqlite3.connect('Database.db')
	cursor = connect.cursor()
	cursor.execute("DELETE FROM students WHERE email = (?)", (email,))
	connect.commit()
	connect.close()

