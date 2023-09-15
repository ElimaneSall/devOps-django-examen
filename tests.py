# import os
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.test import TestCase
#
# # Configure Django settings for testing
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monprojet.settings")
# # os.environ['DJANGO_SETTINGS_MODULE'] = 'monprojet.settings'  # Remplacez 'monprojet' par le nom de votre projet Django
# settings.configure()
#
# # Votre suite de tests commence ici
# class TestListeUtilisateurs(TestCase):
#     def setUp(self):
#         # Créez des utilisateurs de test pour les besoins des tests
#         self.user1 = User.objects.create(username='user1', email='user1@example.com', first_name='John',
#                                          last_name='Doe')
#         self.user2 = User.objects.create(username='user2', email='user2@example.com', first_name='Jane',
#                                          last_name='Smith')
#
#     def test_liste_utilisateurs(self):
#         # Utilisez la méthode reverse pour obtenir l'URL de l'endpoint
#         url = reverse('liste-utilisateurs')
#
#         # Effectuez une requête GET à l'URL de l'endpoint
#         response = self.client.get(url)
#
#         # Vérifiez que la réponse a le code HTTP 200 (OK)
#         self.assertEqual(response.status_code, 200)
#
#         # Vérifiez que la réponse contient les données attendues
#         self.assertContains(response, 'user1')
#         self.assertContains(response, 'user1@example.com')
#         self.assertContains(response, 'John')
#         self.assertContains(response, 'Doe')
#         self.assertContains(response, 'user2')
#         self.assertContains(response, 'user2@example.com')
#         self.assertContains(response, 'Jane')
#         self.assertContains(response, 'Smith')


from django.test import TestCase
from django.urls import reverse
from monprojet.account.models import Visit


class TestIncrementerCompteurVisites(TestCase):
    def test_incrementer_compteur_visites(self):
        # Assurez-vous qu'il n'y a pas encore d'objet Visit dans la base de données
        self.assertEqual(Visit.objects.count(), 0)

        # Utilisez la méthode reverse pour obtenir l'URL de l'endpoint
        url = reverse('visites')

        # Effectuez une requête GET à l'URL de l'endpoint
        response = self.client.get(url)

        # Vérifiez que la réponse a le code HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Vérifiez que l'objet Visit a été créé dans la base de données
        self.assertEqual(Visit.objects.count(), 1)

        # Récupérez l'objet Visit créé
        visit = Visit.objects.first()

        # Vérifiez que le compteur de visites a été incrémenté
        self.assertEqual(visit.count, 1)

