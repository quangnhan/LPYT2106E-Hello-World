import requests


class MockApi:
    __url = "https://611ba6e422020a00175a460d.mockapi.io"

    def get_products_by_category(self, category):
        url = f"{self.__url}/category/{category}/products"
        response = requests.get(url)
        return response.json()
