from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from app_gadgets.models import TechBox, IssueGadget, Employee
# Create your tests here.

class TechBoxAPITestCase(APITestCase):
    def setUp(self):
        self.username = "vaibhav"
        self.email = "vaibhav@gmail.com"
        self.password = "some_strong_pass"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        TechBox.objects.create(name="XYZ", available="True")
        TechBox.objects.create(name="Mouse", available="True")
        TechBox.objects.create(name="Webcam", available="True")

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_01_get_method(self):
        url = 'http://127.0.0.1:8000/gadgets/gadget_api/'
        response = self.client.get(url)
        print("GET Method: ",response.status_code)
        self.assertEqual(response.status_code, 200)
        data = TechBox.objects.all().count()
        print(data)
        self.assertEqual(data, 3)


    def test_02_get_method_with_key(self):
        url = 'http://127.0.0.1:8000/gadgets/gadget_api/1/'
        # data = {'pk': 1}
        response = self.client.get(url)
        print("GET Method with key: ",response.status_code)
        self.assertEqual(response.status_code, 200)


    def test_03_post_method_success(self):
        url = 'http://127.0.0.1:8000/gadgets/gadget_api/'
        data = {'name':'Pendrive', 'available':'True'}
        response = self.client.post(url, data, format='json')
        print("POST Method is working: ",response.status_code)
        self.assertEqual(response.status_code, 201)

    def test_04_post_method_fail(self):
        url = 'http://127.0.0.1:8000/gadgets/gadget_api/'
        data = {'available':'True'}
        response = self.client.post(url, data, format='json')
        print("POST Method is not working: ",response.status_code)
        self.assertEqual(response.status_code, 400)

    def test_05_delete_method_success(self):
        url = 'http://127.0.0.1:8000/gadgets/gadget_api/1/'
        # data = {'id': 1}
        response = self.client.delete(url, format="json")
        print("DELETE Method works: ",response.status_code)
        self.assertEqual(response.status_code, 200)



    def test_06_put_method_success(self):
        url = 'http://127.0.0.1:8000/gadgets/gadget_api/1/'
        data = {'name': 'XYZ', 'available': 'False'}
        response = self.client.put(url, data=data, format='json')
        print("Update Works: ",response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_07_put_method_fail(self):
        url = 'http://127.0.0.1:8000/gadgets/gadget_api/1/'
        data = {'available': 'False'}
        response = self.client.put(url, data=data, format='json')
        print("Update doesnt Works:", response.status_code)
        self.assertEqual(response.status_code, 400)


class IssueGadgetAPITestCase(APITestCase):
    def setUp(self):
        self.username = "vaibhav"
        self.email = "vaibhav@gmail.com"
        self.password = "some_strong_pass"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        TechBox.objects.create(name="XYZ", available="True")
        TechBox.objects.create(name="Mouse", available="True")
        TechBox.objects.create(name="Webcam", available="False")
        emp_data = Employee.objects.create(name="vaibhav", email="abc@gmail.com", emp_code='10', department="Python", address="XYZ", city="Neemuch", phone="1234", date_joined="April 30, 2021")

        gadget_1 = TechBox.objects.get(name="XYZ")
        gadget_2 = TechBox.objects.get(name="Webcam")
        print(gadget_1.name)
        print(gadget_2.name)
        IssueGadget.objects.create(gadget_name=gadget_1, emp_code=10)
        IssueGadget.objects.create(gadget_name=gadget_1, emp_code=20)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_01_get_method(self):
        url = 'http://127.0.0.1:8000/gadgets/issue_gadget_api/'
        response = self.client.get(url)
        print("GET Method: ", response.status_code)
        self.assertEqual(response.status_code, 200)
        data = IssueGadget.objects.all().count()
        print(data)
        self.assertEqual(data, 2)

    def test_02_post_method_fail(self):
        url = 'http://127.0.0.1:8000/gadgets/issue_gadget_api/'
        data = {'gadget_name':'Mouse','emp_code': 30}
        response = self.client.post(url, data, format='json')
        print("POST Method is working: ",response.status_code)
        self.assertEqual(response.status_code, 400)

    def test_02_post_method_pass(self):
        url = 'http://127.0.0.1:8000/gadgets/issue_gadget_api/'
        data = {
            "id": 1,
            "issue_date": "2021-04-30",
            "expire_date": "2021-04-30T11:43:53+05:30",
            "emp_code": "10",
            "gadget_name": 2
    }
        response = self.client.post(url, data, format='json')
        print("POST Method is working: ",response.status_code)
        self.assertEqual(response.status_code,200)
















