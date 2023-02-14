import os


def icon_link_creator(splited_list):
    os.system("winget find \"{0}\" >> {1}\\temp_file.txt".format(splited_list[1], os.path.abspath(os.curdir)))



def main_list_creator(list_name):
    f = open(list_name)
    a = []
    form_check_opened = 0
    group_type = 0
    for i in f:
        if len(i) > 4 and not (i == "Displayed name,Choco pack name,WinGet pack name,Is svg?\n"): a.append(i[:-1])
    for i in a:
        if i[0] == '*' or i[0] == '%' or i[0] == '&':
            a = 2
        else:
            splitted_list = i.split(",")
            icon_link_creator(splitted_list)


main_list_creator("list.csv")