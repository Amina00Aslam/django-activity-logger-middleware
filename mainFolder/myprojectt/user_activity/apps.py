from django.apps import AppConfig


class UserActivityConfig(AppConfig):
    """
    Configuration class for the 'user_activity' app.

    This class is responsible for setting up configuration for 'user_activity' application. It includes
    automatic database ID configuration and ensures that signals are imported when the application is ready.

    Attributes:
        default_auto_field (str): Specifies the type of primary key to use for models.
        name (str): The name of the application (should match the app directory name).
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_activity'

    def ready(self):
        """
            Override the ready() method to perform startup tasks.

            This method imports 'signals' module from 'user_activity' app to register
            any signal handlers to ensures signals are connected.
            Note: Do not place import at top-level to avoid import-related side-effects.
        """

        import user_activity.signals
