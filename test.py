import re
import requests
import csv

ban_list = ['机构设置', '访客', '学生', '教师', ' 校友']
response = requests.get('https://www.sjtu.edu.cn/resource/assets/js/headersy.js')
text = response.text
role_1 = r'\s+<a.*href=\'([a-zA-Z]+://[\S]*)\' target=.*>(.*?)</'
role_1_1 = r'\s+<a.*href=\'([a-zA-Z]+://[\S]*)\' target=.*>(.*?)<s'
role_1_2 = r'\s+<a.*href=\'([a-zA-Z]+://[\S]*)\' target=.*>(.*?)\"'
role_2 = r'<a\s*tabtarget=\'\d*\'.*?>(.*?)</a>'
role_2_1 = r'<a class=\'pad-left25\'  tabtarget=.*>(.*?)</a>'
role_2_2 = r'<a class=\'pad-left25\'  >(.*?)</a>'
role_2_3 = r'<a  >(.*?)</a>'
title1 = re.finditer(role_1, text, re.M)
title1_1 = re.finditer(role_1_1, text, re.M)
title1_2 = re.finditer(role_1_2, text, re.M)
title2 = re.finditer(role_2, text, re.M)
title2_1 = re.finditer(role_2_1, text, re.M)
title2_2 = re.finditer(role_2_2, text, re.M)
title2_3 = re.finditer(role_2_3, text, re.M)

with open('test.csv', 'w', encoding='utf-8', newline='')as file:
	csv_write = csv.writer(file)
	csv_write.writerow(['机构名称', '网址'])
	print('title1')
	for i in title1:
		if i.group(2) and i.group(2) not in ban_list:
			# print(i.group(1), i.group(2))
			csv_write.writerow([i.group(2), i.group(1)])
	
	print('title1_1')
	for i in title1_1:
		if i.group(2):
			# print(i.group(1), i.group(2))
			csv_write.writerow([i.group(2), i.group(1)])
	
	print('title1_2')
	for i in title1_2:
		if i.group(2):
			# print(i.group(1), i.group(2))
			csv_write.writerow([i.group(2), i.group(1)])
	
	print('title2')
	for i in title2:
		# print(i.group(1))
		csv_write.writerow([i.group(1), 'No Web'])
	
	print('title2_1')
	for i in title2_1:
		# print(i.group(1))
		csv_write.writerow([i.group(1), 'No Web'])
	
	print('title2_2')
	for i in title2_2:
		# print(i.group(1))
		csv_write.writerow([i.group(1), 'No Web'])
	
	print('title2_3')
	for i in title2_3:
		# print(i.group(1))
		csv_write.writerow([i.group(1), 'No Web'])



# 主要数据格式：
# 1 <a class='pad-left25' href='http://naoce.sjtu.edu.cn' target='_blank'>船舶海洋与建筑工程学院</a>"
# 1 <a class='pad-left25' href='https://scsb.sjtu.edu.cn/' target='_blank' tabtarget='34' retargeta='157' toretabtarget='156'>系统生物医学研究院</a>"
# 1 <a href='http://www.seiee.sjtu.edu.cn' target='_blank'>电子信息与电气工程学院</a>"
# 1.1 <a href='https://www.si.sjtu.edu.cn/' target='_blank' >学生创新中心<small></small></a>"
# 1.1 <a class='pad-left25'  href='https://net.sjtu.edu.cn/' target='_blank' >网络信息中心<small>（网络安全和信息化领导小组办公室）</small></a>"
# 1.2 <a class='pad-left25' href='https://hr.sjtu.edu.cn/teacher/' target='_blank' >党委教师工作部"
# 2 <a tabtarget='95' toretabtarget='190' retargeta='191'>上海交通大学闵行幼儿园</a>
# 2 <a   tabtarget='35' retargeta='158' toretabtarget='157'>海洋研究院</a>"
# 2.1 <a class='pad-left25'  tabtarget='94' toretabtarget='189' retargeta='190'>上海交通大学幼儿园</a>
# 2.2 <a class='pad-left25'  >信息安全管理办公室</a>"
# 2.3 <a  >上海海洋装备前瞻技术研究院</a>"