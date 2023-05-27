import winreg as wrg

#locate of the key
loc = wrg.HKEY_USERS

#path of the key
reg_path = wrg.OpenKeyEx(loc, r"S-1-5-21-3991912920-1792284575-3672857830-1002_Classes\\WOW6432Node\\CLSID") #paste your path here, before that u must open ur registry
key = wrg.CreateKey(reg_path, "{07999AC3-058B-40BF-984F-69EB1E554CA7}") #here the folder u must to delete.. so u dont need to change it

#reset the idm
execute = input("wanna reset your Idm?? (Y/N): ")
if execute == "y" and "Y":
	#deleting the key
    del_key = wrg.DeleteKey(key, "")
    print("")
    print("Reset succesfuly.. reset your computer :)")
else:
    print('you were cancelled to reset.. thanks:)')

wrg.CloseKey(key)




	