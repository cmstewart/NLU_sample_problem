def generalizing(tagged_version):
	i = 0
	final_list = []
	for token in tagged_version.split(' '):
		 string_1 = token.replace('|<unk>','')
		 if '<duration>' in string_1:
		 	i+=1
			if i==1:
		 		string_1 = string_1.replace('<duration>','')
		 if 'hour' in string_1:
		 	string_1 = string_1.replace(string_1,'hour]<duration>')
		 if 'monday' in string_1:
		 	string_1 = string_1.replace('monday','[monday]')
		 if 'one' in string_1:
		 	string_1 = string_1.replace(string_1,'[one')     
		 string_1 = string_1.replace('|','')
		 final_list.append(string_1)
	final_string =' '.join(final_list)
	print(final_string)