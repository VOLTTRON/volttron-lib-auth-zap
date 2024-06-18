from volttron.types.auth import Authenticator, CredentialsStore, Credentials
from volttron.server.server_options import ServerOptions
from volttron.decorators import service
from volttron.types.bases import Service

@service
class ZAPAuthenticator(Authenticator):
    def __init__(self, *, options: ServerOptions, credentials_store: CredentialsStore):
        self._credentials_store = credentials_store
        self._options = options

    def authenticate(self, *, credentials: Credentials) -> bool:
        if self._options.auth_enabled:
            if not self._credentials_store.has_identity(credentials.identity):
                # Might be other stuff here to work with.
                return False
        #creds = self._credentials_store.retrieve_credentials(credentials.identity)
        return True
