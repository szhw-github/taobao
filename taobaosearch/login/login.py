
from login.settings import *
from log import log
import sys,time,random
sys.path.insert(0,IMPORTPATH)
from pyppeteer.launcher import launch
import asyncio
from login.exe_js import js1, js3, js4, js5

class Login():
    def __init__(self,browser,page,username,pwd):
        self.__b=browser
        self.__p=page
        self.__un=username
        self.__pwd=pwd


    @classmethod
    async def open_logpage(cls):
        browser = await launch({'headless': True, 'args': ['--no-sandbox'], })
        page = await browser.newPage()
        await page.setUserAgent(UA)
        await page.goto(URL_LOG)
        await page.evaluate(js1)
        await page.evaluate(js3)
        await page.evaluate(js4)
        await page.evaluate(js5)
        return cls(
            browser=browser,
            page=page,
            username=USERNAME,
            pwd=PWD
        )


    async def login(self):
        log('输入账号')
        await self.__p.type('.J_UserName', self.__un, {'delay': random.randint(100, 151) - 50})
        await self.__p.type('#J_StandardPwd input', self.__pwd, {'delay': random.randint(100, 151) - 50})
        time.sleep(2)
        fail = 'go on'
        while fail=='go on':
            fail = await self.__enter()
        await self.__b.close()
        return fail


    async def __enter(self):
        slider = await self.__p.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块
        if slider:
            flag = await self.__mouse_slide()
            if flag:
                await self.__get_cookie()
                await self.__p.click('#J_SubmitStatic')
                await self.__p.waitForNavigation()
                cookie = await self.__get_cookie()
                return cookie
            else:
                return 'fail'
        else:
            log('没有滑块')
            await self.__p.keyboard.press('Enter')
            await self.__p.waitForNavigation()
            try:
                global error
                error = await self.__p.Jeval('.error', 'node => node.textContent')
            except Exception as e:
                error = None

            finally:
                if error:
                    log('没有滑块,登录失败')
                    await self.__p.type('#J_StandardPwd input', self.__pwd, {'delay': random.randint(100, 151)})
                    return 'go on'
                else:
                    log('没有滑块,登录成功')
                    cookie=await self.__get_cookie()
                    return cookie


    async def __mouse_slide(self):
        try:
            log('滑动模块')
            await self.__p.hover('#nc_1_n1z')
            await self.__p.mouse.down()
            await self.__p.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
            await self.__p.mouse.up()
            time.sleep(3)

        except Exception as e:
            log(e)
            return 0

        else:
            slider_again = await self.__p.Jeval('.nc-lang-cnt', 'node => node.textContent')
            if slider_again != '验证通过':
                log('验证失败')
                return 0
            else:
                log('验证通过')
                return 1


    async def __get_cookie(self):
        res = await self.__p.content()
        cookies_list = await self.__p.cookies()
        cookies = ''
        for cookie in cookies_list:
            str_cookie = '{0}={1};'
            str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
            cookies += str_cookie
        return cookies

