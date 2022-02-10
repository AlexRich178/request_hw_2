import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file(self, path_to_file):
        link_dict = self.get_upload_link(path_to_file=path_to_file)
        href = link_dict.get('href', '')
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('File upload successfully.')


if __name__ == '__main__':
    path_to_file = 'text_file.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload_file(path_to_file)
