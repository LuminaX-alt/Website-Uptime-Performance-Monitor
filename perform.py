!pip install matplotlib
import requests
import time
import matplotlib.pyplot as plt
from datetime import datetime
def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status = "UP" if response.status_code == 200 else f"DOWN ({response.status_code})"
        response_time = response.elapsed.total_seconds()
    except requests.exceptions.RequestException:
        status = "DOWN"
        response_time = None
    return status, response_time
websites = ['https://www.google.com', 'https://www.github.com', 'https://yourwebsite.com']

log = {site: {"timestamps": [], "statuses": [], "response_times": []} for site in websites}
monitoring_duration = 5 * 60  # Monitor for 5 minutes
interval = 30  # Check every 30 seconds

start_time = time.time()

print("🔍 Monitoring started...\n")
while time.time() - start_time < monitoring_duration:
    now = datetime.now().strftime("%H:%M:%S")
    for site in websites:
        status, response_time = check_website(site)
        log[site]["timestamps"].append(now)
        log[site]["statuses"].append(status)
        log[site]["response_times"].append(response_time)
        print(f"[{now}] {site} → {status} | Response Time: {response_time:.2f}s" if response_time else f"[{now}] {site} → {status}")
    time.sleep(interval)
for site in websites:
    times = log[site]["timestamps"]
    responses = log[site]["response_times"]

    plt.figure(figsize=(10, 4))
    plt.plot(times, responses, marker='o', label='Response Time (s)')
    plt.xticks(rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Response Time (seconds)")
    plt.title(f"📈 Performance Monitor - {site}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
!pip install gradio

import gradio as gr

def check_live(url):
    status, response_time = check_website(url)
    return f"Status: {status}\nResponse Time: {response_time if response_time else 'N/A'} seconds"

gr.Interface(fn=check_live, inputs="text", outputs="text", title="🌐 Website Uptime Checker").launch()
import pandas as pd

for site in websites:
    df = pd.DataFrame({
        "Timestamp": log[site]["timestamps"],
        "Status": log[site]["statuses"],
        "Response Time": log[site]["response_times"]
    })
    df.to_csv(f"{site.replace('https://','').replace('.','_')}_log.csv", index=False)
import smtplib
from email.mime.text import MIMEText

def send_email_alert(site):
    msg = MIMEText(f"Alert! The website {site} is DOWN.")
    msg['Subject'] = f"🚨 Website Down Alert: {site}"
    msg['From'] = '********'
    msg['To'] = '**********'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("*********", "**********")  # Use App Password
    server.send_message(msg)
    server.quit()
down_flags = {site: False for site in websites}

for site in websites:
    status, response_time = check_website(site)
    if status == "DOWN":
        if not down_flags[site]:  # Only alert once
            send_email_alert(site)
            down_flags[site] = True
    else:
        down_flags[site] = False
