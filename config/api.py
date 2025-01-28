from demo.api import router
from ninja import NinjaAPI


api = NinjaAPI()
api.add_router("", router)
