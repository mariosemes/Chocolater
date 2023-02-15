import os


def remove_list(original_file_path, edit_id):  
    original_file = open(original_file_path)
    read_flag = 1
    lines = ""

    while(1): 
        s = original_file.readline()
        if s.replace("\n", "") == "<!-- start{0} -->".format(edit_id): 
            read_flag = 0
            lines += "<!-- start{0} -->\n".format(edit_id)
        if s.replace("\n", "") == "<!-- end{0} -->".format(edit_id):   read_flag = 1
        if read_flag: lines += s
        if s == "": break

    with open(original_file_path, "w") as original_file:
        for line in lines:
            original_file.write(line)


def put_new_list(original_file_path, editted_info_path, edit_id):
    original_file = open(original_file_path)
    editted_info  = open(editted_info_path)
    read_flag = 1
    lines = ""
    s = ""

    while(1):
        if read_flag:     
            s = original_file.readline()
        if not read_flag: 
            s = editted_info.readline()
            if s.replace("\n", "") == "<!-- end{0} -->".format(edit_id):  
                read_flag = 1
                continue
        if s.replace("\n", "") == "<!-- start{0} -->".format(edit_id): read_flag = 0
        
        lines += s

        if s == "": break

    with open(original_file_path, "w") as f:
        for line in lines:
            f.write(line)


def icon_link_creator(splited_list):
    os.system("choco info \"{0}\" >> {1}\\temp_file.txt".format(splited_list[1], os.path.abspath(os.curdir)))
    choco_info_file = open(os.path.abspath(os.curdir) + "\\" + "temp_file.txt", "r+")
    choco_info_file.readline()
    choco_info = choco_info_file.readline()
    choco_info = choco_info.split()
    link = splited_list[1] + "." + choco_info[1]
    choco_info_file.truncate(0)
    choco_info_file.close()
    print(link)
    return link


def main_list_creator(list_path):
    f = open(list_path)
    a = []
    final = ""
    form_check_opened = 0
    current_group = ""
    group_type = 0
    for i in f:
        if len(i) > 4 and not (i == "Displayed name,Choco pack name,WinGet pack name,Is svg?\n"): a.append(i[:-1])
    for i in a:
        if i[0] == '*' or i[0] == '%' or i[0] == '&':
            if form_check_opened == 1: final += "\n</div> \n\n"
            form_check_opened = 1
            current_group = i[1:-3]
            final += "<div class=\"form-check\">\n"
            final += "<input class=\"form-check-input\" type=\"checkbox\" name=\"category\" id=\"{0}\" value=\"{0}\">\n"\
                .format(current_group)
            final += "<label class=\"form-check-label\" for=\"{0}\"><h3>{0}</h3></label> <br>"\
                .format(current_group)
            if i[0] == '*': group_type = 1
            if i[0] == '%': group_type = 2
            if i[0] == '&': group_type = 3
        else:
            splitted_list = i.split(",")
            if i[0] == "#":
                f = open(os.path.abspath(os.curdir) + "\\" + "temp_file.txt", "a")
                if i == "#\\\\\\": 
                    f.write("<!-- end_comment -->\n")
                else:
                    f.write("<br>" +  i[1:] + "\n")
                continue
            # p_img_extension = ""
            if splitted_list[3] == "":
                p_img_extension = "png"
            else:
                p_img_extension = splitted_list[3]
            package_img = "<img src=\"https://community.chocolatey.org/content/packageimages/{0}.{1}\" width=\"16\" height=\"16\">".format(
                icon_link_creator(splitted_list), p_img_extension)
            package_link_html_opened = "<a href=\"https://community.chocolatey.org/packages/{0}\" target=\"_blank\">".format(
                splitted_list[1])
            link_icon = "<img src=\"https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/url.svg\" width=\"16\" height=\"16\">"
            winget_icon = "<img src=\"https://raw.githubusercontent.com/Deezbec/Chocolater-and-WinGeter/main/images/WinGet_support.webp\" width=\"16\" height=\"16\">"
            winget_package_htmlopened = "<a href=\"https://wingetgui.com/apps?id={0}\" target=\"_blank\">".format(
                splitted_list[2])
            #winget_icon = ""
            if splitted_list[2] == "": winget_icon = ""
            final += (
                "\n\n<input class=\"form-check-input\" type=\"checkbox\" name=\"app\" id=\",{1},{0},{2}\" value=\",{1},{0},{2}\">\n".format(
                    splitted_list[1], current_group, splitted_list[2]))
            if group_type == 1:
                final += "<label class=\"form-check-label\" for=\",{3},{1},{2}\">{4} {0} {5}{6}</a>{7}{8}</a></label><br>".format(
                    splitted_list[0], splitted_list[1], splitted_list[2], current_group, package_img,
                    package_link_html_opened, link_icon, winget_package_htmlopened, winget_icon)
            if group_type == 2:
                final += "<label class=\"form-check-label\" for=\",{3},{1},{2}\">{5}{4}</a></label>".format(
                    splitted_list[0], splitted_list[1], splitted_list[2], current_group, package_img,
                    package_link_html_opened, )
                final += "<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>"
            if group_type == 3:
                final += "<label class=\"form-check-label\" for=\",{3},{1},{2}\">{0}{6}{7}</a></label><br>".format(
                    splitted_list[0], splitted_list[1], splitted_list[2], current_group, package_img,
                    package_link_html_opened, winget_package_htmlopened, winget_icon)
                

    final += "\n</div> \n\n"
    final += "<!-- end -->\n"

    f = open(os.path.abspath(os.curdir) + "\\" + "html_formatted_list.txt", "w")
    f.write(final)
    f.close()


# Main

# Default_info
generator_path = os.path.abspath(os.curdir) + "\\" + "generator.html"
list_path = os.path.abspath(os.curdir) + "\\" +  "list.csv"

if_run_main_list_creator = 1
if_run_remove_list = 1
if_run_put_new_list = 1

# User info
input_text = input('Write html file name (default: generator.html): ')
if not (input_text == ""): generator_path = input_text
input_text = input("Write new list file name (default: list.csv): ")
if not (input_text == ""): list_path = input_text
#input_text = input("Run all functions? (default: yes): ") #\n type \"e\" for extra functions):
#if not (input_text == "") and not (input_text == "yes"):
#    if input("Run main_list_creator? (\"\" - yes; \"no\" - no) ") == "no":
#        if_run_main_list_creator = 0
#    if input("Run remove_list? (\"\" - yes; \"no\" - no) ") == "no": if_run_remove_list = 0
#    if input("Run put_new_list? (\"\" - yes; \"no\" - no) ") == "no": if_run_put_new_list = 0

if if_run_main_list_creator:    
    main_list_creator(list_path)
if if_run_remove_list:
    remove_list(generator_path, "")  # remove list
    remove_list(generator_path, "_comment") # remove notes
if if_run_put_new_list:
    put_new_list(generator_path, os.path.abspath(os.curdir) + "\\" +  "html_formatted_list.txt", "")
    put_new_list(generator_path, os.path.abspath(os.curdir) + "\\" +  "temp_file.txt", "_comment")
    os.remove("{}\\temp_file.txt".format(os.path.abspath(os.curdir)))

print("Completed!")
#input()
