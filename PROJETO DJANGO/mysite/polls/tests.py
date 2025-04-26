# polls/tests.py
from django.test import TestCase
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        # Teste para verificar se a data de publicação é recente
        pass
