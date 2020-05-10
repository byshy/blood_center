from django.utils import timezone

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from api.models import BloodCenter, Donor, History

User = get_user_model()


class GlobalSetUp(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            id="405134123",
            email="email@example.com",
            mobile="0567817018",
            password="some pass",
            username="n"
        )
        self.token = Token.objects.create(user=self.user)
        self.api_auth()

        self.center = BloodCenter.objects.create(longitude=120.1, latitude=32.5, name="GBC")
        self.donor = Donor.objects.create(id=self.user, gender=1, age=20, blood_type=1)
        self.donor_history = History.objects.create(date=timezone.now(), user_id=self.donor,
                                                    blood_center_id=self.center)

    def api_auth(self):
        self.client.force_authenticate(self.user, self.token)


class BloodCenterListViewTestCase(GlobalSetUp):
    list_blood_center_url = reverse("api_home:get_blood_centers")

    def test_get_all_centers(self):
        response = self.client.get(self.list_blood_center_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BloodCenterViewTestCase(GlobalSetUp):
    get_blood_center_url = reverse("api_home:get_blood_center", kwargs={'name': "GBC"})
    get_missing_blood_center_url = reverse("api_home:get_blood_center", kwargs={'name': "not a center"})
    get_blood_center_wrong_arg_url = reverse("api_home:get_blood_center", kwargs={'name': 1})

    def test_get_center(self):
        response = self.client.get(self.get_blood_center_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], 'GBC')

    def test_no_center_found(self):
        # successful test
        response = self.client.get(self.get_missing_blood_center_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_wrong_center_name(self):
        # successful test
        response = self.client.get(self.get_blood_center_wrong_arg_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_center_unauthorized(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.get_blood_center_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class DonorViewTestCase(GlobalSetUp):
    get_donor_url = reverse("api_home:get_donor", kwargs={'id': "405134123"})
    # get_missing_donor_url = reverse("api_home:get_donor", kwargs={'id': "not an id"})
    # this test is not possible since a str can't be converted to int.
    get_donor_wrong_arg_url = reverse("api_home:get_donor", kwargs={'id': 1})

    def test_get_donor(self):
        response = self.client.get(self.get_donor_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['id'], '405134123')

    def test_wrong_id(self):
        # successful test
        response = self.client.get(self.get_donor_wrong_arg_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_donor_unauthorized(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.get_donor_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class HistoryListViewTestCase(GlobalSetUp):
    get_donor_history_url = reverse("api_home:get_donor_history", kwargs={'user_id': "405134123"})
    # get_missing_donor_history_url = reverse("api_home:get_donor_history", kwargs={'user_id': "not an id"})
    # this test is not possible since a str can't be converted to int.
    get_donor_history_wrong_arg_url = reverse("api_home:get_donor_history", kwargs={'user_id': 1})

    def test_get_donor_history(self):
        response = self.client.get(self.get_donor_history_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(len(response.data), 0)

    def test_wrong_user_id(self):
        response = self.client.get(self.get_donor_history_wrong_arg_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_center_unauthorized(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.get_donor_history_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
