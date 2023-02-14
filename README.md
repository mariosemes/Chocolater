![Chocolater](https://raw.githubusercontent.com/mariosemes/Chocolater/main/images/simple-logo.jpg "Chocolater")
#### App Install Tool

[![CLICK TO VISIT GENERATO with Deezbec's progs](https://img.shields.io/badge/Click_To_Visit_Generator-blue.svg?style=for-the-badge)](https://raw.githack.com/Deezbec/Chocolater-and-WinGeter/main/generator.html)
Deezbec's progs 

Basically it is [Chocolater](https://github.com/mariosemes/Chocolater) by [Mariosemes](https://github.com/mariosemes) with new features:
1) Simple creation of your own list
2) "Select all" from group
3) WinGet support
4) Icons for programs are automatically got from chocolatey's program package page<br><br>
Remark about "select all from group" check box: <br> While it is active checking boxes of entryes of the selected group will remove them from selection

------------
[![CLICK TO VISIT GENERATOR with Deezbec's progs](https://img.shields.io/badge/Click_To_Visit_Generator-blue.svg?style=for-the-badge)](https://raw.githack.com/Deezbec/Chocolater-and-WinGeter/main/generator.html)
------------
## Want to create your own list?
1) Download the source code
2) Copy "generator.hmtl" and "list.csv" to "list editing" folder
3) Edit "list.csv" (I personally do this with VS code's "edit CSV" extension)<br>
Columns stand for:<br>
1st - Displayed package name<br>
2nd - Chocolatey package name (its also used to get icons)<br>
3rd - WinGet pack name (optional)<br>
4th - What is icon on chocolatey package page extension (default - png)<br><br>
Rows:<br>
Can be devided to 3 categories:<br>
1st -  Group<br>
Groups can start with:  "\*","&","%"<br>
"\*" - standart list<br>
"&" - list without icon and chocolatey package link<br>
"%" - standart compact list. Can be used to create pack's of programs<br><br>
2nd - Entry<br>
Just Enter all the needed information for the entry <br>
4) Run "Create & replace list.py"<br>
if everything is ok, you will see your programs names with the latest version found on Chocolatey <br>
Program should end with "Completed"<br>
If you have any problems, feel free to msg me on discord Deezbec#2094 or create a ticket on github <br><br>
3rd - Comments<br>
They should be place on the bottom of list.csv file<br>
Each line have to be started with "#"<br>

------------
### License
This script is under the [GNU General Public License v3.0](https://github.com/mariosemes/Chocolater/blob/main/LICENSE "GNU General Public License v3.0") License.
