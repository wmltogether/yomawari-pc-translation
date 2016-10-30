# -*- coding:utf-8 -*-

import codecs,struct,sys,fnmatch,os
def dir_fn(adr):
    dirlst=[]
    for root,dirs,files in os.walk(adr):
        for name in files:
            adrlist=os.path.join(root, name)
            dirlst.append(adrlist)
    return dirlst
def makestr(lines):
    string_list = []
    head_list = []
    num = len(lines)
    for index,line in enumerate(lines):
        if u'####' in line:
            head_list.append(line[5:-7])
            i = 1
            string = ''
            while True:
                if index+i >= num:
                    break
                if '####' in lines[index+i]:
                    break
                string += lines[index+i]
                i += 1
            string_list.append(string[:-4])
    return string_list, head_list
def make_str_dic(string_list,head_list):
    dic = {}
    for i in xrange(len(string_list)):
        dic[head_list[i]]=string_list[i]
    return dic
def make_head_dic(string_list,head_list):
    dic_h = {}
    for i in xrange(len(string_list)):
        dic_h[string_list[i]]=head_list[i]
    return dic_h
def convert_ios2psp(fn):
    print(fn)
    #log.write(fname+'\r\n')
    fn_p = fn
    fna= "log.txt"
    if os.path.exists("iose\\logadd.txt"):
        fnglob = "logadd.txt"
    else:
        fnglob = "log.txt"
    psplines = codecs.open('pspe\\%s'%fn_p,'rb','utf-16').readlines()
    ioslines = codecs.open('iose\\%s'%fna,'rb','utf-16').readlines()
    ioslines_c = codecs.open('iosc\\%s'%fna,'rb','utf-16').readlines()
    globlines = codecs.open('iose\\%s'%fnglob,'rb','utf-16').readlines()
    globlines_c = codecs.open('iosc\\%s'%fnglob,'rb','utf-16').readlines()
    psp_string_list, psp_head_list = makestr(psplines)
    ios_string_list, ios_head_list = makestr(ioslines)
    ios_string_list_c, ios_head_list_c = makestr(ioslines_c)
    engdic = make_head_dic(ios_string_list,ios_head_list)
    chsdic = make_str_dic(ios_string_list_c,ios_head_list_c)
    glob_string_list, glob_head_list = makestr(globlines)
    glob_string_list_c, glob_head_list_c = makestr(globlines_c)
    globengdic = make_head_dic(glob_string_list,glob_head_list)
    globchsdic = make_str_dic(glob_string_list_c,glob_head_list_c)
    dest = codecs.open('pspc\\%s'%fn_p,'wb','utf-16')
    p=0
    for j in xrange(len(psp_string_list)):
        string = psp_string_list[j]
        head = psp_head_list[j]
        #print(head)
        if string in engdic:
            if string in engdic:
                p=1
                ioshead = engdic[string]
                try:
                    c_string = chsdic[ioshead]
                except:
                    c_string = string
                dest.write('#### %s ####\r\n%s\r\n\r\n'%(head,c_string))
            else:
                #print('#### %s ####\r\n%s\r\n\r\n'%(head,string))
                
                log.write('#### %s,%s ####\r\n%s\r\n\r\n'%(fname,head,string))
                dest.write('#### %s ####\r\n%s\r\n\r\n'%(head,string))
                #if head=='214':print('%s,%s'%(c_string,string))
        elif string.replace('{0A}\r\n' , '') in engdic:
            string =string.replace('{0A}\r\n' , '')
            ioshead = engdic[string]
            try:
                c_string = chsdic[ioshead]
            except:
                c_string = string
            dest.write('#### %s ####\r\n%s\r\n\r\n'%(head,c_string))
        elif string in globengdic:
            globhead = globengdic[string]
            try:
                c_string = globchsdic[globhead]
            except:
                c_string = string
            dest.write('#### %s ####\r\n%s\r\n\r\n'%(head,c_string))
        elif string.replace('\r\n' , '') in engdic:
            string =string.replace('\r\n' , '')
            ioshead = engdic[string]
            try:
                c_string = chsdic[ioshead]
            except:
                c_string = string
            dest.write('#### %s ####\r\n%s\r\n\r\n'%(head,c_string))         
        else:
            #print('#### %s ####\r\n%s\r\n\r\n'%(head,string))
            log.write('#### %s,%s ####\r\n%s\r\n\r\n'%(fname,head,string))
            dest.write('#### %s ####\r\n%s\r\n\r\n'%(head,string))
            #if head=='214':print('%s,%s'%(c_string,string))
    dest.close()
    if os.path.getsize('pspc\\%s'%fn_p) <= 4:
        os.remove('pspc\\%s'%fn_p)
    
fn=dir_fn('pspe')
log = codecs.open('log.txt','wb','utf-16')
for j in xrange(len(fn)):
    if not fnmatch.fnmatch(fn[j],'*.txt'):
        continue
    fname = fn[j][5:]
    convert_ios2psp(fname)
log.close()




