
def translate_papago(text):

    import os
    import sys
    import urllib.request
    import json

    client_id = "3TWPuubaRXWr5vB99nDe"  # 개발자센터에서 발급받은 Client ID 값
    client_secret = "9mjVniEDpx"  # 개발자센터에서 발급받은 Client Secret 값
    url = "https://openapi.naver.com/v1/papago/n2mt"

    global trans_output
    
    data = "source=ko&target=en&text=" + text
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    response_body = response.read()
    jsonStr = json.loads(response_body.decode('utf-8'))

    trans_output = jsonStr['message']['result']['translatedText']

    return trans_output
