from file import selected
print ("Moi ban nhap kieu du lieu can sap xep: 'id' or 'temperature' or 'humidity' or 'time'")
a = input()
if a !='id' and a != 'temperature' and a!='humidity':
	print("Khong ton tai truong nay, moi ban nhap lai:")
	a = input()
if a == 'id':
	print("Sap xep tang gian hay giam dan: 'giam' or 'tang'")
	b = input()
	if b == 'tang':
		selected(a,b)
	if b == 'giam':
		selected(a,b)
if a == 'temperature':
	print("Sap xep tang gian hay giam dan")
	b = input()
	if b == 'tang':
		selected(a,b)
	if b == 'giam':
		selected(a,b)
if a == 'humidity':
	print("Sap xep tang gian hay giam dan")
	b = input()
	if b == 'tang':
		selected(a,b)
	if b == 'giam':
		selected(a,b)
if a == 'time':
	print("Sap xep tang gian hay giam dan")
	b = input()
	if b == 'tang':
		selected(a,b)
	if b == 'giam':
		selected(a,b)