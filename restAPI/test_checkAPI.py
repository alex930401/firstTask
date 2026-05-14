import requests
import pytest
import allure

@pytest.mark.APITest
class Test_CheckAPI():

    @allure.title("Проверка результат get запроса")
    @allure.tag("Позитивный кейс")
    @pytest.mark.critReg
    def test_get_request(self):
    #Ожидаемый результат
        result_json = {
          "userId": 1,
          "id": 1,
          "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
          "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }

        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        data = response.json()

        with allure.step("Проверяем статус обработки запроса, должен быть 200:"):
            assert response.status_code == 200

        with allure.step("Проверяем полученного Json-сообщение:"):
            assert data == result_json

    @allure.title("Проверка результат post запроса")
    @allure.tag("Позитивный кейс")
    @pytest.mark.critReg
    def test_post_request(self):
        # Ожидаемый результат
        result_json = {
                'id': 101,
                'title': 'foo',
                'body': 'bar',
                'userId': 1
            }

        url = "https://jsonplaceholder.typicode.com/posts"
        headers = {
            'Content-type': 'application/json; charset=UTF-8',
        }
        body = {
           'title': 'foo',
            'body': 'bar',
            'userId': 1,
          }

        response = requests.post(url, json=body, headers=headers)
        data = response.json()

        with allure.step("Проверяем статус обработки запроса, должен быть 200:"):
            assert response.status_code == 201

        with allure.step("Проверяем полученного Json-сообщение:"):
            assert data == result_json