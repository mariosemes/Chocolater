import os
f = open('prog+list.txt')
a = []
final = ""
form_check_opened = 0
for i in f:
    if len(i) > 1: a.append(i[:-1])
for i in a:
    if i[0] == '-':
        if form_check_opened == 1: final += "\n</div> \n\n"
        form_check_opened = 1
        final += "<div class=\"form-check\">\n <h3>{}</h3>".format(i[1:])
    else:
        b = i.split(" _ ")
        os.system('choco info "{}" >> c:\!User\Temp\jojo.txt'.format(b[1]))
        f = open("jojo.txt", "r+")
        f.readline()
        s = f.readline()
        s = s.split()
        link = b[1] + "." + s[1]
        f.truncate(0)
        f.close()
        print(link)

        final += ("\n\n<input class=\"form-check-input\" type=\"checkbox\" name=\"app\" id=\"{0}\" value=\"{0}\">\n".format(b[1]))
        if len(b) == 2: final += ("<label class=\"form-check-label\" for=\"{1}\"><img src=\"https://community.chocolatey.org/content/packageimages/{2}.png\" width=\"16\" height=\"16\"> {0} <a href=\"https://community.chocolatey.org/packages/{1}\" target=\"_blank\"><img src=\"https://raw.githubusercontent.com/Deezbec/Chocolater/main/images/url.svg\" width=\"16\" height=\"16\"></a></label><br>".format(b[0], b[1], link))
        if len(b) == 3: final += ("<label class=\"form-check-label\" for=\"{1}\"><img src=\"https://community.chocolatey.org/content/packageimages/{2}.svg\" width=\"16\" height=\"16\"> {0} <a href=\"https://community.chocolatey.org/packages/{1}\" target=\"_blank\"><img src=\"https://raw.githubusercontent.com/Deezbec/Chocolater/main/images/url.svg\" width=\"16\" height=\"16\"></a></label><br>".format(b[0], b[1], link))



final += "\n</div> \n\n"
print(final)



