import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import json
import time

def Gold():
    Gold_Url = "https://xn--42cah7d0cxcvbbb9x.com/"
    response = requests.get(Gold_Url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr", class_="trline")

    data = {}

    if len(rows) > 1:
        bar_sell_td = rows[1].find_all("td")
        if len(bar_sell_td) >= 3:
            data["barSell"] = bar_sell_td[2].text.strip()
            data["barBuy"] = bar_sell_td[1].text.strip()

    if len(rows) > 2:
        ornament_sell_td = rows[2].find_all("td")
        if len(ornament_sell_td) >= 3:
            data["ornamentSell"] = ornament_sell_td[2].text.strip()
            data["ornamentBuy"] = ornament_sell_td[1].text.strip()

    if len(rows) > 3:
        status_change_span = rows[3].find("span", class_="css-sprite-up")#เช็คว่าค่าขึ้นหรือลง
        if status_change_span:
            data["statusChange"] = "ทองขึ้น"  # Assuming "ทองขึ้น"
        else:
            status_change_span = rows[3].find("span", class_="img-down") #เช็คว่าค่าขึ้นหรือลง
            if status_change_span:
                data["statusChange"] = "ทองลง"  # Assuming "ทองลง"
        
        today_change_td = rows[3].find_all("td")
        if len(today_change_td) >= 3:
            data["todayChange"] = today_change_td[2].text.strip()

    if len(rows) > 4:
        updated_date_td = rows[4].find_all("td")
        if len(updated_date_td) >= 3:
            data["updatedDate"] = updated_date_td[0].text.strip()
            data["updatedTime"] = updated_date_td[1].text.strip()
            data["updatedCount"] = updated_date_td[2].text.strip()

    return data

def main(data):
    
    load_dotenv()

    TO = os.getenv('TO')
    AUTHORIZATION = os.getenv('AUTHORIZATION')
    colorCode = "#666666"
    if data.get("statusChange") == "ทองขึ้น":
        colorCode = "#64a338"
    elif data.get("statusChange") == "ทองลง":
        colorCode = "#e03b24"

    bubble_json = {
        "to": TO,
        "messages": [
            {
                "type": "flex",
                "altText": "ราคาทองวันนี้",
                "contents": {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://i.postimg.cc/3xxWh7Ln/bullion-1744773-1280.jpg",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "text",
                                "text": "ราคาทองวันนี้",
                                "size": "xl",
                                "gravity": "center",
                                "weight": "bold",
                                "wrap": True
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ทองคำแท่ง (ซื้อ)",
                                                "flex": 4,
                                                "size": "sm",
                                                "color": "#AAAAAA"
                                            },
                                            {
                                                "type": "text",
                                                "text": data.get("barBuy", ""),
                                                "flex": 3,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#666666",
                                                "wrap": True
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ทองคำแท่ง (ขาย)",
                                                "flex": 4,
                                                "size": "sm",
                                                "color": "#AAAAAA"
                                            },
                                            {
                                                "type": "text",
                                                "text": data.get("barSell", ""),
                                                "flex": 3,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#666666",
                                                "wrap": True
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ทองรูปพรรณ (ซื้อ)",
                                                "flex": 4,
                                                "size": "sm",
                                                "color": "#AAAAAA"
                                            },
                                            {
                                                "type": "text",
                                                "text": data.get("ornamentBuy", ""),
                                                "flex": 3,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#666666",
                                                "wrap": True
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ทองรูปพรรณ (ขาย)",
                                                "flex": 4,
                                                "size": "sm",
                                                "color": "#AAAAAA"
                                            },
                                            {
                                                "type": "text",
                                                "text": data.get("ornamentSell", ""),
                                                "flex": 3,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#666666",
                                                "wrap": True
                                            }
                                        ]
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "xxl",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "การเปลี่ยนแปลงวันนี้",
                                                "flex": 4,
                                                "size": "sm",
                                                "color": "#AAAAAA"
                                            },
                                            {
                                                "type": "text",
                                                "text": f'{data.get("todayChange", "")} {data.get("statusChange", "")}',
                                                "flex": 3,
                                                "size": "sm",
                                                "align": "end",
                                                "weight": "bold",
                                                "color": colorCode,
                                                "wrap": True
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "margin": "xxl",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": f'{data.get("updatedDate", "")} {data.get("updatedTime", "")} {data.get("updatedCount", "")}',
                                                "size": "sm",
                                                "align": "end"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        ]
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AUTHORIZATION}'
    }

    response = requests.post(
        'https://api.line.me/v2/bot/message/push',
        headers=headers,
        data=json.dumps(bubble_json)
    )

    print(response.status_code)
    print(response.text)
    

def main_loop():
    previous_data = None
    while True:
        data = Gold()
        if data != previous_data:
            main(data)
            previous_data = data
        time.sleep(60)  # Sleep for 1 minute
        
main_loop()