import os


def remove_list(f): #file length pproblem
    read_flag = 1
    lines = ""

    for i in range(2000): #length of the file
        s = f.readline()
        if read_flag: lines += s
        if s == "<!-- start -->\n": read_flag = 0
        if s == "<!-- end -->\n":   read_flag = 1

    with open(html_file, "w") as f:
        for line in lines:
            f.write(line)

def put_new_list(f):
    final = open("html_formated_list.txt")
    read_flag = 1
    f.read
    lines = ""

    for i in range(1000):

        if read_flag:     s = f.readline()
        if not read_flag: s = final.readline()
        lines += s
        if s == "<!-- start -->\n": read_flag = 0
        if s == "<!-- end -->\n":   read_flag = 1

    with open(html_file, "w") as f:
        for line in lines:
            f.write(line)

def link_creater(splited_list):
    os.system("choco info \"{0}\" >> {1}\\temp_file.txt".format(splited_list[1], os.path.abspath(os.curdir)))
    choco_info_file = open("temp_file.txt", "r+")
    choco_info_file.readline()
    choco_info = choco_info_file.readline()
    choco_info = choco_info.split()
    link = splited_list[1] + "." + choco_info[1]
    choco_info_file.truncate(0)
    choco_info_file.close()
    print(link)
    return link

def main_list_creater():
    f = open(list_name)
    a = []
    final = ""
    form_check_opened = 0
    current_group = ""
    for i in f:
        if len(i) > 1: a.append(i[:-1])
    for i in a:
        if i[0] == '-':
            if form_check_opened == 1: final += "\n</div> \n\n"
            form_check_opened = 1
            final += "<div class=\"form-check\">\n"
            final += "<input class=\"form-check-input\" type=\"checkbox\" name=\"category\" id=\"{0}\" value=\"{0}\">\n".format(i[1:])
            final += "<label class=\"form-check-label\" for=\"{0}\"><h3>{0}</h3></label> <br>".format(i[1:])
            current_group = i[1:]
        else:
            splited_list = i.split(" _ ")
            link = link_creater(splited_list)
            final += ("\n\n<input class=\"form-check-input\" type=\"checkbox\" name=\"app\" id=\"{0}\" value=\"_{1}_{0}\">\n".format(splited_list[1], current_group))
            if len(splited_list) == 2: final += ("<label class=\"form-check-label\" for=\"{1}\"><img src=\"https://community.chocolatey.org/content/packageimages/{2}.png\" width=\"16\" height=\"16\"> {0} <a href=\"https://community.chocolatey.org/packages/{1}\" target=\"_blank\"><img src=\"https://raw.githubusercontent.com/Deezbec/Chocolater/main/images/url.svg\" width=\"16\" height=\"16\"></a></label><br>".format(splited_list[0], splited_list[1], link))
            if len(splited_list) == 3: final += ("<label class=\"form-check-label\" for=\"{1}\"><img src=\"https://community.chocolatey.org/content/packageimages/{2}.svg\" width=\"16\" height=\"16\"> {0} <a href=\"https://community.chocolatey.org/packages/{1}\" target=\"_blank\"><img src=\"https://raw.githubusercontent.com/Deezbec/Chocolater/main/images/url.svg\" width=\"16\" height=\"16\"></a></label><br>".format(splited_list[0], splited_list[1], link))
    final += "\n</div> \n\n"
    final += "<!-- end -->\n"

    f = open("html_formated_list.txt", "w")
    f.write(final)
    f.close()


#Main

#Default_info
html_file = "generator.html"
list_name = "list.txt"
#User info
input_text = input(print('Write html file name (default: generator.html): '))
if not(input_text == ""): html_file = input_text
input_text = input(print("Write new list file name (default: list.txt): "))
if not(input_text == ""): list_name = input_text

main_list_creater()

remove_list(open(html_file))

put_new_list(open(html_file))

print("Completed!")
input()






