import easygui
import easygui.boxes
 
easygui.msgbox("Bilibili:BobbxTYARJK Write.  Hello,World!", title=".NET installer")

import easygui
 
name = easygui.enterbox("What is your name?", title="Name Input")
easygui.msgbox(f"Hello, {name}!,Let's Contiune", title="Greeting,", ok_button="None")

import easygui
 
choices = [".NET 9.0 PRE", ".NET 8.0(always support)", ".NET 6.0",".NET 5.0 And more old version"]
choice = easygui.choicebox("Which .NET would you install?", choices=choices)
easygui.msgbox(f"You selected: {choice},Copy This Link:https://dotnet.microsoft.com/zh-cn/download/dotnet to install", title="INSTALL Selection")

import easygui

easygui.msgbox("Are you finish your download?",title=("Finish Download"),ok_button=("yes"))

import easygui

easygui.msgbox("Now you need open downloaded install program (Download Floder) in the C:/",title=("Install"))

import easygui
easygui.msgbox("Click Next and wait it for auto install",title="install")

import easygui
easygui.msgbox("If you Finish Install,You can exit,If you can't install,please do again or look for Professional peopleto install.",title="finish",ok_button="I know"\
    )