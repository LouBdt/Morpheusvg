#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:35:06 2023

@author: lou
"""
#==============================================
TRANSFO = "linear" #or linear, elastic, backout, backin, bounce
DURATION = 1000 #in ms
PAGENAME = "Animation"
HEAD = "What you want to write above your html page"
FILE = "Hope it works this time" #the name of the html file generated
#==============================================



ALPHA = "abcdefghijklmnopqrstuvwxyz"
ALPHA+=ALPHA.upper()
VAR = list(ALPHA)+["a"+ALPHA[i] for i in range(len(ALPHA))]

import os
allcorps = []
ind = 0
#Importing all SVG files in the cwd and extracting only the code of the paths
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".svg"):
        print(filename)
        with open(filename, 'r') as f:
            text=f.readlines()
        corps = []
        i=0
        while not text[i].startswith('        d='):
            i+=1
        for j in range(i,len(text)):
            corps.append(text[j])
            if text[j].endswith(" />\n"):
                break
            
        allcorps.append(corps)
        ind+=1

preambule=['<!DOCTYPE html>\n', '<!--\n', 'Created using JS Bin\n', 'http://jsbin.com\n', '\n', 'Copyright (c) 2023 by ahmedam55 (http://jsbin.com/zeloziw/1/edit)\n', '\n', 'Released under the MIT license: http://jsbin.mit-license.org\n', '-->\n', '<meta name="robots" content="noindex">\n', '<html>\n', '<head>\n', '  <meta charset="utf-8">\n', '  <meta name="viewport" content="width=device-width">\n', '  <title>{PN}</title>\n'.format(PN = PAGENAME), '<style id="jsbin-css">\n', 'h1{\n', '  text-align:center;\n', '}\n', 'svg {\n', '    display: block;\n', '    margin: 0 auto;\n', '}\n', '</style>\n', '</head>\n', '<body>\n', "<h1>{h}</h1>\n".format(h = HEAD), '  \n', '<svg xmlns="http://www.w3.org/2000/svg" id="cups"\n', '     width="10in" height="10in"\n', '     viewBox="0 0 1000 1000">\n']
header = ['  <path id="{ID}"\n', '        fill="black" stroke="black" stroke-width="0"\n']
footer1 = ['\n', '</svg>\n', '  \n', '  <script src="https://cdnjs.cloudflare.com/ajax/libs/snap.svg/0.5.1/snap.svg-min.js"></script>\n', '<script id="jsbin-javascript">\n', 'var svg = document.getElementById("cups");\n', 'var s = Snap(svg);\n', '\n']
footer2 = ['</script>\n', '</body>\n', '</html>\n']


ind = 0
vardec = []
with open(FILE+".html", 'w') as f: 
    f.writelines(preambule)
    premiter = 0
    for ind in range(len(allcorps)):
        char = VAR[ind]

        for line in header:
            if line.startswith("  <path id="):
                if premiter == 0:
                    f.write("  <path id=\"a\"\n")
                    f.write("        fill=\"None\" stroke=\"black\" stroke-width=\"10\"\n")
                    premiter+=1
                else:
                    f.write("  <path opacity=\"0\" id=\"{ID}\"\n".format(ID = char))
                    f.write("        fill=\"None\" stroke=\"black\" stroke-width=\"0\"\n")   

        for line in allcorps[ind]:
            f.write(line)
            
        st = "var {varname} = Snap.select(\'#{name}\');\n".format(varname = char+"Cup", name=char)
        vardec.append(st)
    f.write("</svg>")
    
    for line in footer1:
        f.write(line)
    for line in vardec:
        f.write(line)
    f.write("\n")
    for ind in range(len(allcorps)):
        t = "var {ccp} = {cc}.node.getAttribute('d');\n".format(ccp = VAR[ind]+"CupPoints", cc = VAR[ind]+"Cup")
        f.write(t)
    for ind in range(len(allcorps)-1):
        curchar = VAR[ind]
        nextchar = VAR[ind+1]
        line = "var to{cc} = function(){{\n".format(cc= curchar)
        f.write(line)
        line = "    aCup.animate({{ d : {ncP} }}, {dur}, mina.{trans}, to{nc});\n".format(ncP = nextchar+"CupPoints", dur = DURATION, trans = TRANSFO, nc = nextchar)
        f.write(line)
        f.write("}\n")
        f.write("\n")
    
    line = "var to{cc} = function(){{\n".format(cc= VAR[len(allcorps)-1])
    f.write(line)
    line = "    aCup.animate({{ d : aCupPoints }}, {dur}, mina.{trans}, toa);\n".format(dur = DURATION, trans = TRANSFO)
    f.write(line)
    f.write("}\n")
    f.write("\n")
#        char = VAR[ind]
#        varnam = char+'Cup'
#        st = "var {varnamepoint} = {varname}.node.getAttribute('d');\n".format(varnamepoint = varnam+"Points",  varname = varnam, name=char)
#        f.write(st)
#    f.write("var to{nextvar} = function(){{\n".format(nextvar='a'))
#    ncp = VAR[len(allcorps)-1]+'Cup'+'Points'
#    f.write("  {simpleCup}.animate({{ d: {nextcuppoint} }}, {dur}, mina.{trans}, to{curvar});\n".format(dur = DURATION, simpleCup = 'aCup', nextcuppoint = ncp, trans = TRANSFO, curvar = 'b'))
#    f.write("}\n")
#    for ind in range(len(allcorps)-1):
#        char = VAR[ind]
#        varnam = char+'Cup'
#        ncp = VAR[ind+1]+'Cup'+'Points'
#        f.write("var to{nextvar} = function(){{\n".format(nextvar=VAR[ind+1]))
#        f.write("  {simpleCup}.animate({{ d: {nextcuppoint} }}, {dur}, mina.{trans}, to{curvar});\n".format(dur = DURATION, simpleCup = varnam, nextcuppoint = ncp, trans = TRANSFO,curvar = VAR[ind]))
#        f.write("}\n")
#    
    f.write('toa();\n')
#    
    f.writelines(footer2)
        