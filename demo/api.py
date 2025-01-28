
from ninja import Router

router = Router()

@router.get('/')
def test(request):
    return "test"
