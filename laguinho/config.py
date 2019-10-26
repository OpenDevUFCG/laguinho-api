import os


class BaseConfig:
    MONGO_HOST = os.getenv('LAGUINHO_MONGO_HOST', default='localhost')
    MONGO_PORT = os.getenv('LAGUINHO_MONGO_PORT', default='27017')
    MONGO_DBNAME = os.getenv('LAGUINHO_MONGO_DBNAME', default='laguinho')
    MONGO_USERNAME = os.getenv('LAGUINHO_MONGO_USERNAME',
                               default='opendevufcg')
    MONGO_PASSWORD = os.getenv('LAGUINHO_MONGO_PASSWORD',
                               default='laguinhoapi')
    MONGO_AUTH_SOURCE = os.getenv('LAGUINHO_MONGO_AUTH_SOURCE',
                               default='admin')
    MONGO_URI = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}?authSource={MONGO_AUTH_SOURCE}'
