from services.routing_service import RoutingService

from clients.auth_client import AuthClient
from clients.payment_client import PaymentClient
from clients.storage_client import StorageClient
from clients.notify_client import NotifyClient


class GatewayService:

    def __init__(self):

        self.routing = RoutingService()

        self.auth = AuthClient()

        self.payment = PaymentClient()

        self.storage = StorageClient()

        self.notify = NotifyClient()

    def forward(
        self,
        service
    ):

        if service == "auth":

            return self.auth.get_status()

        if service == "payment":

            return self.payment.get_status()

        if service == "storage":

            return self.storage.get_status()

        if service == "notify":

            return self.notify.get_status()

        return {

            "error": "Unknown service"

        }
