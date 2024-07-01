from http_client import CMCHttpClient
from config import settings


cmc_client = CMCHttpClient(base_url='https://pro-api.coinmarketcap.com', api_key=settings.CMC_API_KEY)