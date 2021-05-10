import requests, os, logging
from datetime import date
from urllib.parse import urlparse


def download_csv():
    url = urlConstrutor()
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        a = requests.get(url, headers=headers)
        if (a.status_code == 404):
            print(a.status_code)
            return
        u = urlparse(url)
        print(os.path.basename(u.path))
        with open('../downloaded_zip/' + os.path.basename(u.path), 'wb') as f:
            f.write(a.content)
    except requests.ConnectionError:
        print('Failed to download with status code: ' + a.status_code)
        logging.info("download failed: possible reasons = weekend, bse server unavailable")
    print(a.status_code)
    return


def dateIdentifier():
    todays_date = date.today()
    return (str(todays_date.day).zfill(2), str(todays_date.month).zfill(2), str(todays_date.year))


def urlConstrutor():
    day, month, year = dateIdentifier()
    return 'https://www.bseindia.com/download/BhavCopy/Equity/EQ' + day + month + year + '_CSV.ZIP'


def fileNameConstrutor():
    day, month, year = dateIdentifier()
    return 'EQ' + day + month + year + '_CSV.ZIP'


download_csv()
