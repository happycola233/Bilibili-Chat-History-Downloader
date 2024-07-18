import requests
import time
import pickle
import winreg
import json
import time

true = True
false = False
null = None

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]
桌面路径 = get_desktop()

选择=input("1、爬聊天记录  2、提取聊天中图片链接 [1/2] ")
if 选择=="1":
    headers={'Cookie': 'SESSDATA='+input("请输入SESSDATA：")+'; bili_jct='+input("请输入bili_jct："), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    uid=input("输入UID：")
    print()

    start = time.perf_counter()

    聊天列表数据 = []
    end_seqno = eval(requests.get("https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs?sender_device_id=1&talker_id="+uid+"&session_type=1&size=1&build=0&mobi_app=web",headers=headers).text)["data"]["max_seqno"]
    while True:
        result=eval(requests.get("https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs?sender_device_id=1&talker_id="+uid+"&session_type=1&size=200&end_seqno=" + str(end_seqno+1) + "&build=0&mobi_app=web",headers=headers).text)
        if result["code"]==0:
            if result["data"]["min_seqno"]==1:
                if result["data"]["messages"] != None:
                    result["data"]["messages"].reverse()
                    聊天列表数据 = result["data"]["messages"]+聊天列表数据
                print("消息序号开始值："+str(result["data"]["min_seqno"])+"，消息序号结束值："+str(result["data"]["max_seqno"])+"，总消息数："+str(len(聊天列表数据)))
                end_seqno=result["data"]["min_seqno"]-1
                break
            if result["data"]["messages"] != None:
                result["data"]["messages"].reverse()
                聊天列表数据 = result["data"]["messages"]+聊天列表数据
            print("消息序号开始值："+str(result["data"]["min_seqno"])+"，消息序号结束值："+str(result["data"]["max_seqno"])+"，总消息数："+str(len(聊天列表数据)))
            end_seqno=result["data"]["min_seqno"]-1
        time.sleep(0)


    with open (桌面路径 + "\\UID" + uid + "变量全信息（共"+str(len(聊天列表数据)) + "条）.txt","wb") as f:
        pickle.dump(聊天列表数据,f)
        f.close()
        
    with open (桌面路径 + "\\UID" + uid + "美化（共"+str(len(聊天列表数据)) + "条）.txt","wb") as f:
        f.write ((json.dumps(聊天列表数据, ensure_ascii=False, indent=2)).encode())
        f.close()

    print()
    print("已保存：" + 桌面路径 + "\\UID" + uid + "变量全信息（共"+str(len(聊天列表数据)) + "条）.txt")
    print("已保存：" + 桌面路径 + "\\UID" + uid + "美化（共"+str(len(聊天列表数据)) + "条）.txt")
    print()
    print("--------------------任务已完成--------------------")
    end = time.perf_counter()
    runTime = round(end - start,3)
    print("总共用时：", runTime)

else:
    import ctypes
    from tkinter import *
    from tkinter import filedialog

    # 设置DPI感知以适应高DPI缩放
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except AttributeError:
        pass

    root = Tk()
    root.withdraw()  # 隐藏根窗口

    # 获取当前DPI
    current_dpi = root.winfo_screenmmwidth() / root.winfo_screenwidth() * 25.4

    # 计算高DPI缩放因子
    scaling_factor = 1.0
    if current_dpi > 96:
        scaling_factor = current_dpi / 96.0

    # 设置窗口字体大小和缩放因子
    root.option_add("*Font", "TkDefaultFont %d" % int(10 * scaling_factor))
    root.option_add("*Dialog.msg.font", "TkDefaultFont %d" % int(10 * scaling_factor))

    # 调用资源管理器打开文件选择对话框
    聊天信息文件 = filedialog.askopenfilename(filetypes=(("变量全信息文件", "*.txt"), ("All files", "*.*")),title='选择变量全信息文件')
    start = time.perf_counter()
    file=open(聊天信息文件,"rb")
    聊天信息=pickle.load(file)
    file.close()
    open(桌面路径 + "\\消息图片链接提取.txt", 'w', encoding='utf-8').close()#清除文件内容
    for i in range(1,len(聊天信息)):
        if 聊天信息[i]["msg_type"] == 2:
            f=open(桌面路径 + "\\消息图片链接提取.txt", 'a+', encoding='utf-8')#附加（可写不可读）
            f.write((eval(聊天信息[i]["content"])["url"]).replace("\\/","/") + "\n")
    f.close()
    print("提取的链接已保存到"+ 桌面路径 + "\\消息图片链接提取.txt")
    print()
    print("--------------------任务已完成--------------------")

    end = time.perf_counter()
    runTime = round(end - start,3)
    print("总共用时：", runTime, "秒")