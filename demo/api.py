from ninja import Router

router = Router()


@router.get("/")
def test(request):
    return "test"


@router.get("/test")
def change(request):
    return "test"
