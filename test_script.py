import laguinho
import unittest
import json

class FlaskTestCase(unittest.TestCase):
    app = laguinho.create_app()
    tester = app.test_client()
    content_sent = {
        "name": "Name Teste",
        "url": "https://url.teste.com",
        "path": "path/teste",
        "maintainers": [
            "Maintainer Teste One",
            "Maintainer Teste Two",
            "Maintainer Teste Three"
        ],
        "format": "csv",
        "contributable": True
    }

    def test_index(self):
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_datasets_publish(self):
        response = self.tester.post('/datasets', data=json.dumps(self.content_sent), content_type='application/json')

        # verificando se o item é igual ao content_sent
        self.assertEqual(json.loads(response.data), self.content_sent)

    def test_datasets_get_datasets(self):
        self.tester.post('/datasets', data=json.dumps(self.content_sent), content_type='application/json')
        self.tester.post('/datasets', data=json.dumps(self.content_sent), content_type='application/json')
        response = self.tester.get('/datasets', content_type='html/text')
        response_json = json.loads(response.data)

        # verificando se a lista contém 2 itens
        self.assertEqual(len(response_json), 2)
        # verificando se o primeiro item da lista é igual ao content_sent
        self.assertEqual(response_json[1], self.content_sent)
    
    def test_datasets_get_datasets_by_name(self):
        self.tester.post('/datasets', data=json.dumps(self.content_sent), content_type='application/json')
        response = self.tester.get('/datasets/Name%20Teste')

        # verificando se o item é igual ao content_sent
        self.assertEqual(json.loads(response.data), self.content_sent)

if __name__ == '__main__':
    unittest.main()