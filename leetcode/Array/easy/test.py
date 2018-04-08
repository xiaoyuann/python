import pymysql

conn=pymysql.connect("localhost","root","888888","contact",charset="utf8")
cur=conn.cursor()
'''cursor.execute("DROP TABLE IF EXISTS CONTACTS")
sql="""create table contacts(
    Cname char(20),
    PhoneNumber char(12) NOT NULL,
    Cage int,
    Csex char(4),
    Caddress char(20) )"""
cursor.execute(sql)'''

sql="""alter table contacts modify Cid int not null auto_increment first"""

try:
    cur.execute(sql)
    conn.commit()
except:
    conn.rollback()
conn.close()