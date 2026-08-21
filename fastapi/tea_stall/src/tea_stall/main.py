from fastapi import FastAPI, HTTPException
from .data import tea_menu
from .models import MenuResponse, MenuItem

app = FastAPI(
    title="Tea Stall",
    description="Read only menu API for Kiosk displays and mobile apps",
    version="1.0.0",
)


@app.get("/", tags=["Root"])
def root():
    return {"message": "Hello World"}


@app.get(
    "/menu",
    response_model=MenuResponse,
    description="Get all menu items or filter by category",
    tags=["Menu"],
)
def get_items(category: str | None = None):
    if category:
        filtered_menu = [menu for menu in tea_menu if menu["category"] == category]

        if not filtered_menu:
            raise HTTPException(status_code=404, detail="Category not found")

        return MenuResponse(
            status="success",
            count=len(filtered_menu),
            items=[MenuItem(**menu) for menu in filtered_menu],
        )

    return MenuResponse(
        status="success",
        count=len(tea_menu),
        items=[MenuItem(**menu) for menu in tea_menu],
    )


@app.get(
    "/menu/{menu_id}",
    response_model=MenuResponse,
    description="Get a specific menu item by ID",
    tags=["Menu"],
)
def get_item(menu_id: int):
    tea = next((menu for menu in tea_menu if menu["id"] == menu_id), None)

    if not tea:
        raise HTTPException(status_code=404, detail="Tea not found")

    return MenuResponse(
        status="success",
        count=1,
        items=[MenuItem(**tea)],
    )
