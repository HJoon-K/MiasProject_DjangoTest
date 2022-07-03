from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt  # csrf 적용 X

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json


# Create your views here.
class CarView(View):
    def get(self, request):
        form = request.GET.dict()
        # print(form)
        try:
            carno = form['carno']
            bymd = form['bymd']
        except:
            return render(request, 'p_visit.html')


        URL = 'https://www.cyberts.kr/cp/pvr/cpr/readCpPvrCarPrsecResveMainView.do'

        # options = Options() # 옵션을 조정하기 위한셋팅
        # options.add_argument('--blink-settings=imagesEnabled=false') # 이미지 로딩안하게 옵션셋팅

        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        driver.implicitly_wait(time_to_wait=5) # 로딩대기 (암묵적) 최대 5초까지

        driver.get(url=URL)
        tabs = driver.window_handles
        driver.implicitly_wait(time_to_wait=5)

        driver.switch_to.window(driver.window_handles[0])
        keyword = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td/ul/li/input")  # 검색 속성 찾기
        keyword.send_keys(carno)  # 검색어 입력

        keyword = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/ul/li/input")  # 검색 속성 찾기
        keyword.send_keys(bymd)  # 검색어 입력

        keyword.send_keys("\ue007")  # 검색후 enter키 입력

        fdate = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[1]")
        edate = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[2]")
        pdate = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[3]")

        print(f'{fdate.text} / {edate.text} / {pdate.text}')

        context = {'fdate': fdate.text, 'edate': edate.text}
        print(context)

        # return render(request, 'p_visit.html')
        return HttpResponse(json.dumps(context), content_type='application/json')


    def post(self, request):
        pass
