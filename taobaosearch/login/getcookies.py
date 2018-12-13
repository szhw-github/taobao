
from log import log
import asyncio,time,random
from login.login import Login

def get_cookies():
    log('START LOGIN')
    loop = asyncio.get_event_loop()
    cookie='fail'
    while cookie=='fail':
        log('try to get cookies')
        time.sleep(random.randint(10,30))
        try:
            page=loop.run_until_complete(Login.open_logpage())
            cookie=loop.run_until_complete(page.login())
        except:
            log('try fail')
            continue
        log('try secceed')
        return cookie

if  __name__=='__main__':
    get_cookies()


