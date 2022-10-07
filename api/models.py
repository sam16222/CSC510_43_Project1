from datetime import datetime
from itertools import count
import uuid
from typing import Optional, List
from pydantic import BaseModel, Field

class Recipe(BaseModel):
    """Base class for Recipe"""
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    cookTime: Optional[str] = None
    prepTime: Optional[str] = None
    totalTime: Optional[str] = None
    description: Optional[str] = None
    images: Optional[list] = None
    category: str
    tags: List[str]
    ingredientQuantities: list
    ingredients: List[str]
    rating: Optional[str] = None
    calories: Optional[str] = None
    fat: Optional[str] = None
    saturatedFat: Optional[str] = None
    cholesterol: Optional[str] = None
    sodium: Optional[str] = None
    carbs: Optional[str] = None
    fiber: Optional[str] = None
    sugar: Optional[str] = None
    protein: Optional[str] = None
    servings: Optional[str] = None
    instructions: List[str]

    class Config:
        schema_extra = {
            
            "example": {
                "id": "abcd-efgh-jklm-nopq-rstuv",
                "name": "Low-Fat Berry Blue Frozen Dessert",
                "cookTime": "24H",
                "prepTime": "45M",
                "totalTime": "24H45M",
                "description": "Make and share this Low-Fat Berry Blue Frozen Dessert recipe from Food.com.",
                "images": [
                    "https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/38/YUeirxMLQaeE1h3v3qnM_229%20berry%20blue%20frzn%20dess.jpg",
                    "https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/38/AFPDDHATWzQ0b1CDpDAT_255%20berry%20blue%20frzn%20dess.jpg",
                    "https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/38/UYgf9nwMT2SGGJCuzILO_228%20berry%20blue%20frzn%20dess.jpg",
                    "https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/38/PeBMJN2TGSaYks2759BA_20140722_202142.jpg",
                    "https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/38/picuaETeN.jpg",
                    "https://img.sndimg.com/food/image/upload/w_555,h_416,c_fit,fl_progressive,q_95/v1/img/recipes/38/pictzvxW5.jpg"
                ],
                "category": "Frozen Desserts",
                "tags": [
                    "Dessert",
                    "Low Protein",
                    "Low Cholesterol",
                    "Healthy",
                    "Free Of...",
                    "Summer",
                    "Weeknight",
                    "Freezer",
                    "Easy"
                ],
                "ingredientQuantities": [
                    "4",
                    "1/4",
                    "1",
                    "1"
                ],
                "ingredients": [
                    "blueberries",
                    "granulated sugar",
                    "vanilla yogurt",
                    "lemon juice"
                ],
                "rating": "4.5",
                "calories": "170.9",
                "fat": "2.5",
                "saturatedFat": "1.3",
                "cholesterol": "8",
                "sodium": "29.8",
                "carbs": "37.1",
                "fiber": "3.6",
                "sugar": "30.2",
                "protein": "3.2",
                "servings": "4",
                "instructions": [
                    "Toss 2 cups berries with sugar.",
                    "Let stand for 45 minutes, stirring occasionally.",
                    "Transfer berry-sugar mixture to food processor.",
                    "Add yogurt and process until smooth.",
                    "Strain through fine sieve. Pour into baking pan (or transfer to ice cream maker and process according to manufacturers' directions). Freeze uncovered until edges are solid but centre is soft.  Transfer to processor and blend until smooth again.",
                    "Return to pan and freeze until edges are solid.",
                    "Transfer to processor and blend until smooth again.",
                    "Fold in remaining 2 cups of blueberries.",
                    "Pour into plastic mold and freeze overnight. Let soften slightly to serve."
                ]
            }
        }


class RecipeListRequest(BaseModel):
    ingredients: List[str]
    page: int

class RecipeListResponse(BaseModel):
    recipes: List[Recipe] = Field(..., description="List of recipe ids")
    page: int = Field(..., description="Page number")
    count: int = Field(..., description="Number of total recipes based on filters")