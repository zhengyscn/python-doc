
'''统计日志文件中ip列表'''
def get_ipsset():
	ip_set = set() # 为什么要用集合而不用列表？

	with open('access.log', 'r') as fd:
		for line in fd:
			line_str = line.rstrip("\n") # 为什么要加一个strip
			ip = line_str.split()[0]
			ip_set.add(ip)

	return ip_set


'''统计不同状态码出现的次数'''
def get_httpstatus():
	http_status_dic = {}
	status_code_range = [ str(x) for x in range(100, 601)]

	with open('access.log', 'r') as fd:
		for line in fd:
			line_str = line.rstrip("\n") # 为什么要加一个strip
			tmpdata_list = line_str.split()

			status_code = tmpdata_list[8]
			if status_code in status_code_range:
				http_status_dic[status_code] = http_status_dic.get(status_code, 0) + 1
			else:
				status_code = tmpdata_list[-5]
				if status_code in status_code_range:
					http_status_dic[status_code] = http_status_dic.get(status_code, 0) + 1
				else:
					print("WARN")

	return http_status_dic



def sort_dict(dic):
	return sorted(dic.items(), key=lambda x:x[1], reverse=False)


def main():
	http_status_dic = get_httpstatus()
	print(http_status_dic)
	http_status_dic = sort_dict(http_status_dic)
	print(http_status_dic)





if __name__ == '__main__':
	main()