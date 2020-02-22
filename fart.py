import os
import threading
import time
import sys
import math
from math import *
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import random
import sys


from tkinter import messagebox


def clear():
    os.system("cls")

def exit():
    sys.exit()

class module_manager:
    def __init__(self):
        self.modules = []
    def add(self,inp):
        self.modules.append(inp)

ModuleManager = module_manager()

modules = []
erroring = True
code = []
stringcount = 1
while True:
    clear()
    print("Programming language:")
    print("1.Write code")
    print("2.Read code")
    print("3.Exit")
    i = input(">")

    if i == "1":
        clear()
        print("Write code:")
        while True:
            comm = input(str(stringcount) + ".")
            stringcount += 1
            if comm == "return":
                break
            code.append(comm)
        break

    elif i == "2":
        print("Enter path:")
        path = input(">")
        if os.path.exists(path) != True:
            print("Wrong!")
            time.sleep(1)

        else:
            o = open(path,"r")

            for line in o:
                l = list(line)

                for a in range(len(l)):
                    if l[a] == "\n":
                        l[a] = ""

                ln = "".join(l)
                code.append(ln)

            o.close()
            print("Succses!")
            time.sleep(1)
            break
            

    elif i == "3":
        exit()

def export(module):
    global ModuleManager
    if(module == "window"):
        try:
            import window
            from window import inputbox
            ModuleManager.add(inputbox)
            ModuleManager.add(window.ask)
            ModuleManager.add(window.error)
            ModuleManager.add(window.info)
            ModuleManager.add(window.warning)
            ModuleManager.add(window.okcancel)
            modules.append(module)
            
        except:
            print('A problem with module "window". Please download it.')
            input(">")
            exit(0)

    else:
        print("Unknown module.")

def error(n):
    global erroring
    if(erroring):
        print("Detected error in " + str(n + 1) + "th string.")



def check(variab):
    itis = False

    for i in vars:
        if vars.name == variab.name:
            itis = True

    if itis == True:
        return True

    else:
        return False
class reqest:
    next = True
    string =0
    breaking = False
class variable:
    type = "unknown"
    forint = 0
    forstring = ""
    forbool = False
    created = False
    id = 0
    name = ""

variables = []
slashnew = variable()
slashnew.name = "newline"
slashnew.forstring = "\n"
slashnew.type = "string"
variables.append(slashnew)

