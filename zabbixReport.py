import re
import os
import urllib.request, urllib.parse
import http.cookiejar
import datetime
import mysql.connector
# import paramiko
import sshtunnel
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('192.168.10.61', 22, 'root', 'fairlink')
# stdin,stdout,stderr = ssh.exec_command('free -m')
# print(stdout.read())

date = int(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))


def graph(hostip, itemname):
    with sshtunnel.SSHTunnelForwarder(
            ('192.168.10.61', 22),
            ssh_password='fairlink',
            ssh_username='root',
            remote_bind_address=('127.0.0.1', 3306)
    ) as server:
        cnn = mysql.connector.connect(host='127.0.0.1', user='root', password='111111', port=server.local_bind_port, database='zabbix')
        cursor = cnn.cursor()
        cursor.execute("select graphid from graphs_items where graphs_items.itemid=(select itemid from items join hosts on hosts.hostid=items.hostid where hosts.host=\'%s\' and items.name=\'%s\')" % (hostip, itemname))
        results = cursor.fetchone()
        graphid = results[0]
        cursor.execute('select name from hosts where host=\'%s\'' % hostip)
        hostname = cursor.fetchone()[0].decode()        #字节数组转换为str
        # print(graphid, hostname)
        cursor.close()
        cnn.close()

    url = 'http://192.168.10.61/zabbix/index.php'
    value = {'name': 'Admin', 'password': 'fairlink', 'autologin': '1', 'enter': 'Sign in', 'request': ''}
    data = urllib.parse.urlencode(value).encode('utf-8')
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    # opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0')]
    req = opener.open(url, data)
    req = opener.open('http://192.168.10.61/zabbix/chart2.php?graphid=%d&period=86400&width=800&stime=%d' % (graphid, date))
    # print(req.geturl())
    # print(req.read())
    file = open('C:\\Users\\daize\\Desktop\\%s_%d.png' % (hostname, date), 'wb')
    file.write(req.read())
    file.close()

# msg = MIMEMultipart('related')
# msg['Subject'] = 'Zabbix Daily Report'
# msg['From'] = 'daize.song@fairlinkcentury.com'
# msg['To'] = 'daize.song@fairlinkcentury.com'
    msg = MIMEMultipart('related')
    message = '''
    <p>%s_%s</p>
    <p><img src="cid:image1"></p>
    ''' % (hostname, itemname)
    message = MIMEText(message, 'html')
    msg.attach(message)
    file = open('C:\\Users\\daize\\Desktop\\%s_%d.png' % (hostname, date), 'rb')
    # print(file.read())
    msgImage = MIMEImage(file.read())
    file.close()
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)
    return msg
    # print(msg)


msg = graph('192.168.10.55', 'Available memory')
msg['Subject'] = 'Zabbix Daily Report'
msg['From'] = 'daize.song@fairlinkcentury.com'
msg['To'] = 'daize.song@fairlinkcentury.com'

smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
# smtp.connect('smtp.exmail.qq.com')
smtp.login('daize.song@fairlinkcentury.com', 'song123')
smtp.sendmail(msg['From'], msg['To'], msg.as_string())
smtp.quit()

