from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from account.models import Visit
from datetime import date

# Votre suite de tests commence ici
class TestListeUtilisateurs(TestCase):
    def setUp(self):
        # Créez des utilisateurs de test pour les besoins des tests
        self.user1 = User.objects.create(username='user1', email='user1@example.com', first_name='John',
                                         last_name='Doe')
        self.user2 = User.objects.create(username='user2', email='user2@example.com', first_name='Jane',
                                         last_name='Smith')

    def test_liste_utilisateurs(self):
        # Utilisez la méthode reverse pour obtenir l'URL de l'endpoint
        url = reverse('liste-utilisateurs')

        # Effectuez une requête GET à l'URL de l'endpoint
        response = self.client.get(url)

        # Vérifiez que la réponse a le code HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Vérifiez que la réponse contient les données attendues
        self.assertContains(response, 'user1')
        self.assertContains(response, 'user1@example.com')
        self.assertContains(response, 'John')
        self.assertContains(response, 'Doe')
        self.assertContains(response, 'user2')
        self.assertContains(response, 'user2@example.com')
        self.assertContains(response, 'Jane')
        self.assertContains(response, 'Smith')

class TestIncrementerCompteurVisites(TestCase):
    def test_incrementer_compteur_visites(self):
        today = date.today()
        # Créez un objet Visit fictif pour simuler les visites
        visit = Visit.objects.create(date=today, count=5)

        # Utilisez la méthode reverse pour obtenir l'URL de l'endpoint
        url = reverse('visites')

        # Effectuez une requête GET à l'URL de l'endpoint
        response = self.client.get(url)

        # Vérifiez que la réponse a le code HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Vérifiez que la réponse contient la date et le nombre de visites
        data = response.json()
        self.assertIn('Date', data)
        self.assertIn('Nombre de visites', data)

        # Vérifiez que les données renvoyées correspondent à celles de l'objet Visit fictif
        self.assertEqual(data['Date'], visit.date.strftime('%Y-%m-%d'))
        self.assertEqual(data['Nombre de visites'], visit.count)

