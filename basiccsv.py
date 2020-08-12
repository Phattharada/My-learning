
import csv


def WritetoCSV(ep):
	with open('allexpense.csv','a',newline='',encoding='utf-8') as file:
		# 'a' = append เพิ่มได้เรื่อยๆ , 'w' = replace ทับไฟล์เดิม
		 fw = csv.writer(file) # fr = file  writer
		 #ep = ['ไก่',300]
		 fw.writerow(ep) 
	
	print('Done!')

x=['ไข่',30]
WritetoCSV(x)