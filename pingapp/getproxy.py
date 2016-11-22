#! /usr/bin/python
#coding=utf-8
 
import datetime
from datetime import timedelta
from datetime import tzinfo
import os
import re
import socket
import sys
import time
import urllib2
from  pingpage import pingpagecomm
import pwd
import grp

class getproxy:
    __type = 0 #代表实时抓数据
    __check = 0 #代表检查代理端口是否能够使用
    path = ""
    proxytype = 0 
      
    __app_col = ('anzhi', '360','qq','baidu','huawei','pp','coolmart','oppo')
    
    def getlocaldate(self):
        
        from_tzinfo =   pingpagecomm.GMT()#格林威治时区，0时区
        local_tzinfo =  pingpagecomm.GMT8()#本地时区，+8区
        
        gmt_time = datetime.datetime.utcnow()
        gmt_time = gmt_time.replace(tzinfo=from_tzinfo)
        local_time = gmt_time.astimezone(local_tzinfo)
        return local_time.strftime("%Y-%m-%d")  
 
    def hex2dec(self, string_num):
        return str(int(string_num.upper(), 16))
    
    #type=1 代表实时抓取 check=1 代表检查端口 protype=1 代表proxy类型
    def __init__(self, type=0, check=0,path="",proxytype=0):
        self.__type = type
        self.__check = check 
        self.path = path
        self.proxytype = proxytype 
        
    
    def __get_ip_byappfile(self, filename):
        tmpd = {}
        
        if os.path.exists(filename) == False:
            return tmpd
     
        fread = open(filename, "r")
        for line in fread:
            line = line.strip()
            if line == "":
                continue
            arr = line.split("_")
            if arr:
                tmpd[arr[0]] = 1 
        fread.close()
        return tmpd
    
        
    def save_ip(self, ipdict_col):
        #path = "ipcol"
        if not  os.path.isdir(self.path):
            os.mkdir(self.path, 0777)
        
        appip_arr = {}
        
        #循环打开文件句柄,每个应用市场一个文件        
        f = {}
        for apksrc in self.__app_col:   
            #filename = path + "/" + apksrc + "_" + self.getlocaldate() + ".log"
            filename = self.path + "/" + apksrc + "_" + pingpagecomm.getlocaldate() + ".log"
            
            print filename  
 
            appip_arr[apksrc] = self.__get_ip_byappfile(filename) #保存已经存在的ip 
            f[apksrc] = open(filename, "a")
         
        #循环将新获取的可用IP保存到文件中(每个应用市场一个文件)
        for apksrc in self.__app_col: #每个应用市场
            for iplist in ipdict_col:
                for ip in iplist:
            
                    #if appip_arr[apksrc][ip['ip']]=="":
                    if appip_arr[apksrc].get(ip['ip']) ==  None :
                        f[apksrc].write( ip['from'] + "_" + ip['ip'] + "_" + ip['port'] + "_0_0_" +  str(int(time.mktime(time.gmtime())))  + "\n") 
                    #ip_port_downloadcount_succcount_errorcount_更新时间
            f[apksrc].close() 
        
    
    #检查代理是否能够连接
    def check_porxy_connect(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((ip, int(port)))
            s.close()
            print 'ok'
            return True
        except:
            print 'error'
            return False
        finally:
            s.close()


    def get_proxy_bygatherproxy(self):
        #http://gatherproxy.com/proxylist/country/?c=China
        if self.__type == 1:
            url = "http://gatherproxy.com/proxylist/country/?c=China"
            response = urllib2.urlopen(url)
            content = response.read()
            f = open(self.path + '/get_proxy_bygatherproxy.log', "w")
            f.write(content)
            f.close()
      
        else:
            file = self.path + "/get_proxy_bygatherproxy.log"
            f = open(file, "r")
            content = f.read()
            f.close()
        
        html = content.replace('null', '""')

        ipdict = []
        reg = 'gp.insertPrx\((.*?)\);'
        imgre = re.compile(reg, re.S) 
        items = re.findall(imgre, html) #返回列表
        f = open(self.path + '/proxyinfo.log', "a")
        for item in items:
            item = item.lower()
            item = eval(item)

            ip = item['proxy_ip']
            port = self.hex2dec(item['proxy_port'])
            speed = item['proxy_time']
            proxycountry = item['proxy_country']
            type = item['proxy_type'] #Elite
            updatetime = item['proxy_last_update']
            uptime = ""
            print type 
            
            f.write("gatherproxy" + "_" + ip + "_" + port + "_" +  type  + "\n") 
            
            if self.proxytype==1 and type!="Elite":
                continue 
            
            dictproxy = {"from":"gatherproxy" ,"ip":ip, "port":port, "speed":speed, "updatetime":updatetime, "proxycountry":proxycountry, "uptime":uptime, "type":type}
            
            if  self.__check == 1 and  self.check_porxy_connect(ip, port):
                ipdict.append(dictproxy)
            elif self.__check == 0:
                ipdict.append(dictproxy)
        f.close()
        
        return ipdict 
    
    
    def get_local_file(self):
        url = "http://www.newyingyong.cn/getproxy.php"
        response = urllib2.urlopen(url)
        html = response.read()
        items = html.split('\n')
         
        ipdict = []
        if len(items)<1 :
            return ipdict
        
        for item in items:
            tmpdata = item.split("_")
            #print tmpdata 
            if len(tmpdata)>2  and tmpdata[3] == "Elite"  and self.check_porxy_connect(tmpdata[1], tmpdata[2]) :
                dictproxy = {"from":tmpdata[0],"ip":tmpdata[1], "port":tmpdata[2], "speed":"", "updatetime":"", "proxycountry":"", "uptime":"", "type":tmpdata[3]}
                ipdict.append(dictproxy)
        
        return ipdict

    def get_proxy_byproxynova(self):
        if self.__type == 1:
            #url = "http://www.proxynova.com/proxy-server-list/country-am/"
            url = "http://www.proxynova.com/proxy-server-list/country-cn/"

            response = urllib2.urlopen(url)
            html = response.read()

            reg = '<table.*id="tbl_proxy_list">.*<tbody>(.*)</tbody>.*</table>'
            imgre = re.compile(reg, re.S) 
            items = re.findall(imgre, html)
            if items:
                content = items[0]
            f = open(self.path + '/get_proxy_byproxynova.log', "w")
            f.write(content)
            f.close()
        else:
            f = open(self.path + '/get_proxy_byproxynova.log', "r")
            content = f.read()
            f.close()

        '''
        reg = '<tr>.*?<span class="row_proxy_ip">(.*?)</span></td>.*?<td align="left">.*?">(.*?)</a>.*?</td>.*?<td align="left">'
        reg = reg + '.*?datetime="(.*?)">.*?</time>.*?</td>.*?<td align="left">.*?data-value="(.*?)".*?</td>.*?<td style="text-align:center !important;">'
        reg = reg + '.*?">(.*?)</span>.*?</td>.*?<td align="left">.*?<a.*?>(.*?)</a>.*?</td>.*?<td align="left">.*?">(.*?)</span>.*?</tr>'
        '''

        reg = '<tr>.*?<span class="row_proxy_ip">(.*?)</span></td>.*?<td align="left">(.*?)</td>.*?<td align="left">'
        reg = reg + '.*?datetime="(.*?)">.*?</time>.*?</td>.*?<td align="left">.*?data-value="(.*?)".*?</td>.*?<td style="text-align:center !important;">'
        reg = reg + '.*?">(.*?)</span>.*?</td>.*?<td align="left">.*?<a.*?>(.*?)</a>.*?</td>.*?<td align="left">.*?">(.*?)</span>.*?</tr>'

        ipdict = []
        imgre = re.compile(reg, re.S)
        items = re.findall(imgre, content)
        file =  '/usr/share/nginx/proxyinfo.log'
        #file = self.path + '/proxyinfo.log'
        f = open( file, "a")
         
        for item in items:

            ip = item[0] #ip 
            port = item[1]  #端口 
            updatetime = item[2] # 更新时间
            speed = item[3] #速度   
            uptime = item[4]
            proxycountry = item[5] #国家
            type = item[6] #代理类型
            
            print type 
            port = re.sub('.*<a[^>]+>(.*)</a>.*', r'\1', port.strip()) 
            if  updatetime != "":
                updatetime = updatetime.replace('Z', '')
                timeArray = time.strptime(updatetime, "%Y-%m-%d %H:%M:%S")
                updatetime = int(time.mktime(timeArray))

            s_proxycountry = proxycountry.split('\t')
            if s_proxycountry:
                proxycountry = s_proxycountry[0]
            f.write("gatherproxy" + "_" + ip + "_" + port + "_" + type  + "\n") 
            
            if self.proxytype==1 and type!="Elite":
                continue 
            dictproxy = {"from":"proxynova" ,"ip":ip, "port":port, "speed":speed, "updatetime":updatetime, "proxycountry":proxycountry, "uptime":uptime, "type":type}
            if  self.__check == 1 and  self.check_porxy_connect(ip, port):
                ipdict.append(dictproxy)
            elif self.__check == 0:
                ipdict.append(dictproxy)
                
        uid = pwd.getpwnam("ftpuser2").pw_uid
        gid = grp.getgrnam("www-data").gr_gid
        os.chown(file, uid, gid)
        #os.chown(file,"www-data","www-data")
        
        #os.chmod(file,"077")
        f.close()
        ipdict = tuple(ipdict)    
        return ipdict 
        # end function 
    
    #end class
   
 
path = "/root/pingapp/ipcol"
#path = "ipcol"

#obj = getproxy(1,1,path,1)
#ipdict = obj.get_local_file()
#print ipdict

#obj = getproxy(1,1,path,1)
#obj.get_local_file()
#sys.exit('parmam error2')

args = sys.argv[1:] 
if len(args)<1 :
   sys.exit('parmam error')
type = args[0] 

if type == "getproxy" :

    ipdict_col = []
    obj = getproxy(1,1,path,1)   # 1代表实施抓 1代表ping  
    #ipdict = obj.get_proxy_bygatherproxy()
    #ipdict_col.append(ipdict) 
    ipdict = obj.get_proxy_byproxynova()
    ipdict_col.append(ipdict) 
    #obj.save_ip(ipdict_col)
else :
    ipdict_col = []
    obj = getproxy(1,1,path,1)
    ipdict = obj.get_local_file()
    ipdict_col.append(ipdict) 
    obj.save_ip(ipdict_col)
    
 
 
 

 
 
 
 
 
 
 
  
 
