from fastapi import FastAPI
import app.utils.base as utils
from app.domains.location.locationController import router as locations_router
from app.domains.category.categoryController import router as categories_router
from app.domains.review.reviewController import router as reviews_router
from app.domains.recommender.recommenderController import router as recomender_router

app = FastAPI()

@app.get("/")
def read_version():
    return {"version": utils.get_version()}

app.include_router(locations_router, prefix="/api/v1/location")
app.include_router(categories_router, prefix="/api/v1/category")
app.include_router(reviews_router, prefix="/api/v1/review")
app.include_router(recomender_router, prefix="/api/v1/recommender")