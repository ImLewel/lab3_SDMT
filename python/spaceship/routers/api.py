from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrixmult')
def matrixmult() -> dict:
    first = np.random.rand(10, 10)
    second = np.random.rand(10, 10)
    return {
        "first": first.tolist(),
        "second": second.tolist(),
        "result": np.matmul(first, second).tolist()
    }