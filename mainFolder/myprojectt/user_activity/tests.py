from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import RequestLog, Task, TaskSummary, UserActivityLog


class MiddlewareTest(TestCase):
    """
    This class contains test methods to verify if the middleware is correctly
    logging requests for both authenticated and unauthenticated users.

    Methods:
        setUp(): Creates a test client and a test user for the test environment.
        test_logging_for_authenticated_user(): Tests if request logging works for authenticated user.
    """

    def setUp(self):
        """
        Set up the test environment.
        This method creates test client for sending HTTP requests and sample user for testing authenticated requests.
        """

        self.client = Client()    # Create a test client instance
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_logging_for_authenticated_user(self):
        """
        Test logging of HTTP requests for an authenticated user.
        This method logs in a test user, makes a GET request to a sample URL,
        and checks if the request log is correctly recorded in the database.
        """

        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/some-url/')
        log_entry = RequestLog.objects.latest('timestamp')
        self.assertEqual(log_entry.user.username, 'testuser')
        self.assertEqual(log_entry.method, 'GET')
        self.assertEqual(response.status_code, log_entry.status_code)


class SignalTest(TestCase):
    """
    Test case for testing Django signals related to user activity and task creation.
    Contains methods to verify that signals are correctly updating TaskSummary model upon task creation.

    Methods:
        setUp(): Creates a test user for the test environment.
        test_task_creation_updates_summary(): Tests if creating a task triggers update in TaskSummary model.
    """

    def setUp(self):
        """ Set up the test environment """

        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_task_creation_updates_summary(self):
        """ Test if creating a new task updates the TaskSummary """

        Task.objects.create(user=self.user, title='Test Task', description='Test Description')
        summary = TaskSummary.objects.get(user=self.user)
        self.assertEqual(summary.total_tasks_created, 1)
