from logging import Manager
from aries_cloudagent.core.profile import Profile
from aries_cloudagent.protocols.issue_credential.v1_0 import manager
from aries_cloudagent.protocols.issue_credential.v1_0.messages.credential_issue import CredentialIssueSchema
from aries_cloudagent.protocols.issue_credential.v1_0.messages.inner.credential_preview import CredentialPreview
import asyncio

import asyncio


# async def speak_async():
#     while True:
#         print("Hello I'm Abhishek, writer on GFG")


# loop = asyncio.get_event_loop()
# loop.run_until_complete(speak_async())
# loop.close()


class Manager(manager.CredentialManager):

    # def __init__(self, profile: Profile):
    #     self._profile = profile

    # @property
    # def profile(self) -> Profile:
    #     return self._profile

    async def prepare(self):
        proposal = {
            "comment": "Hello Regov. Kindly review my proposal for digital certification",
            "connection_id": "a89a273c-3001-4bd8-be7d-63361b79b5fd",
            "credential_preview": {
                "@type": "issue-credential/2.0/credential-preview",
                "attributes": [
                    {
                        "mime-type": "plain/text",
                        "name": "name",
                        "value": "Apple Inc."
                    },
                    {
                        "mime-type": "plain/text",
                        "name": "phone",
                        "value": "018XXX8586"
                    },
                    {
                        "mime-type": "plain/text",
                        "name": "ID",
                        "value": "G8XXXXXX8P"
                    }
                ]
            },
            "filter": {
                "indy": {}
            }
        }
        await manager.CredentialManager.prepare_send(self,
                                                     connection_id="116d60f2-7c6d-4e30-a4ab-53a6cf7d2a0c", credential_proposal=proposal)


a = Manager(Profile)
asyncio.run(a.prepare())
# speak_async()
# a.prepare()
