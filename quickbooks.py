from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
import json
from intuitlib.client import AuthClient


code='AB11649635281KQg3YJqAKn0IZctS6S7n9a7SuDIGTG1Cy9W3X',
state='Ux61zBS2hY9v6oX0rBjkAt3QoYXFTD',
realmId='4620816365217554820',
scopes=Scopes.ACCOUNTING,
Environment='production',
client_id='ABcX3e4BRl8UelvRtyCYNVWsGPfA4m8WpmV1UfBm15Wx4MPdfm',
client_secret='JjemBe2k6KhWwQU1Ndr94BiILmsBU8Ugr4cnnC8C',
redirect_uri='http://localhost:8000/sampleAppOAuth2/'



def auth_client(AuthClient(
    client_id=client_id,
    client_secret=client_secret,
    environment='production',
    redirect_uri=redirect_uri(request),
    state=state,
    code=code,
    scopes=scopes,
    realmId=realmId
)
                    
auth_client.get_bearer_token(auth_code, realm_id=realm_id)

