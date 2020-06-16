import sqlite3

from project_contact import data

db = sqlite3.connect('contact.db')
cur = db.cursor()
cur.execute('create table if not exists contacts(name text,phone text)')

def con_main():
	ch = ''
	while ch != 0:
		ch = int(input('0..for Exit\n1..for Add\n2..for Delete\n3..for View\n4..for Edit\n5..for Search......:'))
		if ch == 1:
			name = input("Enter the contact's name : ")
			phone_no = input("Enter the phone number : ")
			data.add_data(db,name,phone_no)
		elif ch == 2:
			s = input('Write number or name to delete contact : ')
			data.delete_data(db,s)
		elif ch == 3:
			data.view_data(db)
		elif ch == 4:
			s = input('Write phone number or name to edit contact : ')
			data.edit_data(db,s)
		elif ch == 5:
			s = input('Write number or name to edit contact : ')
			data.search(db,s)
		elif ch == 0:
			print('Thank you for visite..')
		else:
			print('choice is invalid..try again')

con_main()
db.commit()
db.close()