def compilate(command,r):
    global variables
    global modules
    global erroring
    n = r.string
    if command == "\n" or command == "" or command[0] == "/":
        n+=1
        r.string = n
        return r
    if command == "end":
        r.next = True
        n+=1
        r.string = n

        return r

    if r.next == True:
        method = ""
        args = []
        arg_coodinate = -1
        d = list(command)
        for i in range(len(d)):
            if d[i] == " ":
                d[i] = ""
        command = "".join(d)
        for i in range(len(command)):
            if command[i] == "(":
                arg_coodinate = i
                break

            
            method += command[i]

        try:
            if arg_coodinate != -1:
                args_raw = []

                if command.find(")",0,len(command)) == -1:
                    error(n)
                    return r
                

                j = ""
                arg_string = ""

                for i in range(arg_coodinate, len(command)):
                    arg_string += command[i]

                

                arg_list = list(arg_string)

                arg_list.pop(0)
                i = len(arg_list) -1
                while i >= 0:
                    if arg_list[i] == ")":
                        arg_list.pop(i)
                        break
                    
                    i -= 1

                arg_string = "".join(arg_list)

                
                j = ""
                
                arg_string += ","
                
                for i in arg_string:
                    if i == ",":
                        args_raw.append(j)
                        j = ""
                        continue

                    j += i

                


                for i in args_raw:
                    if i[0] == "&":
                        y = list(i)
                        y.pop(0)
                        s="".join(y)

                        names = []

                        for i in variables:
                            names.append(i.name)
                        id = -1
                        for i in range(len(names)):
                            if names[i] == s:
                                id = i
                                break
                        if id != -1:
                            if variables[id].type == "int":
                                args.append(variables[id])
                            else:
                                error(n)

                        elif id == -1:
                            error(n)

                    elif i[0] == "$":
                        
                        y = list(i)
                        y.pop(0)
                        s="".join(y)

                        names = []
                        

                        for i in variables:
                            names.append(i.name)
                        id = -1
                        for i in range(len(names)):
                            if names[i] == s:
                                id = i
                                break
                        
                        if id != -1:
                            if variables[id].type == "string":

                                args.append(variables[id])
                            else:
                                error(n)

                        elif id == -1:
                            error(n)

                    elif i[0] == "#":
                        y = list(i)
                        y.pop(0)

                        for i in range(len(y)):
                            if y[i] == "_":
                                y[i] = " "
                        

                        s="".join(y)

                        try:
                            d = variable()
                            d.forstring = s
                            d.name = "Added_String"
                            d.type = "string"
                            args.append(d)

                        except:
                            error(n)

                    elif i[0] == ":":
                        y = list(i)
                        y.pop(0)
                        s="".join(y)

                        try:
                            d = variable()
                            d.forint = int(s)
                            d.name = "Added_Int"
                            d.type="int"
                            args.append(d)

                        except:
                            error(n)

                    elif i[0] == "*":
                        y = list(i)
                        y.pop(0)
                        s="".join(y)

                        try:
                            d = variable()
                            if(s == "true"):
                                d.forbool = True
                            elif s == "false":
                                d.forbool = False
                            else:
                                error(n)
                                d.forbool = False
                            d.name = "Added_Bool"
                            d.type="bool"
                            args.append(d)

                        except:
                            error(n)

                    elif i[0] == "!":
                        y = list(i)
                        y.pop(0)
                        s="".join(y)
                        id = -1
                        for i in range(len(variables)):
                            if(variables[i].type == "bool" and variables[i].name == s):

                                id = i
                                break

                        if(id == -1):
                            error();
                            continue

                        args.append(variables[id])

                    elif i[0] == "^":
                        y = list(i)
                        y.pop(0)
                        s="".join(y)
                        try:
                            name = ""
                            was = False

                            for i in range(len(variables)):
                                if(variables[i].type == "string"):
                                    if(variables[i].name == s):
                                        name = variables[i].forstring
                                        
                                        was= True
                                        break

                            if(was == False):
                                error(n)
                                continue                         


                            id = -1
                            for i in range(len(variables)):
                                
                                if(variables[i].name == name):
                                    id = variables[i].id
                                    break
                            
                            if(id == -1):
                                error(n)
                                continue
                            else:
                                args.append(variables[id])

                        except:
                            error(n)                                



                    else:
                        error(n)

        except:
            pass

        if method == "printf":
            if len(args) > 0:
                for i in args:
                    if i.type == "int":

                        print(str(i.forint),end='')
                    elif i.type=="string":
                        print(i.forstring,end='')
                    elif i.type == "bool":
                        if(i.forbool == True):
                            print("true",end='')
                        else:
                            print("false",end='')
                    else:
                        error(n)
            else:
                error(n)

        elif method == "newline":
            if len(args) > 0:
                print("")
                for i in args:
                    if i.type == "int":

                        print(str(i.forint),end='')
                    elif i.type=="string":
                        print(i.forstring,end='')
                    else:
                        error(n)
            else:
                print("")

        elif method == "new_int":
            if len(args) >= 1 and len(args) <= 2:
                if args[0].type=="string":
                    name = args[0].forstring
                    forint = 0
                    if(len(args) > 1 and args[1].type == "int"):
                        forint = args[1].forint

                    names = []

                    for i in variables:
                        names.append(i.name)

                    if name not in names:
                        vr = variable()
                        vr.type = "int"
                        vr.created = True
                        vr.name = name
                        vr.forstring = ""
                        vr.forint = forint
                        vr.id = len(variables)
                        variables.append(vr)
                    else:
                        error(n)
                else:
                    error(n)

            else:
                error(n)

        elif method == "new_string":
            if len(args) >= 1 and len(args) <= 2:
                if args[0].type=="string":
                    name = args[0].forstring
                    forstr = ""
                    if(len(args) == 2 and args[1].type == "string"):
                        forstr = args[1].forstring

                    names = []

                    for i in variables:
                        names.append(i.name)

                    if name not in names:
                        vr = variable()
                        vr.type = "string"
                        vr.name = name
                        vr.created = True
                        vr.forstring = ""
                        vr.id = len(variables)
                        vr.forstring = forstr
                        variables.append(vr)
                    else:
                        error(n)
                else:
                    error(n)

            else:
                error(n)

        elif method == "sleep":
            if len(args) == 1:
                if args[0].type == "int":
                    time.sleep(args[0].forint)

                else:
                    error(n)
            else:
                error(n)

        elif method == "clear":
            if len(args) == 0:
                clear()
            else:
                error(n)

        elif method == "exit":
            sys.exit(0)
        
        elif method == "plus":
            if len(args) > 1:
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1

                    else:
                        other += 1

                if other > 0 or ints > 0 and strings > 0:
                    error(n)
                    

                else:
                    if args[0].created == True:
                        if ints > 0:
                            
                            for i in range(1,len(args)):
                                variables[args[0].id].forint += args[i].forint

                        elif strings > 0:
                            for i in range(1,len(args)):
                                variables[args[0].id].forstring += args[i].forstring
                        
                        else:
                            error(n)
                            
                    else:
                        error(n)
                        

            else:
                error(n)
                
        elif method == "minus":
            if len(args) > 1:
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1

                    else:
                        other += 1

                if other > 0 or ints > 0 and strings > 0 or strings>0:
                    error(n)
                    

                else:
                    if args[0].created == True:
                        if ints > 0:
                            
                            for i in range(1,len(args)):
                                variables[args[0].id].forint -= args[i].forint

                        else:
                            error(n)
                            
                    else:
                        error(n)
                        

            else:
                error(n)
                
        elif method == "devide":
            if len(args) > 1:
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1

                    else:
                        other += 1

                if other > 0 or ints > 0 and strings > 0 or strings>0:
                    error(n)
                    

                else:
                    if args[0].created == True:
                        if ints > 0:
                            
                            for i in range(1,len(args)):
                                variables[args[0].id].forint /= args[i].forint

                        else:
                            error(n)
                            
                    else:
                        error(n)
                        

            else:
                error(n)
                    
        elif method == "multiply":
            if len(args) > 1:
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1

                    else:
                        other += 1

                if other > 0:
                    error(n)
                    

                else:
                    if args[0].created == True:
                        if ints > 0 and strings == 0:
                            
                            for i in range(1,len(args)):
                                variables[args[0].id].forint *= args[i].forint
                        elif strings > 0 and ints > 0:
                            if len(args) == 2:
                                if args[0].type == "string" and args[1].type == "int":
                                    
                                    variables[args[0].id].forstring *= args[1].forint

                                else:
                                    error(n)
                                    
                            else:

                                error(n)


                        else:
                            error(n)
                            
                    else:
                        error(n)
                        

            else:
                error(n)

        elif method == "sqrt":
            if len(args) == 1 :
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1

                    else:
                        other += 1

                if other > 0 or strings > 0:
                    error(n)
                    

                else:
                    if args[0].created == True:
                        if ints > 0:
                            
                            
                            variables[args[0].id].forint = sqrt(variables[args[0].id].forint)

                        else:
                            error(n)
                            
                    else:
                        error(n)


            else:
                error(n)

        elif method == "power":
            if len(args) == 2 :
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1

                    else:
                        other += 1

                if other > 0 or strings > 0:
                    error(n)
                    

                else:
                    if args[0].created == True:
                        if ints > 0:
                            
                            
                            variables[args[0].id].forint = pow(variables[args[0].id].forint,args[1].forint)

                        else:
                            error(n)
                            
                    else:
                        error(n)
                        

            else:
                error(n)
                
        elif method == "equal":
            if len(args) == 2 :
                strings = 0
                ints = 0
                bools = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1
                    elif i.type == "bool":
                        bools += 1
                    else:
                        other += 1

                if other > 0:
                    error(n)
                    

                else:
                    if args[0].created == True:
                        if args[0].type == "int" and args[1].type == "string":
                            variables[args[0].id].forint = len(args[1].forstring)
                        elif args[0].type == "int" and args[1].type == "int":
                            variables[args[0].id].forint = args[1].forint
                        elif args[0].type == "bool" and args[1].type == "bool":
                            variables[args[0].id].forbool = args[1].forbool
                        elif args[0].type == "string" and args[1].type == "string":
                            variables[args[0].id].forstring = args[1].forstring

                        elif args[0].type == "int" and args[1].type == "bool":
                            if(args[1].forbool == True):
                                variables[args[0].id].forint = 1
                            else:
                                variables[args[0].id].forint = 0
                        elif args[0].type == "string" and args[1].type == "bool":
                            if(args[1].forbool == True):
                                variables[args[0].id].forstring = "true"
                            else:
                                variables[args[0].id].forstring = "false"
                        elif args[0].type == "bool" and args[1].type == "int":
                            if(args[1].forint > 0):
                                variables[args[0].id].forbool = True

                            else:
                                variables[args[0].id].forbool = False


                        else:
                            error(n)
                            
                    else:
                        error(n)
                        
            else:
                error(n)
                
        elif method == "factorial":
            if len(args) == 2:
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1

                    else:
                        other += 1

                if other > 0 or strings > 0:
                    error(n)
                    

                else:
                    if args[0].created == True:
                        if ints > 0:
                            

                            variables[args[0].id].forint = factorial(args[1].forint)

                        else:
                            error(n)
                            
                    else:
                        error(n)
                        

            else:
                error(n)

        elif method == "to_int":
            if len(args) == 2:
                if args[0].type == "int" and args[1].type == "string":
                    if args[0].created == True:
                        try:
                            variables[args[0].id].forint = int(args[1].forstring)

                        except:
                            error(n)
                            
                    else:
                        error(n)
                        
                else:
                    error(n)
                    
            else:
                error(n)
                    
        elif method == "to_string":
            if len(args) == 2:
                if args[0].type == "string" and args[1].type == "int":
                    if args[0].created == True:
                        try:
                            variables[args[0].id].forstring = str(args[1].forint)

                        except:
                            error(n)
                            
                    else:
                        error(n)
                        
                else:
                    error(n)
                    
            else:
                error(n)
                
        elif method == "write":
            if len(args) >= 1:
                id = args[0].id
                stringforshow = ""
                for i in range(1,len(args)):
                    if args[i].type == "string":
                        stringforshow += args[i].forstring
                    elif args[i].type == "int":
                        stringforshow += str(args[i].forint)

                if args[0].type == "int":
                    try:
                        variables[id].forint = int(input(stringforshow))
                    except:
                        error(n)
                        
                elif args[0].type == "string":
                    variables[id].forstring = input(stringforshow)
            else:
                error(n)
                
        elif method == "if":
            
            if len(args) == 3:
                
                if args[1].type == "string":
                    if args[1].forstring == "=":
                        if args[0].type == "int" and args[2].type == "int":
                            if args[0].forint == args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "string" and args[2].type == "string":
                            if args[0].forstring == args[2].forstring:
                                pass
                            else:
                                r.next=False
                        elif args[0].type == "string" and args[2].type == "int":
                            if len(args[0].forstring) == args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "int" and args[2].type == "string":
                            if args[0].forint == len(args[2].forstring):
                                pass
                            else:
                                r.next=False

                        elif args[0].type == "bool" and args[2].type == "bool":
                            if(args[0].forbool == args[2].forbool):
                                pass
                            else:
                                r.next = False
                        else:
                            error(n)                                                 
                    
                    elif args[1].forstring == ">":
                        if args[0].type == "int" and args[2].type == "int":
                            if args[0].forint > args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "string" and args[2].type == "string":
                            if len(args[0].forstring) > len(args[2].forstring):
                                pass
                            else:
                                r.next=False
                        elif args[0].type == "string" and args[2].type == "int":
                            if len(args[0].forstring) > args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "int" and args[2].type == "string":
                            if args[0].forint > len(args[2].forstring):
                                pass
                            else:
                                r.next=False       
                        else:
                            error(n)                    

                    elif args[1].forstring == "<":
                        if args[0].type == "int" and args[2].type == "int":
                            if args[0].forint < args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "string" and args[2].type == "string":
                            if len(args[0].forstring) < len(args[2].forstring):
                                pass
                            else:
                                r.next=False
                        elif args[0].type == "string" and args[2].type == "int":
                            if len(args[0].forstring) < args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "int" and args[2].type == "string":
                            if args[0].forint < len(args[2].forstring):
                                pass
                            else:
                                r.next=False   
                        else:
                            error(n)

                    elif args[1].forstring == "!=":
                        if args[0].type == "int" and args[2].type == "int":
                            if args[0].forint != args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "string" and args[2].type == "string":
                            if args[0].forstring != args[2].forstring:
                                pass
                            else:
                                r.next=False
                        elif args[0].type == "string" and args[2].type == "int":
                            if len(args[0].forstring) != args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "int" and args[2].type == "string":
                            if args[0].forint != len(args[2].forstring):
                                pass
                            else:
                                r.next=False   
                        else:
                            error(n)

                    elif args[1].forstring == ">=":
                        if args[0].type == "int" and args[2].type == "int":
                            if args[0].forint >= args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "string" and args[2].type == "string":
                            if len(args[0].forstring) >= len(args[2].forstring):
                                pass
                            else:
                                r.next=False
                        elif args[0].type == "string" and args[2].type == "int":
                            if len(args[0].forstring) >= args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "int" and args[2].type == "string":
                            if args[0].forint >= len(args[2].forstring):
                                pass
                            else:
                                r.next=False 

                        else:
                            error(n)  

                    elif args[1].forstring == "<=":
                        if args[0].type == "int" and args[2].type == "int":
                            if args[0].forint <= args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "string" and args[2].type == "string":
                            if len(args[0].forstring) <= len(args[2].forstring):
                                pass
                            else:
                                r.next=False
                        elif args[0].type == "string" and args[2].type == "int":
                            if len(args[0].forstring) <= args[2].forint:
                                pass
                            else:
                                r.next=False
                        
                        elif args[0].type == "int" and args[2].type == "string":
                            if args[0].forint <= len(args[2].forstring):
                                pass
                            else:
                                r.next=False   
                        else:
                            error(n)
                
                    else:
                        error(n)
                                              
                else:
                    error(n)
                    
            else:
                error(n)
                
        elif method == "clear_var":
            if len(args) == 1:
                if args[0].created:
                    variables[args[0].id].forint = 0
                    variables[args[0].id].forstring = ""
                    variables[args[0].id].forbool = False
                else:
                    error(n)
                    

            else:
                error(n)
                
        elif method == "hide_errors":
            erroring = False
        elif method == "return_errors":
            erroring = True
   
        elif method == "find":
            if len(args) == 3:
                if args[0].type == "int" and args[1].type == "string" and args[2].type == "string":
                    count = 0

                    for i in args[1].forstring:
                        if i == args[2].forstring:
                            count += 1

                    if args[0].created == True:
                        args[0].forint = count
                else:
                    error(n)
                    
            else:
                error(n)
                
        elif method == "file":
            if len(args) >= 3:
                if args[0].type == "string" and args[1].type == "string":
                    if args[0].forstring == "insert":
                        o = open(args[1].forstring,"w")

                        for i in range(2,len(args)):
                            if args[i].type == "int":
                                o.write(str(args[i].forint))
                            elif args[i].type == "string":
                                o.write(args[i].forstring)

                        o.close()

                    elif args[0].forstring == "get":
                        if len(args) == 3:
                            try:
                                o = open(args[1].forstring,"r")
                                if args[2].created:
                                    if args[2].type == "int":
                                        try:
                                            variables[args[2].id].forint = int(o.read())

                                        except:
                                            error(n)
                                            

                                    elif args[2].type == "string":
                                        variables[args[2].id].forstring = o.read()

                                    else:
                                        error(n)


                                else:
                                    error(n)
                                    
                            except:
                                error(n)



                    elif args[0].forstring == "add":
                        try:
                            o = open(args[1].forstring,"a")

                            for i in range(2,len(args)):
                                if args[i].type == "int":
                                    o.write(str(args[i].forint))
                                elif args[i].type == "string":
                                    o.write(args[i].forstring)

                            o.close()
                        except:
                            error(n)
                            

                else:
                    error(n)
                    

            else:
                error(n)

        elif method == "delete":
            if len(args) == 1:
                if args[0].created:
                    

                    for i in range(args[0].id + 1, len(variables)):
                        variables[i].id -= 1

                    variables.pop(args[0].id)
                else:
                    error(n)
                    

            else:
                error(n)

        elif method == "new_bool":
            if len(args) >= 1 and len(args) <= 2:
                if args[0].type=="string":
                    name = args[0].forstring
                    names = []

                    for i in variables:
                        names.append(i.name)

                    if name not in names:
                        vr = variable()
                        vr.type = "bool"
                        vr.created = True
                        vr.name = name
                        vr.forstring = ""
                        vr.forint = 0
                        if len(args) == 2 and args[1].type == "bool":
                            vr.forbool = args[1].forbool
                        

                        vr.id = len(variables)
                        variables.append(vr)
                    else:
                        error(n)
                else:
                    error(n)

            else:
                error(n)

        elif method == "restart":
            erroring = True
            r.next = True
            r.string = 0
            
        elif method == "toline":
            if len(args) == 1:
                if args[0].type == "int":
                    if args[0].forint - 1 >= 0:
                        n = args[0].forint - 1
                        r.string = n
                        return r
                    else:
                        error(n)
                        

                else:
                    error(n)
                    

            else:
                print("Error!")
                    
        elif method == "getline":
            if len(args) == 1:
                if args[0].type == "int":
                    args[0].forint = n + 1

                else:
                    error(n)
                    

            else:
                error(n)
            
        elif method == "browse":
            if len(args) >= 1:
                stringforsearch = ""

                for i in args:
                    if i.type == "int":
                        stringforsearch += str(i.forint)
                    elif i.type == "string":
                        stringforsearch += i.forstring
                
                sa = list(stringforsearch)
                for i in range(len(sa)):
                    if sa[i] == " ":
                        sa[i] = "+"

                stringforsearch = "".join(sa)

                webbrowser.open_new_tab("https://www.google.com/search?q=" + stringforsearch)

            else:
                error(n)
                        
        elif method == "browse_open":
            if len(args) >= 1:
                stringforsearch = ""

                for i in args:
                    if i.type == "int":
                        stringforsearch += str(i.forint)
                    elif i.type == "string":
                        stringforsearch += i.forstring

                sa = list(stringforsearch)
                for i in range(len(sa)):
                    if sa[i] == " ":
                        sa[i] = "+"

                stringforsearch = "".join(sa)

                webbrowser.open_new_tab(stringforsearch)

            else:
                error(n)
                
        elif method == "random":
            if len(args) == 3:
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1
                    else:
                        other += 1

                if ints > 0 and strings == 0 and other == 0:
                    if args[0].created == True:
                        variables[args[0].id].forint = random.randint(args[1].forint,args[2].forint)
                    else:
                        error(n)
                        

                else:
                    error(n)
                    
            else:
                error(n)
                
        elif method == "break":
            r.breaking = True
            return r
    
        elif method == "getchar":
            if len(args) == 3:
                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1
                    else:
                        other += 1

                if ints == 1 and strings == 2 and other == 0:
                    try:
                        variables[args[0].id].forstring = args[1].forstring[args[2].forint - 1]

                    except:
                        error(n)
                        

                else:
                    error(n)
                    
            else:
                error(n)
                   
        elif method == "replace":
            if len(args) == 3:
                if args[0].type == "string" and args[1].type == "string" and args[2].type == "string":

                    pinto = list(args[0].forstring)
                    for i in range(len(pinto)):
                        if pinto[i] == args[1].forstring:
                            pinto[i] = args[2].forstring
                    
                    variables[args[0].id].forstring = "".join(pinto)

                else:
                    error(n)
                    
            else:
                error(n)
                
        elif method == "send_mail":
            
            if len(args) == 6:

                strings = 0
                ints = 0
                other = 0

                for i in args:
                    if i.type == "int":
                        ints += 1

                    elif i.type == "string":
                        strings += 1
                    else:
                        other += 1

                if strings > 0 and ints == 0 and other == 0:
                    try:
                        client = args[0].forstring
                        buti = args[1].forstring
                        msg = MIMEMultipart()
                        msg['From'] = client
                        msg['To'] = buti
                        msg['Subject'] = args[2].forstring
                        body = args[3].forstring
                        msg.attach(MIMEText(body, 'plain'))
                        server = smtplib.SMTP('smtp.' + args[5].forstring)
                        server.starttls()
                        server.login(client,args[4].forstring)
                        text = msg.as_string()
                        server.sendmail(client,buti, text)
                        server.quit()
                    except:
                        error(n)
                        
                else:
                    error(n)
                    

            else:
                error(n)
                
        elif method == "mail_help":
            print("SendMail-command structure:")
            print("send_mail(from,to,subject,message,login,protocol)")
            print("For protocol you can try: yandex.ru, google.com and other.")
            print("You can catch some problems, if you try with google.com.")
            
        elif method == "inputbox":
            if(len(args) == 4):
                if(args[0].type == "int" or args[0].type == "string"):
                        if(args[1].type == "string" and args[2].type == "string" and args[3].type == "int"):
                            if("window" in modules):
                                info = ModuleManager.modules[0](titles = args[1].forstring,texts = args[2].forstring,fontsizes = args[3].forint)
                                if(args[0].created == True):
                                    if(args[0].type == "int"):
                                        try:
                                            variables[args[0].id].forint = int(info)
                                        except:
                                            error(n)
                                    elif args[0].type == "string":
                                        variables[args[0].id].forstring = info;
                                else:
                                    error(n)
                            else:
                                error(n)


                        else:
                            error(n)

                else:
                    error(n)
            
            else:
                error(n)

        elif method == "connect":
            if(len(args) == 1):
                if(args[0].type == "string"):
                    export(args[0].forstring)
                else:
                    error(n)
            else:
                error(n)

        elif method == "ask":
            if(len(args) == 3):
                if(args[0].type == "bool" and args[1].type == "string" and args[2].type == "string"):
                    if(args[0].created == True):
                        if("window" in modules):
                            bool = ModuleManager.modules[1](titles = args[1].forstring,texts = args[2].forstring)
                            variables[args[0].id].forbool = bool
                        else:
                            error(n)
                    else:
                        error(n)
                else:
                    error(n)
            else:
                error(n)
                    
        elif method == "show_error":
            if(len(args) == 2):
                if("window" in modules):
                    if(args[0].type =="string" and args[1].type == "string"):
                        ModuleManager.modules[2](titles = args[0].forstring,texts = args[1].forstring)
                    else:
                        error(n)
                else:
                    error(n)
            else:
                error(n)
        elif method == "show_info":
            if(len(args) == 2):
                if("window" in modules):
                    if(args[0].type =="string" and args[1].type == "string"):
                        ModuleManager.modules[3](titles = args[0].forstring,texts = args[1].forstring)
                    else:
                        error(n)
                else:
                    error(n)
            else:
                error(n)
        elif method == "show_warning":
            if(len(args) == 2):
                if("window" in modules):
                    if(args[0].type =="string" and args[1].type == "string"):
                        ModuleManager.modules[4](titles = args[0].forstring,texts = args[1].forstring)
                    else:
                        error(n)
                else:
                    error(n)
            else:
                error(n)
        elif method == "ask_ok_cancel":
            if(len(args) == 3):
                if(args[0].type == "bool" and args[1].type == "string" and args[2].type == "string"):
                    if(args[0].created == True):
                        if("window" in modules):
                            bool = ModuleManager.modules[5](titles = args[1].forstring,texts = args[2].forstring)
                            variables[args[0].id].forbool = bool
                        else:
                            error(n)
                    else:
                        error(n)
                else:
                    error(n)
            else:
                error(n)
                    


        else:
            print("Error(" + str(n+1) + "): Unknown command")
            
        
    r.string += 1
    r.breaking = False
    return r

    
                    
            

req = reqest()


while req.string < len(code):
    req = compilate(code[req.string],req)
    
    if(req.breaking == True):
        break 



input("\nPress RETURN to exit...")










