class RoutingService:

    def route(
        self,
        service
    ):

        routes = {

            "auth": "/auth",

            "payment": "/payment",

            "storage": "/storage",

            "notify": "/notify"

        }

        return {

            "service": service,

            "route": routes.get(
                service,
                "Unknown Service"
            )

        }
