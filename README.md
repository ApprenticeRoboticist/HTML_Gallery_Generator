## HTML Photogallery Generator
Simple Python desktop app I developed in order to shorten and automate creation of robot assembly instructions. </br> 

### Story behind the project
During my work as Lego Mindstorms instructor one of my resposibilities was invention of new robot projects and then making its step by step assembly instructions. An instruction consists of many photos divided by sections called 'steps' and has to be in HTML format so it can be opened and displayed from a browser. Creating one manually required a lot of monotonous file renaming and copying-and-pasting inside HTML file and took around 20 to 30 minutes based on amount of photos and committed typos. As a sworn enemy of dull and repetitive yet possible-to-be-automated work, I decided to call on my Python skills to invent faster and less troublesome way of creating robot assembly instructions.

### Technologies and Tools
![](https://img.shields.io/badge/OS-Windows_10-informational?style=flat-square&logo=Windows&logoColor=white&color=red)
![](https://img.shields.io/badge/Python-3.7-informational?style=flat-square&logo=Python&logoColor=white&color=critical)
![](https://img.shields.io/badge/IDE-PyCharm-informational?style=flat-square&logo=Pycharm&logoColor=white&color=green)

### App overview
Launching an app causes its main window to show up. The app consists of one main view divided by four sections called "steps" (fig. 1).
<br><br>
<img src="https://github.com/Daemiac/HTML_Gallery_Generator/blob/master/readme_images/HPG1.png" width="400" height="550">
<br> *Fig. 1 - post start-up app's main window* <br><br>
Each step represents one operation in whole algorithm of making an instruction:
- the first step requires to choose folder of file's destination which should also contain photos needed to create instruction. If you don't choose a folder you cant proceed any further;
- the second step gives an option to numerate the photos inside the chosen folder. Numeration of photos is crucial for further processing. If photos inside chosen folder are already numerated the messagebox which informs about that fact pops up;
- the third step is naming the instruction file; 
- the fourth step is responsible for creating instruction pattern. Each of instruction's steps contains one or more photos - it is up to user to choose the amount of steps and photos that build them;

After successful journey through all steps the *"Generate the instruction"* button becomes active (fig. 2).

<img src="https://github.com/Daemiac/HTML_Gallery_Generator/blob/master/readme_images/HPG.png" width="400" height="550"><br>*Fig. 2 - the app ready to generate an instruction*

Clicking this button generates a file in HTML format inside previously chosen folder which contains gallery of robot assembly steps!

### Launch

You can start the app by copying the source code and running it with IDE. 
Requirements:
1. Python 3 (developed with 3.7 version)
2. Tkinter, os and time python libraries installed;

### Things I learned
This was my first serious python project which allowed me to practise such things as:
- working with standard library;
- making operations on lists;
- making operations on external files with use of 'os' module;
- catching and handling exceptions;
- creating GUI with Tkinter module;
- object oriented programming;

## License
![](https://img.shields.io/badge/License-MIT-informational?style=flat-square&logo=<>&logoColor=white&color=yellow)<br>
[MIT](https://choosealicense.com/licenses/mit/)
