import winreg as wrg


def Reset_idm(reg_path, reg_key, locate):
    open_reg = wrg.OpenKeyEx(locate, reg_path)
    open_key = wrg.CreateKey(open_reg, reg_key)

    if open_reg:
        del_key = wrg.DeleteKey(open_key, "")
        print('Done, reboot your pc')
    else:
        print("failed to reset, path must be correct")

#Regedit directory locate
locate = wrg.HKEY_USERS
reg_path = 'S-1-5-21-3991912920-1792284575-3672857830-1002_Classes\\WOW6432Node\\CLSID'
reg_key = '{07999AC3-058B-40BF-984F-69EB1E554CA7}'

Reset_idm(reg_path, reg_key, locate)