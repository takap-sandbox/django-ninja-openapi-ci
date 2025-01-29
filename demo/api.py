from ninja import Router

router = Router()


@router.get("/")
def test(request):
    return "test"


@router.get("/update")
def update(request):
    return "update"
