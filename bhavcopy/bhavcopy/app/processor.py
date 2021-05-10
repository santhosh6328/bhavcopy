import json
import zipfile, downloader, redis
import pandas as pd

# redis must be locally running,
# steps to install to be added in readme
r = redis.Redis()


def unzip():
    with zipfile.ZipFile('../downloaded_zip/' + downloader.fileNameConstrutor(), 'r') as zip_ref:
        zip_ref.extractall('../downloaded_zip')


def read_csv():
    # to modify the csv with only required content
    data = pd.read_csv('../downloaded_zip/' + downloader.fileNameConstrutor(), encoding='unicode_escape')
    data.drop('SC_GROUP', inplace=True, axis=1)
    data.drop('SC_TYPE', inplace=True, axis=1)
    data.drop('LAST', inplace=True, axis=1)
    data.drop('PREVCLOSE', inplace=True, axis=1)
    data.drop('NO_TRADES', inplace=True, axis=1)
    data.drop('NO_OF_SHRS', inplace=True, axis=1)
    data.drop('NET_TURNOV', inplace=True, axis=1)
    data.drop('TDCLOINDI', inplace=True, axis=1)
    sc_code = data['SC_CODE'].tolist()

    sc_name = data['SC_NAME'].tolist()
    sc_high = data['HIGH'].tolist()
    sc_low = data['LOW'].tolist()
    sc_open = data['OPEN'].tolist()
    sc_close = data['CLOSE'].tolist()

    redis_dict = dict(zip(sc_code, zip(*(map(str, lst) for lst in (sc_name, sc_open, sc_close, sc_high, sc_low)))))

    for key in redis_dict:
        r.set(key, json.dumps(redis_dict[key]))


unzip()
read_csv()
