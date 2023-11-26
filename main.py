import winreg 

def reset_idm(locate, reg_path, reg_key):
	open_reg = winreg.OpenKeyEx(locate, reg_path)
	open_key = winreg.CreateKey(open_reg, reg_key)

	if open_reg: 
		del_key = winreg.DeleteKey(open_key, "")
		print("Done, reboot your computer")
	else:
		print("failed to reset, path must be correct!!")

#input these variable
locate = winreg.HKEY_USERS
reg_path = 'S-1-5-21-3991912920-1792284575-3672857830-1002_Classes\\WOW6432Node\\CLSID'
reg_key = '{07999AC3-058B-40BF-984F-69EB1E554CA7}'

reset_idm(locate, reg_path, reg_key)

