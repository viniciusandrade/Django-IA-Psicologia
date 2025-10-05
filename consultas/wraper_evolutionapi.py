import requests
from urllib.parse import urlencode, urljoin
from django.conf import settings

class BaseEVolutionAPI:

    def __init__(self):
        self._BASE_URL = settings.EVOLUTION_API_URL
        self._API_KEY =  settings.EVOLUTION_API_KEY_INSTANCE

    
    def _send_request(
        self,
        path,
        method='GET',
        body=None,
        headers={},
        params_url={}
    ):
        method =method.upper()
        url = self._mount_url(path, params_url)
        
        if not isinstance(headers, dict):
            headers = {}

        headers.setdefault('Content-Type', 'application/json')
        instance = self._get_instance(path)
        headers['apikey'] = self._API_KEY

        request = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete
        }.get(method)

        return request(url, headers=headers, json=body)
        
    def _mount_url(self, path, params_url):
        if isinstance(params_url, dict):
            parameters = urlencode(params_url)
        
        url = urljoin(self._BASE_URL, path)

        if parameters:
            url = url + '?' + parameters
        return url
        
    def _get_instance(self, path):
        return path.strip('/').split('/')[-1]


class SendMessage(BaseEVolutionAPI):

    def send_message(self, instance, body):
        path = f'/message/sendText/{instance}/'
        return self._send_request(path, method='POST', body=body)