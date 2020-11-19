def fancyLog(path, type, returned, htmlCode):
	path = checkLogLength("| Path: {}".format(path))
	type = checkLogLength("| Type: {}".format(type))
	returned = checkLogLength("| Returned: {}".format(returned))
	print("+-------------------------------------------------------------------------------------------+")
	print("| API Request                                                                               |")
	print(path + "|")
	print(type + "|")
	print(returned + "|")
	print("| HTML Code: {}                                                                            |".format(str(htmlCode)))
	print("+-------------------------------------------------------------------------------------------+")
	