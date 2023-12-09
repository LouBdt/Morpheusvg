This html code generated is mainly inspired by this https://jsbin.com/zeloziw/1/edit?html,css,js,output\n
So copyright (c) 2023 by ahmedam55 (http://jsbin.com/zeloziw/1/edit)\n
Released under the MIT license: http://jsbin.mit-license.org\n



\n
It uses http://snapsvg.io/docs/ to morph the files together\n
All I did was make a python script that scrapes the svg files to get the path data, put them all into a html file, then generate a JS script that loops the animations together\n




#===========HOW TO USE IT================\n
Simply download the .py file into your directory with the .svg files you want to morph. Doesn't matter how they are named as long as they have that .svg extension\n
If you open the .py file with a text editor, you can adjust:\n
  TRANSFO = "linear" #or linear, elastic, backout, backin, bounce depending on how you want the animation to look, more info on http://snapsvg.io/docs/#mina\n
  DURATION = 1000 #in ms the duration of the morphing process\n
  PAGENAME = "Animation" #the name of the HTML page\n
  HEAD = "What you want to write above your html page" #There is a text above, empty string if you want nothing\n
  FILE = "Hope it works this time" #the name of the html file generated\n
Then run the python code, it has no special requirements\n
It should generate a .html file (that could be veeeeery big depending on your svg files and how many there are\n

\n


#============DISCLAIMERS==================\n
The python script is creative common but I don't know if the original JS is as well. Use it carefully\n
I only had it to work with up to 15 SVG files, it freezes if you add more and it doesnt loop. It seems to be a problem with snap-svg but if you get to solve it, let me know !\n
I don't know anything about javascript, or object-oriented programmation, the code generated is widely suboptimal and I'm sorry for that, I did with what I could do\n
If you make fun animations with this script, don't hesitate to send me the result, I'd be happy to see it ! > charlie_brt@riseup.net\n
