# -*- coding: utf-8 -*-
'此类是启动和初始化类，控制着开始'
__author_ = 'ly'

#sys
import os
import sys
import AnalysisOneStock
import ConfigManegment
import tkinter as tk

class MainFrame(object):
    def main(self):
        #加载配置文件
        c = ConfigManegment.ConfigManegment()

        if(False == os.path.exists(c.getTargetFolderPath())):
            print('Target path not exists')

        fileTuple = []
        for files in os.walk(c.getTargetFolderPath()):
            fileTuple.append(files)

        for textfile in fileTuple[0][2]:
            pass

        #显示界面
        #Application()


        #开始分析
        a = AnalysisOneStock.AnalysisOneFile(c.getTargetFolderPath(), 'SH#601877.txt')
        if True == a.readDataFromFile():
            print("Ture")
        else:
            print("False")



'''
class Application(tk.Frame):
    def sourceAction(self):
        root = tk.tix.Tk()
        dialog = tk.tix.DirSelectDialog(root, command=print_selected)

    def sourceTarget(self):
        print('bbb')

    def sourceResult(self):
        print('ccc')

    master = tk.Tk()
    tk.Label(master, text='分析文件路径').grid(row=0, sticky="nsew")
    tk.Label(master, text='输出文件路径').grid(row=1, sticky="nsew")
    tk.Label(master, text='分析进度').grid(row=2, sticky="nsew")

    eSource = tk.Entry(master)
    eTarget = tk.Entry(master)
    eResult = tk.Entry(master)
    eSource.grid(row=0, column=1)
    eTarget.grid(row=1, column=1)
    eResult.grid(row=2, column=1)

    bSource = tk.Button(master, text='选择')
    bSource.bind('<Button-1>', sourceAction)

    bTarget = tk.Button(master, text='选择')
    bTarget.bind('<Button-1>', sourceTarget)

    bResult = tk.Button(master, text='执行')
    bResult.bind('<Button-1>', sourceResult)


    bSource.grid(row=0, column=3)
    bTarget.grid(row=1, column=3)
    bResult.grid(row=2, column=3)

    master.mainloop()
'''
if __name__ == '__main__':
    MainFrame().main()
