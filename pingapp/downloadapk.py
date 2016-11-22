#! /usr/bin/python
#coding=utf-8
 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.alert import  Alert 
from selenium.webdriver.common.keys import Keys
import time
import sys
import datetime
from datetime import timedelta
from datetime import tzinfo
import os
import re
import socket
import urllib2
from  pingpage import pingpagecomm
import copy
import random  

class dispatch_pingapp:
    os = 1  #1代表windows 2代表linux
    debug = 0 #1代表调试模式
    useproxy = 0 # 1代表使用代理
    
    appid = "" #appid 
    apptitle = ""
    appmarket = "" #应用市场
    
    ipcolpath = "ipcol" #ip 文件
    dealapppath = "dealapp" #任务标志文件
    logpath = "log" #log日志文件
    
    deal_processnum = 0 #本次任务需要下载的次数
    deal_ipcol = [] #所有可用IP的集合
    deal_downloadipcol = ()
    deal_pingip = {}
    
    def __init__(self,appid,appmarket,apptitle,os=1,debug=0,pathdir="",useproxy=0):
        self.appid = appid
        self.appmarket = appmarket
        self.os = os 
        self.debug = debug 
        self.pathdir = pathdir 
        self.useproxy = useproxy
        self.apptitle = apptitle
         
        self.ipcolpath =  self.pathdir +  self.ipcolpath  
        self.dealapppath = self.pathdir+ self.dealapppath 
        self.logpath = self.pathdir  + self.logpath  
        
    
    def log(self,str):
        str = self.appmarket + "_" + pingpagecomm.getlocaldate(1) + "_" +  str + "\n"
         
        if not  os.path.isdir(self.logpath):
           os.mkdir(self.logpath, 0777)
        filename = self.logpath + "/" + self.appmarket + "_" +  self.appid + "_" + pingpagecomm.getlocaldate() + ".log"
        
        f = open(filename, "a")
        f.write(str)
        f.close()
        #f = fopen()
        
    def get_ratio(self,x,y) :
        if y == 0 or x == 0 :
            return 0 
        return int(float(x)/float(y)*1000)
    
    def get_downloadip(self):
        
        newdata = []
        nodata = []
        radiodata = []
        otherdata = []
        tmpb = 0 
        tmpc = 0 
        tmpd = 0  
        
        #获取最新获取到的IP
        '''
        i = eval("-" + str(self.deal_processnum))
        newdata = self.deal_ipcol[i:]
        del self.deal_ipcol[i:]  #删除部分数据
        '''
        self.deal_ipcol.reverse()
        for k  in self.deal_ipcol:
            if  (k[2] == 0) and (tmpb <   self.deal_processnum) : 
                tmpb = tmpb + 1
                newdata.append(k)
                self.deal_ipcol.remove(k)
      
        random.shuffle(self.deal_ipcol)
 
        #获取未下载过的IP
        for k  in self.deal_ipcol:
            if  (k[2] == 0) and (tmpc <   self.deal_processnum) : 
                tmpc = tmpc + 1
 
                nodata.append(k)
                self.deal_ipcol.remove(k)
        
        #获取下载成功率高的IP
        for k  in self.deal_ipcol:
            if  (k[4] >100 ) and (tmpd <  self.deal_processnum) : 
                tmpd = tmpd + 1
                radiodata.append(k)
                self.deal_ipcol.remove(k)
        
        tmpi = self.deal_processnum * 3 - len(newdata) - len(nodata) - len(radiodata)
        
        if (tmpi>0) and (len(self.deal_ipcol)  <  tmpi) :
            tmpi = len(self.deal_ipcol) 
        
        if (tmpi>0) :
            otherdata = self.deal_ipcol[0:tmpi]
        
        self.deal_downloadipcol = newdata +  nodata + radiodata 
        #+ otherdata 

    
     #更新IP库
    def update_ipcol(self):
        if self.useproxy == 0 :
            return 
        
        proxyipfile =  self.ipcolpath + "/" + self.appmarket + "_" + pingpagecomm.getlocaldate() + ".log"
        if os.path.exists(proxyipfile) == False:
            raise Exception('%s,%s : proxyipfile:%s no exists' %  (self.appid , self.appmarket , proxyipfile) )
  
        tmplist = []
        f = open(proxyipfile, "r")
        
        for line in f:
            line = line.strip()
            if line == "":
                continue
            arr = line.split("_")
            tmp_ip = arr[1]
             
            if self.deal_pingip.has_key(tmp_ip) :
                v = self.deal_pingip[tmp_ip]
                download_count = str(int(arr[3])+1)
                if v == 1 :
                    tmplist.append(arr[0] + "_" + arr[1] + "_" + arr[2] + "_" + download_count + "_" + str(int(arr[4])+1) + "_" + arr[5])
                else:
                    tmplist.append(arr[0] + "_" + arr[1] + "_" + arr[2] + "_" + download_count + "_" + arr[4] + "_" + arr[5])
            else :
                tmplist.append(line)
        f.close()
        
        f= open(proxyipfile, "w+")
        for s in tmplist:
            f.write(s + "\n")
        f.close()
     
    #获取所有的IP    
    def get_proxyip(self):
     
        proxyipfile =  self.ipcolpath + "/" + self.appmarket + "_" + pingpagecomm.getlocaldate() + ".log"
        print proxyipfile
       
        if os.path.exists(proxyipfile) == False:
            raise Exception('%s,%s : proxyipfile:%s no exists' %  (self.appid , self.appmarket , proxyipfile) )
         
        f = open(proxyipfile, "r")
        for line in f:
            line = line.strip()
            if line == "":
                continue
        
            arr = line.split("_")
            tmp_ip = arr[1]
            tmp_port = arr[2]
            tmp_downloadcount = int(arr[3]) 
            tmp_succcount = int(arr[4])
            tmp_succratio = self.get_ratio(tmp_succcount,tmp_downloadcount)
            tmp_time = arr[5]
            
            #self.deal_ipcol.append((tmp_ip,tmp_port,tmp_downloadstatus,tmp_downloadcount,tmp_succcount,tmp_succratio,tmp_time))
            self.deal_ipcol.append((tmp_ip,tmp_port,tmp_downloadcount,tmp_succcount,tmp_succratio,tmp_time))
            
        if len(self.deal_ipcol) <=0 :
            raise Exception('%s,%s : get_proxyip:%s no data' %  (self.appid , self.appmarket , proxyipfile) )
     
    #获取需要处理的log
    def deal_data_log(self):
        filename = self.dealapppath + "/" + self.appmarket + "_" + self.appid + ".log"
     
        if os.path.exists(filename) == False:
            raise Exception('%s,%s : deal_data_log:%s no exists' %  (self.appid , self.appmarket , filename) )
        
        f = open(filename, "r")
        tmpfiledata = []
        dealstatus = 0 
        
        for line in f:
            line = line.strip()
            if line == "":
                continue
 
            arr = line.split("_")
            tmp_datetime = arr[0]
            tmp_status= arr[2]
            tmp_num = arr[1]  #需要下载的次数
          
            if dealstatus== 0 and tmp_status == "init" and pingpagecomm.check_time(tmp_datetime )>0:
                dealstatus = 1 
                self.deal_processnum =  int(tmp_num)
                
                if self.debug == 1 :
                    tmpstr = line
                else :
                    tmpstr = tmp_datetime + "_" + tmp_num + "_start"
                    
                tmpfiledata.append(tmpstr)
            else:
                tmpfiledata.append(line)
        f.close()
        
        f= open(filename, "w+")
        for s in tmpfiledata:
            f.write(s + "\n")
        f.close()
       
        if self.deal_processnum<=0 :
            raise Exception('%s,%s : no deal log :%s no exists' %  (self.appid , self.appmarket , filename) )
      
    def initdownload(self):
        obj = downloadapk(self.os,self.debug) 
        i=1
     
        for s in self.deal_downloadipcol : 
            
            if i > self.deal_processnum :
                continue 
                
            proxy = (s[0],s[1])
            if self.useproxy == 0:
                proxy = ()
        
            try :
                self.log( 'deal_initdownload_start_' + str(i) )
                 
                obj.set_param( appmarket,self.appid,self.apptitle,proxy)
                obj.start()
                 
                self.log( 'deal_initdownload_succ_' + str(i) )
                
                if self.useproxy == 1:
                    self.deal_pingip[s[0]] = 1 
                i+=1
            except Exception as e:
                if self.useproxy == 1:
                    self.deal_pingip[s[0]] = 0
                print e 
                self.log('deal_initdownload_fail_' + str(e)+ "_" + str(i))
 
        if self.useproxy:
            print self.deal_pingip
            
