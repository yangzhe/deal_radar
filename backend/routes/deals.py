from decimal import Decimal

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Product, Store, Brand


router = APIRouter(
    prefix="/api/deals",
    tags=["deals"],
)


@router.get("")
def get_deals(db: Session = Depends(get_db)):
    products = (
        db.query(Product, Store, Brand)
        .join(Store, Product.store_id == Store.id)
        .join(Brand, Store.brand_id == Brand.id)
        .all()
    )

    deals = []

    for product, store, brand in products:
        discount = None

        if (
            product.original_price is not None
            and product.original_price > 0
            and product.current_price is not None
        ):
            discount = (
                (product.original_price - product.current_price)
                / product.original_price
                * Decimal("100")
            )

        deals.append(
            {
                "id": product.id,
                "brand": brand.name,
                "name": product.name,
                "image_url": product.image_url,
                "original_price": product.original_price,
                "current_price": product.current_price,
                "currency": product.currency,
                "discount": (
                    round(float(discount), 2)
                    if discount is not None
                    else None
                ),
                "product_url": product.product_url,
            }
        )

    return deals