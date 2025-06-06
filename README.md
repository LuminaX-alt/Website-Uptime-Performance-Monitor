# Website-Uptime-Performance-Monitor
# Website Uptime and Performance Monitor (Google Colab)

This project is a Python-based Website Uptime and Performance Monitor designed to run entirely within Google Colab. It periodically checks whether one or more websites are accessible, records their response times, and logs performance data. The system can also send real-time email alerts if a monitored site becomes unavailable.

---

## Features

- Monitor multiple websites in real time
- Measure and log HTTP status and response time
- Plot website response time over time using Matplotlib
- Calculate uptime percentage for each monitored website
- Send email alerts when a site is detected as down (single alert per outage)
- Export logs to CSV format
- Optional: Real-time URL status checker using Gradio interface

---

## Project Files

| File                      | Description                                              |
|---------------------------|----------------------------------------------------------|
| `website_monitor.ipynb`   | Main Colab notebook with all monitoring logic            |
| `README.md`               | Project documentation and instructions                   |
| `log_<website>.csv`       | Auto-generated logs for each website                     |
| `report_<date>.pdf`       | Optional performance summary (planned feature)           |

---

## How It Works

1. **Website List**
   - Add target websites to a Python list:
     ```python
     websites = ['https://www.google.com', 'https://www.github.com']
     ```

2. **Monitoring Loop**
   - Periodically checks each site for:
     - Availability (`UP` or `DOWN`)
     - Response time in seconds
     - Current timestamp
   - Results are printed and stored in memory for graphing and reporting

3. **Response Time Visualization**
   - Graphs are generated using `matplotlib` to show response time trends

4. **Uptime Percentage**
   - Calculates how often each site was up during the monitoring period

5. **Email Notifications**
   - Sends an email when a site goes down using a secure Gmail app password

---

## Email Alert Setup (Gmail App Password)

1. Enable 2-Step Verification on your Google account
2. Visit: https://myaccount.google.com/apppasswords
3. Generate an app password for "Mail"
4. Replace your actual Gmail password with this generated app password in the code:
   ```python
   server.login("your_email@gmail.com", "your_app_password")







    
<img width="658" alt="image" src="https://github.com/user-attachments/assets/de739d59-3685-40c3-bfe2-9e4724c7054b" />

 <img width="735" alt="image" src="https://github.com/user-attachments/assets/874d2ea9-b031-4a73-9507-5bd8ad5e7004" />

 <img width="662" alt="image" src="https://github.com/user-attachments/assets/56ff02ec-5138-4280-b146-fe07e2175042" />
   
<img width="1295" alt="image" src="https://github.com/user-attachments/assets/2803a9f6-8b7a-4841-ade1-572cfe7ca340" />




