from services.routing_service import RoutingService


class GatewayService:

    def __init__(self):

        self.routing = RoutingService()

    def forward(
        self,
        service
    ):

        return self.routing.route(
            service
        )
