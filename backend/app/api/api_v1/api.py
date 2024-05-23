from fastapi import APIRouter

from .endpoints.auth import auth_router
from .endpoints.student_admission import admission_router
# from .endpoints.seeder import seeder_router

router = APIRouter()
router.include_router(auth_router, prefix="", tags=["auth"])
router.include_router(admission_router, prefix="", tags=["student_admission"])

# router.include_router(seeder_router, prefix="/seed", tags=["seeder"])