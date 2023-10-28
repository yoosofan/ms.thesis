def path_linux_win(nameDir):
	import sys
	import string
	ret1='..'
	error_report_str='error in path_linux_win \ntype is not recognized '
	if sys.version.lower().find('linux')>=0 :
		if type(nameDir) is str:
			ret1=ret1+'/'+nameDir
		elif type(nameDir) is list:
			for str1 in nameDir:
				ret1=ret1+'/'+str1
		else:
			print error_report_str
			exit
		ret1=ret1+'/'
	else:  # windows
		if type(nameDir) is str:
			ret1=ret1+'\\'+nameDir
		elif type(nameDir) is list:
			for str1 in nameDir:
				ret1=ret1+'\\'+str1
		else:
			print error_report_str
			exit
		ret1=ret1+'\\'
	return ret1



#print path_linux_win(['kkk','ffff','gggg'])