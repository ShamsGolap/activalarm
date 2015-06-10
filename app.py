# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activalarm
# Shams Golap <shams79000@gmail.com>

import time
import datetime
import random

from os import popen
from os import getenv


main_command = 'curl '
send_method = '-X POST '
data = '--data-urlencode '
URL = getenv('URL_SLACK_AK')
channel = '@shams'
username = 'La ligne la plus longue'
text = u'GO GO GO ! Faites la ligne la plus longue avec tout ce que vous avez sur vous !'
payload = '\'payload={"channel": "' + channel + '", "username": "' + username + '", "text": "' + text + '"}\' '


def to_two_digits(number):
    if len(number) == 1:
        return '0' + number
    else:
        return number


def activalarm():
    command = main_command + send_method + data + payload + URL

    time.sleep(random_date(10, 12, 6, 6, 2015, 2015, 10, 18, 0, 59, 0, 59))
    popen(command)


def random_date(min_day, max_day, min_month, max_month, min_year, max_year, min_hour, max_hour, min_min, max_min, min_sec, max_sec):
    dd = str(random.randint(min_day, max_day))

    if dd == 12:
        max_hour = 14

    mm = str(random.randint(min_month, max_month))
    yyyy = str(random.randint(min_year, max_year))
    hh = str(random.randint(min_hour, max_hour))
    MM = str(random.randint(min_min, max_min))
    ss = str(random.randint(min_sec, max_sec))

    dd = to_two_digits(dd)
    mm = to_two_digits(mm)
    hh = to_two_digits(hh)
    MM = to_two_digits(MM)
    ss = to_two_digits(ss)

    alert_format = dd + '/' + mm + '/' + yyyy + ' ' + hh + ':' + MM + ':' + ss

    alert_time = time.mktime(datetime.datetime.strptime(alert_format, '%d/%m/%Y %H:%M:%S').timetuple())
    until_alarm = alert_time - time.time()

    return int(until_alarm)


activalarm()
