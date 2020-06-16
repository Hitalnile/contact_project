def add_data(db,name,phone_no):
	cur1 = db.cursor()
	cur1.execute('insert into contacts values(?,?)',(name,phone_no))
	print('Data insert successfully..')	
	
		
def delete_data(db,s):
	cur1 = db.cursor()
	if s == 'name':
		name_d = input("Enter the name to deleted from contacts : ")
		cur1.execute('delete from contacts where name = (?)',(name_d,))
		print('Data delete successfully..')	
	elif s == 'number':
		p_n = input('Enter the phone number to deleted from contacts : ')
		cur1.execute('delete from contacts where name = (?)',(p_n,))
		print('Data delete successfully..')	
	else:
		print('invalid choice..')

		
def view_data(db):
	cur1 = db.cursor()
	cur1.execute('select * from contacts')
	cts = cur1.fetchall()
	print('contact List : ',cts)


def edit_data(db,s):
	cur1 = db.cursor()
	if s == 'name':
		n = input('Enter the name : ')
		p = input('Enter the phone number which is edited : ')
		cur1.execute('update contacts set phone = (?) where name = (?)', (p, n))
		print('Data update successfully..')	
	elif s == 'number':
		n1 = input('Enter the phone number : ')
		p1 = input('Enter the name which is edited : ')
		cur1.execute('update contacts set name = (?) where phone = (?)',(p1,n1))
		print('Data update successfully..')
	else:
		print('Update Failed')

		
def search(db,s):
	cur1 = db.cursor()
	if s == 'name':
		n = input('Enter the name : ')
		cur1.execute('select * from contacts where name == (?)',(n,))
		cts = cur1.fetchone()
		print('contact List : ',cts)
	elif s == 'number':
		n1 = input('Enter the phone number : ')
		cur1.execute('select * from contacts where phone == (?)', (n1,))
		cts = cur1.fetchone()
		print('contact List : ',cts)
	else:
		print('Invalid search...')