class downloadapk() :
    
    __type = 1 #1代表windows 2代表linux
    __debug = 0 # 1代表debug模式
    display = None
    drive = None 
    market = "" #应用市场
    appid = ""
    apptitle = ""
    url = "" #app 对应的URL
    proxy = ()

    def __init__(self, type=0,debug=0 ):
        self.__type = type
        self.__debug = debug 
 
    def set_param(self,market="",appid="",apptitle="",proxy=()):
        self.market = market
        self.appid = appid
        self.proxy = proxy
        
    def start_display(self):
        if self.__type == 2: 
            from pyvirtualdisplay import Display 
            self.display = Display(visible=0, size=(1024, 768))
            self.display.start()
    
    def start_chrome(self):
        
        mobile_emulation = {
        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
       
        try :
            if self.proxy:
                chrome_options = webdriver.ChromeOptions()
                #chrome_options.add_argument("mobileEmulation", mobile_emulation)
                chrome_options.add_argument('--proxy-server=%s,%s'% self.proxy)
                self.driver = webdriver.Chrome(chrome_options=chrome_options)

            else:
                self.driver = webdriver.Chrome()
        except Exception as e:
            if self.__debug== 1 :
                print 'function:init chrome error'
            raise e
    
    def get_page(self):
        
        if self.market == "qq" :
            url = "http://android.myapp.com/myapp/detail.htm?apkName=%s" % (self.appid) 
            pattern = re.compile(ur'应用宝')   
        elif self.market == "360" :
            url = "http://zhushou.360.cn/detail/index/soft_id/%s"  % (self.appid) 
            pattern = re.compile(r'360') 
        elif self.market == "anzhi" :
            url = "http://www.anzhi.com/soft_%s.html" % (self.appid) 
            pattern = re.compile(ur'安卓安智市场') 
        elif self.market == "baidu":
            url = "http://shouji.baidu.com/software/item?docid=%s&f=sug@software" % (self.appid) 
            pattern = re.compile(ur'百度手机') 
        elif self.market == "pp":
            url = "http://android.25pp.com/detail_%s.html" % (self.appid)
            pattern = re.compile(ur'PP助手') 
        elif self.market == "huawei":
            url = "http://appstore.huawei.com/app/C%s" % (self.appid)
            pattern = re.compile(ur'华为应用市场')   
        elif self.market == "coolmart":
            url = "http://www.coolmart.net.cn/#id=detail&appid=%s" % (self.appid)
            pattern = re.compile(ur'酷派应用商店')  
        elif self.market == "wandoujia":
            url = "http://www.wandoujia.com/apps/%s"  % (self.appid)
            pattern = re.compile(ur'豌豆荚')  
            
          
        if self.__debug== 1 :
            print "function:" , url ,self.proxy
            
        #agent = self.driver.execute_script("return navigator.userAgent")
        #print agent 
        
        #self.driver.set_page_load_timeout(30)
        try :
            self.driver.get(url)
            time.sleep(5) #让页面的元素全部加载完成.
            pagetitle = self.driver.title  
            pageurl = self.driver.current_url
        except Exception as e:
            if self.__debug== 1 :
                print 'function:get url error'
            self.close_rs()
            raise e
        
        matchv = pattern.search(pagetitle) 
        if matchv :
            if self.__debug== 1 :
                print "function:getpage succ"
        else :
            if self.__debug== 1 :
                print "function:getpage fail" 
            self.close_rs()
            raise "getpage fail"
    
    def download(self):
        try :
            if self.market == "qq" :
                download_link = self.driver.find_element_by_class_name('det-down-btn')
                actions = ActionChains(self.driver)
                actions.click(download_link)
                actions.perform()
                time.sleep(20)
            elif self.market == "360":
                key = "立即安装"
                download_link = self.driver.find_element_by_link_text(key)
                actions = ActionChains(self.driver)
                actions.click(download_link)
                actions.perform()
                time.sleep(20)
            elif self.market == "anzhi":
                key = "下载到电脑"
                #reload(sys)   
                #sys.setdefaultencoding('gbk') 
                #key = key.encode('utf8') 
                download_link = self.driver.find_element_by_link_text(key)
                actions = ActionChains(self.driver)
                actions.click(download_link)
                actions.perform()
                time.sleep(20)
            elif self.market == "baidu":
                download_link = self.driver.find_element_by_class_name('apk')
                actions = ActionChains(self.driver)
                actions.click(download_link)
                actions.perform()
                time.sleep(20)
            elif self.market == "pp":
                key = "下载到电脑"
                download_link = self.driver.find_element_by_link_text(key)
                actions = ActionChains(self.driver)
                actions.click(download_link)
                actions.perform()
                time.sleep(20)
            elif self.market == "huawei": #有问题
                key = "下载到电脑"
                #download_link = self.driver.find_element_by_link_text(key)
                download_link = self.driver.find_element_by_class_name('mkapp-btn mab-download')
                actions = ActionChains(self.driver)
                actions.click(download_link)
                actions.perform()
                time.sleep(20)
            elif self.market == "coolmart":   
                key = "高速下载"
                download_link = self.driver.find_element_by_link_text(key)
                actions = ActionChains(self.driver)
                actions.click(download_link)
                actions.perform()
                time.sleep(20)
            elif self.market == "wandoujia":
                key = "下载"
                download_link = self.driver.find_element_by_link_text(key)
                actions = ActionChains(self.driver)
                actions.click(download_link)
                actions.perform()
                time.sleep(20)
             
             
            self.close_rs()
            if self.__debug== 1 :
                print "function:download succ" 
        except Exception as e:
            self.close_rs()
            if self.__debug== 1 :
                print "function:download fail" 
            raise e
        
 
    def close_rs(self):
        self.driver.close()
        self.driver.quit()
        if self.__type == 2: 
            self.display.stop()
    
    #控制运行程序
    def start(self):
        self.start_display()
        self.start_chrome()
        self.get_page()
        self.download()
        
 
##############################
apptitle = ''
proxy = ()
#proxy = ('183.217.194.207','8123')

 
args = sys.argv[1:] 
if len(args)<2 :
   sys.exit('parmam error')
appmarket = args[0] 
appid = args[1]

#调试
#obj = downloadapk(type=2,debug=1) 
#obj.set_param(appmarket,appid,'',proxy)
#obj.start()
#sys.exit('exit')
    
#disp = dispatch_pingapp(appid,appmarket,'',debug=1,os=1,pathdir="C:\\pingapp\\",useproxy=0)
disp = dispatch_pingapp(appid,appmarket,'',debug=1,os=2,pathdir="/root/pingapp/",useproxy=1)

try:
    disp.log('start')
    disp.deal_data_log() #获取准备处理的数据
    
    disp.get_proxyip() #获取所有可操作的IP
    disp.get_downloadip() #获取本次任务准备使用的IP
    
    disp.initdownload() #开始下载了
    disp.update_ipcol()
    disp.log('end')

except Exception as e:
    print  e
    disp.log(str(e))
    disp.log('end')

 
 
 
