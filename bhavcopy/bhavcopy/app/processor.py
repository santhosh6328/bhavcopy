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

    #convert columns to dict and push to redis
    sc_list = data.to_dict()
    for key in sc_list:
        r.set(key, json.dumps(sc_list[key]))

unzip()
read_csv()
