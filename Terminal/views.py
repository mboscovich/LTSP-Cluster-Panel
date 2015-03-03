from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.
def code1(request):
    html = "error"
    #Code 1: Register a new client, and save the hw inventory.
    # code 1 ?ip=192.168.2.221/mac=00:90:F5:2A:ED:A7/bootservip=192.168.2.253/code=1
    #      XTERM is booting and has its bootservip
    if 'code=1' in request.GET['ip']:
        datos = re.match(r'(?P<ip>.*)/mac=(?P<mac>.*?)/'
        'bootservip=(?P<bootservip>.*)/code=(?P<code>.*)', request.GET['ip'])
        if datos:
            ip = datos.group('ip')
            mac = datos.group('mac')
            bootservip = datos.group('bootservip')
            code = datos.group('code')
            html = "<html><body>CODE1<br>IP: %s<br>MAC: %s<br>BootServerIP: "\
                "%s<br>Code: %s<br>GET: %s<br>POST: %s</body></html>" % (
                    ip, mac, bootservip, code, request.GET, request.POST)
    # code 2 ?ip=192.168.2.221/appservip=192.168.2.254/display=0.0/code=2
    #     XTERM has it appserver & display
    elif 'code=2' in request.GET['ip']:
        datos = re.match(r'(?P<ip>.*)/appservip=(?P<appservip>.*?)/'
        'display=(?P<display>.*)/code=(?P<code>.*)', request.GET['ip'])
        if datos:
            ip = datos.group('ip')
            appservip = datos.group('appservip')
            display = datos.group('display')
            code = datos.group('code')
            html = "<html><body>CODE2<br>IP: %s<br>APPSERVIP: %s<br>DISPLAY: "\
                "%s<br>Code: %s</body></html>" % (ip, appservip, display, code)
    # code 3 * ?ip=192.168.2.221/appservip=192.168.2.253/display=0.0/code=3/username=3
    #      a user is connected
    elif 'code=3' in request.GET['ip']:
        datos = re.match(r'(?P<ip>.*)/appservip=(?P<appservip>.*?)/'
        'display=(?P<display>.*)/code=(?P<code>.*)/username=(?P<username>.*)',
            request.GET['ip'])
        if datos:
            ip = datos.group('ip')
            appservip = datos.group('appservip')
            display = datos.group('display')
            username = datos.group('username')
            code = datos.group('code')
            html = "<html><body>CODE3<br>IP: %s<br>APPSERVIP: %s<br>DISPLAY: "\
            "%s<br>Code: %s<br>Username: %s</body></html>" % (ip, appservip,
            display, code, username)
    # code 4 * ?ip=192.168.2.221/appservip=192.168.2.253/display=0.0/code=4/username=3
    #      a user is de connected
    elif 'code=4' in request.GET['ip']:
        datos = re.match(r'(?P<ip>.*)/appservip=(?P<appservip>.*?)/'
        'display=(?P<display>.*)/code=(?P<code>.*)/username=(?P<username>.*)',
            request.GET['ip'])
        if datos:
            ip = datos.group('ip')
            appservip = datos.group('appservip')
            display = datos.group('display')
            username = datos.group('username')
            code = datos.group('code')
            html = "<html><body>CODE4<br>IP: %s<br>APPSERVIP: %s<br>DISPLAY: "\
            "%s<br>Code: %s<br>Username: %s</body></html>" % (ip, appservip,
            display, code, username)

    return HttpResponse(html)