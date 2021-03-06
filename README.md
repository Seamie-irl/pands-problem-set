# Problem Set
##*Instructions for following the solutions*

**Student Name:** Seamus Leonard
<br>
**Student ID:** G00376550

### Introduction
In order to be able to view the solutions, you might like to have:
+ A GitHub account
+ Visual Studio Code (or other software which will display the code in the file e.g. Anaconda)
+ Knowledge on how to access the Windows Command Prompt (Command Line Interface) and how to run commands
+ Git - Git Bash

An <a href="#App">appendix</a> at the end of this document provides an outline on how to achieve the above criteria

However, as you're reading this, you're in GitHub and by clicking on the solutions as described below you can view the coding in this manner without having to install any software.

### The problem set
A set of ten problems were presented to the class during the winter semester of 2019 for the **Programming and Scripting** module of the Higher Diploma in Science in Data analytics. The list of questions can be viewed here. https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf

### The Questions and their corresponding Answers
<table>
    <tr>
        <th>Question</th>
        <th>Answer</th>
        <th>pre-Answer files</th>
    </tr>
    <tr>
        <td>Question 1: Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise1.py>Exercise 1</a></td>
        <td><a href=https://github.com/Seamie-irl/pands-problem-set/blob/master/sumupto.py>pre-complete 1</a></td>
    </tr>
    <tr>
        <td>Question 2: Write a program that outputs whether or not today is a day that begins with the letter T.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise2.py>Exercise 2</a></td>
        <td><a href=https://github.com/Seamie-irl/pands-problem-set/blob/master/begins-with-t.py>pre-complete 2a</a><br><a href=https://github.com/Seamie-irl/pands-problem-set/blob/master/secondQ.py>pre-complete 2b</a></td>
    </tr>
    <tr>
        <td>Question 3: Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise3.py>Exercise 3</a></td>
        <td><a href=https://github.com/Seamie-irl/pands-problem-set/blob/master/divisors.py>pre-complete 3</a></td>
    </tr>
    <tr>
        <td>Question 4: [Collatz] Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise4.py>Exercise 4</a></td>
        <td><a href=https://github.com/Seamie-irl/pands-problem-set/blob/master/collatz.py>pre-complete 4</a></td>
    </tr>
    <tr>
        <td>Question 5: Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise5.py>Exercise 5</a></td>
        <td></td>
    </tr>
    <tr>
        <td>Question 6: Write a program that takes a user input string and outputs every second word.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise6.py>Exercise 6</a></td>
        <td><a href=https://github.com/Seamie-irl/pands-problem-set/blob/master/secondstring.py>pre-complete 6</a></td>
    </tr>
    <tr>
        <td>Question 7: Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise7.py>Exercise 7</a></td>
        <td><a href=https://github.com/Seamie-irl/pands-problem-set/blob/master/squareroot.py>pre-complete 7</a></td>
    </tr>
    <tr>
        <td>Question 8: Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise8.py>Exercise 8</a></td>
        <td><a href=https://github.com/Seamie-irl/pands-problem-set/blob/master/datetimeQ.py>pre-complete 8</a></td>
    </tr>
    <tr>
        <td>Question 9: Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise9.py>Exercise 9</a></td>
        <td></td>
    </tr>
    <tr>
        <td>Question 10: Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].</td>
        <td><a href= https://github.com/Seamie-irl/pands-problem-set/blob/master/Exercise10.py>Exercise 10</a></td>
        <td></td>
    </tr>
</table>

### My solutions - background
I have been programming / scripting in one form or another for over 30 years, mostly for personal enjoyment. However, in the last two decades I've also used it for work. My experience is in Visual Basic and SQL though I've also dipped a toe into C++ and MS-DOS batch scripts. As a result of this, a lot of my solutions were trial-and-error. Perhaps not the most efficient method but certainly the most enjoyable and rewarding. I generally created my code and debugged it as I went along. The biggest issue were the minor syntax changes from language to language (for example, placing a colon at the end of loop statement lines). Only when I'd been unable to work out the syntax of code, or indeed the code itself did I search online. Depending on my need at the time I'd either use the Python or StackOverflow websites (see references)

### My solutions - hierarchy
Initially, as I worked on each solution in turn I saved the file with the same filename in the question. However, this created a problem with question 8 where the filename suggested was 'datetime.py'. DateTime is a reserved word so I reverted to identifying each question by Exercise Number.

### My solutions - each solution
Each file beginning with the text 'Exercise' is the solution to the associated numbered question.

At the top of each file I have commented the question and a brief outline of my approach. Thereafter, I have broken the solution into parts and commented to explain the process.

### My Solutions - References
Where I've directly used code in my solutions, the link to the source of the code is commented.

<h2 id="App"> Appendix 1 </h2>

This appendix is neither meant to be a tutorial nor a primer for using software. However, the headings below set out the start-points for using the resources I used in completing the above questions.

### GitHub
The fact that you're reading this suggests not alone are you aware of GitHub but that you've navigated your way through the site at some level. However, should you wish to create your own account, please see <a href=https://github.com>GitHub</a>

### Visual Studio Code
Visual Studio Code (VS) is a code editor redefined and optimised for building and debugging modern web and cloud applications (https://code.visualstudio.com). It can be downloaded <a href=https://code.visualstudio.com/download>from here</a>

Once downloaded, you can run the software by looking for it in your program list with the icon <img src=https://c616b3614506f07e89ab-5cef763fe73fcec814d61b3b60a1ac9a.ssl.cf1.rackcdn.com/V1~113244e0-0b02-4a41-9fb2-1f39e5c5e6a4~952dc796a8d745b2b7968c50b0bcee30 width=50>

A good reference for learning Python code is Python.Org's own documents and tutorials which can be found <a href=https://docs.python.org/3>here</a>

### Windows Command Prompt
The Command Prompt (Cmd) can be accessed on Windows either by searching for it or finding it in your Start Menu under the <Windows System> folder. When searching for it, 'cmd' is usually enough to find it.

Once in Cmd, you should navigate through your directories to where you will be storing your python .py files using cd to change directory and dir to list what's in the directory you're currently in.

### Git
Using Git is an ideal way to keep track of the progress of your coding and for synchonising your local files and folders with GitHub. This software can be downloaded <a href=https://git-scm.com/downloads>here</a> with instructions for using the software <a href=https://git-scm.com/book/en/v2>here</a>