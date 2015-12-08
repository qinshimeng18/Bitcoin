# -*- coding: utf-8 -*-
#!/usr/bin/env python
# from sqlalchemy.orm import scoped_session, sessionmaker
# from mod.databases.db import engine
import MySQLdb
"""
清理mt数据 cleanData
获取所有edges_表的开始结束时间settime
匹配对应的交易数据 matchdata
"""
def cleanData():
    with open(r'C:\Users\xy2\Desktop\bitcoin\MtGox\backoffice\Exports\btc_xfer_report.csv') as f:
        with open(r'M.csv','a') as t:
            for line in f.readlines():
                l=line.split(',')
                if complexMoney(l[4]):
                    t.write(line)

def complexMoney(s):
    """判断是否是复杂特征数字"""
    sum=0
    if s[0]=='-':
        s=s[1:]
    if '.' in s :
        sum=1
    li=[ 0 for i in range(10)]
    for i in s :
        if i in '0123456789':
            li[int(i)]=1
    for i in li:
        sum+=i
    if s[0] == '0':
        sum=sum-1
    if 'E' in s:
        sum=0
    if sum >= 4:
        return 1
    else:
        return 0


def settime(cur):
    """计算每个edges的时间"""
    for i in range(2,205):
        table ='edges_'+str(i)
        sqlstart ='select * from %s where id =1;' % table
        count =cur.execute(sqlstart)
        resultStart=  cur.fetchone()
        sqlstop = 'select * from %s order by id desc limit 1 ;' % table
        count =cur.execute(sqlstop)
        resultStop= cur.fetchone()
        sql='insert into blktime (id,blk_num,starttime,stoptime) values (%d,\'%s\',%s,%s) ' % (i,table,resultStart[4],resultStop[4])
        cur.execute(sql)
def settest(cur,conn):
    for i in range(2,205):
        table ='edges_'+str(i)
        sqlstart ='select * from %s where id =1;' % table
        count =cur.execute(sqlstart)
        # print 'there has %s rows record' % count
        resultStart=  cur.fetchone()
        sqlstop = 'select * from %s order by id desc limit 1 ;' % table
        count =cur.execute(sqlstop)
        resultStop= cur.fetchone()
        # print resultStop,resultStop[4]
        sql='insert into timeofblk (id,blk_num,starttime,stoptime) values (%d,\'%s\',from_unixtime(%s),from_unixtime(%s)) ' % (i,table,resultStart[4],resultStop[4])
        cur.execute(sql)
def matchdata(cur):
    """匹配对应的交易数据"""
    with open(r'MtCleanData-100.csv') as f:
        with open(r'cleandata.csv','a') as t:
            for line in f.readlines():
                l=line.split(',')
                tables=getTable(cur,l[2])
                if  tables :
                    for table in tables:
                        txs=gettx(cur,table,l[2],l[4])
                        for tx in txs:
                            for i in tx:
                                t.write(str(i)+',')
                            t.write(str(l[0])+str(l[2])+'\n')
def gettx(cur,table,ltime,money):
    """返回匹配tx"""
    money=''.join(money.split('-'))
    sql='select source,target,weight,from_unixtime(time) from %s where ABS(weight -%f)<=0.0001 and ( time between (UNIX_TIMESTAMP(%s)-5400) and (UNIX_TIMESTAMP(%s)+5400)); ' % (table[0],float(money),ltime,ltime)
    result=sqlExe(cur, sql)
    return result
def getTable(cur,time):
    """返回对应的table"""
    result=sqlExe(cur,"select blk_num from blktime where %s between from_unixtime(starttime) and from_unixtime(stoptime);" % time)
    return result

def sqlExe(cur,sql):
    cur.execute(sql)
    return cur.fetchall()
def main():


    try:
        conn=MySQLdb.connect(host='223.3.76.57',db='btc4',user='lgn',passwd='88888888',port=3306)
        cur=conn.cursor()
        cur.execute('SET time_zone = \'-0:00\';')
        # cleanData
        # settime(cur)
        # settest(cur,conn)
        matchdata(cur)

        # result=cur.fetchone()
        # print result
        # print 'ID: %s info %s' % result

        # results=cur.fetchmany(5)
        # for r in results:
        #   print r

        # print '=='*10
        # cur.scroll(0,mode='absolute')

        # results=cur.fetchall()
        # for r in results:
        #     print r


        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
if __name__ == '__main__':
    main()

