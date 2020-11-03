# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import json, urllib.request
from urllib.parse import urlencode
import time


# ----------------------------------
#  Juhe Data
#  Interface Document：https://www.juhe.cn/docs/api/id/39
# ----------------------------------

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '''<h1>Home</h1> 
    <p><a href="/cityweather">Weather Forecast</a></p>'''

@app.route('/cityweather', methods=['GET'])
def login_form():
    return '''<form action="/cityweather" method="post">
    <p> City Name <input name="cityname"></p>
    <p><button type="submit">Weather</button></p>
    </form>'''

@app.route('/cityweather', methods=['POST'])
def login():
    # Configure API Key

    appkey = "0e6a91cf59f2b69971aeb9df66b97bfe"

    cityname = request.form['cityname']

    # 1.City Weather Searching
    response = request1(cityname, appkey, "GET").replace("'", '"')
    response_json = json.loads(response)
    CurrentTemp = json.dumps(response_json['sk'].get("temp"))
    CurrentWindDirection = json.dumps(response_json['sk'].get("wind_direction"), ensure_ascii=False)
    CurrentWindStrength = json.dumps(response_json['sk'].get("wind_strength"), ensure_ascii=False)
    CurrentHumidity = json.dumps(response_json['sk'].get("humidity"))
    CurrentTime = json.dumps(response_json['sk'].get("time"))
    TodayTemp = json.dumps(response_json['today'].get("temperature"), ensure_ascii=False)
    TodayWeather = json.dumps(response_json['today'].get("weather"),ensure_ascii=False)
    TodayWind = json.dumps(response_json['today'].get("wind"), ensure_ascii=False)
    TodayWeek = json.dumps(response_json['today'].get("week"), ensure_ascii=False)
    Date = json.dumps(response_json['today'].get("date_y"), ensure_ascii=False)
    TodayDressing = json.dumps(response_json['today'].get("dressing_index"), ensure_ascii=False)
    TodayDressingAdvice = json.dumps(response_json['today'].get("dressing_advice"), ensure_ascii=False)
    TodayUV = json.dumps(response_json['today'].get("uv_index"), ensure_ascii=False)
    TodayWash = json.dumps(response_json['today'].get("wash_index"), ensure_ascii=False)
    TodayTravel = json.dumps(response_json['today'].get("travel_index"), ensure_ascii=False)
    TodayExercise = json.dumps(response_json['today'].get("exercise_index"), ensure_ascii=False)

    TodayDate = time.strftime('%Y%m%d', time.localtime(time.time()))
    FutureDate = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 1)].get("date"),
                                   ensure_ascii=False)
    FutureWeek = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 1)].get("week"),
                            ensure_ascii=False)
    FutureTemperature = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 1)].get("temperature"),
                                   ensure_ascii=False)
    FutureWeather = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 1)].get("weather"),
                               ensure_ascii=False)
    FutureWind = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 1)].get("wind"),
                            ensure_ascii=False)

    FutureDate1 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 2)].get("date"),
                                   ensure_ascii=False)
    FutureWeek1 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 2)].get("week"),
                            ensure_ascii=False)
    FutureTemperature1 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 2)].get("temperature"),
                                   ensure_ascii=False)
    FutureWeather1 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 2)].get("weather"),
                               ensure_ascii=False)
    FutureWind1 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 2)].get("wind"),
                            ensure_ascii=False)

    FutureDate2 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 3)].get("date"),
                                   ensure_ascii=False)
    FutureWeek2 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 3)].get("week"),
                            ensure_ascii=False)
    FutureTemperature2 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 3)].get("temperature"),
                                   ensure_ascii=False)
    FutureWeather2 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 3)].get("weather"),
                               ensure_ascii=False)
    FutureWind2 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 3)].get("wind"),
                            ensure_ascii=False)

    FutureDate3 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 4)].get("date"),
                                   ensure_ascii=False)
    FutureWeek3 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 4)].get("week"),
                            ensure_ascii=False)
    FutureTemperature3 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 4)].get("temperature"),
                                   ensure_ascii=False)
    FutureWeather3 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 4)].get("weather"),
                               ensure_ascii=False)
    FutureWind3 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 4)].get("wind"),
                            ensure_ascii=False)

    FutureDate4 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 5)].get("date"),
                                   ensure_ascii=False)
    FutureWeek4 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 5)].get("week"),
                            ensure_ascii=False)
    FutureTemperature4 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 5)].get("temperature"),
                                   ensure_ascii=False)
    FutureWeather4 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 5)].get("weather"),
                               ensure_ascii=False)
    FutureWind4 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 5)].get("wind"),
                            ensure_ascii=False)

    FutureDate5 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 6)].get("date"),
                                   ensure_ascii=False)
    FutureWeek5 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 6)].get("week"),
                            ensure_ascii=False)
    FutureTemperature5 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 6)].get("temperature"),
                                   ensure_ascii=False)
    FutureWeather5 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 6)].get("weather"),
                               ensure_ascii=False)
    FutureWind5 = json.dumps(response_json['future']['day_' + str(int(TodayDate) + 6)].get("wind"),
                            ensure_ascii=False)

    return "<h>城市：<b>"+cityname+"</b>&nbsp;&nbsp;&nbsp;"+Date[1:-1]+"&nbsp;&nbsp;&nbsp;"+TodayWeek[1:-1]+"&nbsp;&nbsp;&nbsp;"+TodayTemp[1:-1]+"&nbsp;&nbsp;&nbsp;"+TodayWeather[1:-1]+"&nbsp;&nbsp;&nbsp;"+TodayWind[1:-1]+\
        "<p><b>今日提醒：</b><br><li>穿衣："+TodayDressing[1:-1]+"&nbsp;&nbsp;&nbsp;建议："+TodayDressingAdvice[1:-1]+\
             "<li>紫外线："+TodayUV[1:-1]+"&nbsp;&nbsp;&nbsp;外出："+TodayTravel[1:-1]+"&nbsp;&nbsp;&nbsp;洗衣："+TodayWash[1:-1]+"&nbsp;&nbsp;&nbsp;锻炼："+TodayExercise[1:-1]+\
           "<p><b>当前天气：</b><br><li>气温："+CurrentTemp[1:-1]+"<li>风向："+CurrentWindDirection[1:-1]+"<li>风力："+CurrentWindStrength[1:-1]+"湿度："+CurrentHumidity[1:-1]+"<li>时间："+CurrentTime[1:-1]+"<p><b>今日天气：</b><br><li>气温："+TodayTemp[1:-1]+"<li>天气："+TodayWeather[1:-1]+\
        "<p><b>明日天气：</b><br><li>日期："+FutureDate[1:-1]+"&nbsp;&nbsp;&nbsp"+FutureWeek[1:-1]+"<li>气温："+FutureTemperature[1:-1]+"<li>天气："+FutureWeather[1:-1]+"<li>风力："+FutureWind[1:-1]+\
        "<p><b>未来天气：</b><br><li>日期："+FutureDate1[1:-1]+"&nbsp;&nbsp;&nbsp"+FutureWeek1[1:-1]+"<li>气温："+FutureTemperature1[1:-1]+"<li>天气："+FutureWeather1[1:-1]+"<li>风力："+FutureWind1[1:-1]+\
        "<p><li>日期："+FutureDate2[1:-1]+"&nbsp;&nbsp;&nbsp"+FutureWeek2[1:-1]+"<li>气温："+FutureTemperature2[1:-1]+"<li>天气："+FutureWeather2[1:-1]+"<li>风力："+FutureWind2[1:-1]+\
        "<p><li>日期："+FutureDate3[1:-1]+"&nbsp;&nbsp;&nbsp"+FutureWeek3[1:-1]+"<li>气温："+FutureTemperature3[1:-1]+"<li>天气："+FutureWeather3[1:-1]+"<li>风力："+FutureWind3[1:-1]+\
        "<p><li>日期："+FutureDate4[1:-1]+"&nbsp;&nbsp;&nbsp"+FutureWeek4[1:-1]+"<li>气温："+FutureTemperature4[1:-1]+"<li>天气："+FutureWeather4[1:-1]+"<li>风力："+FutureWind4[1:-1]+\
        "<p><li>日期："+FutureDate5[1:-1]+"&nbsp;&nbsp;&nbsp"+FutureWeek5[1:-1]+"<li>气温："+FutureTemperature5[1:-1]+"<li>天气："+FutureWeather5[1:-1]+"<li>风力："+FutureWind5[1:-1]+""


# City Weather Searching
def request1(cityname,appkey, m="GET"):
    url = "http://v.juhe.cn/weather/index"
    params = {
        "cityname": cityname,  # city
        "key": appkey,  # APP Key
        "dtype": "",  # Return Data Type(Default json)
        "format": "",  # //Future 6 days Weather Forecast
    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # Successful Request
            return str(res["result"])

        else:
            return str(res["error_code"])+":"+str( res["reason"])

    else:
        return "request api error"


if __name__ == '__main__':
    app.run()