import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
datasets = kaggle.api.dataset_list(search="covid", file_type='csv')
kaggle.api.dataset_download_file(dataset=datasets[0].ref, file_name='country_wise_latest.csv', path='dataset_download')
