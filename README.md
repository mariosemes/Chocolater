![Chocolater](https://raw.githubusercontent.com/mariosemes/Chocolater/main/images/simple-logo.jpg "Chocolater")
#### App Install Tool

[![CLICK TO VISIT GENERATO with Deezbec's progs](https://img.shields.io/badge/Click_To_Visit_Generator-blue.svg?style=for-the-badge)](https://raw.githack.com/Deezbec/Chocolater-and-WinGeter/main/generator.html)
Deezbec's list

Basically it is [Chocolater](https://github.com/mariosemes/Chocolater) by [Mariosemes](https://github.com/mariosemes) with new features:

1) Simple creation of your own list
2) Icons for programs are automatically got from chocolatey's program package page
3) WinGet support(Not figured out how commands work here, so just package names at the moment)
4) "Select all" from group<br><br>
Remark about "Select all from group" check box: <br> While it is active checking boxes of entryes of the selected group will remove them from selection

------------
## Want to create your own list?

1) Download the source code
2) Copy "generator.hmtl" and "list.csv" to "list editing" folder
3) Edit "list.csv" (I personally do this with VS code's "edit CSV" extension)<br><br>
Columns stand for:  
1st - Displayed package name  
2nd - Chocolatey package name (its also used to get icons)  
3rd - WinGet pack name (optional)  
4th - What is icon on chocolatey package page extension (default - png)<br><br>
Rows:  
Can be devided to 3 categories:  
1st -  Group  
Groups can start with:  "\*","&","%"  
"\*" - standart list  
"&" - list without icon and chocolatey package link  
"%" - standart compact list. Can be used to create pack's of programs  <br><br>
2nd - Entry  
Just Enter all the needed information for the entry<br><br>
3rd - Comments  
They should be place on the bottom of list.csv file  
Each line have to be started with "#"  
Comment section ends with: "#\\\\\\"  

4) Run "Create & replace list.py"  
For some reason I can't run it without IDE, no idea how to fix  
That's why I recommend you to launch it in VS code with python or any other IDE  
if everything is ok, you will see your programs names with the latest version found on Chocolatey  
Program should end with "Completed"  
If you have any problems, feel free to msg me on discord Deezbec#2094 or create a ticket on github  

------------
## Development notes

### Feature ideas:  
1) hover program summery;  
2) another way of adding icons  

### Known issues:  


------------
### License
This script is under the [GNU General Public License v3.0](https://github.com/mariosemes/Chocolater/blob/main/LICENSE "GNU General Public License v3.0") License.