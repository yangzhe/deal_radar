from decimal import Decimal

from database import SessionLocal
from models import (
    Brand,
    Store,
    Product,
    ProductVariant,
    PriceHistory,
)


def seed_data():
    db = SessionLocal()

    try:
        # --------------------------------------------------
        # 1. Brand
        # --------------------------------------------------
        lululemon = Brand(
            name="Lululemon",
            slug="lululemon",
            website="https://shop.lululemon.com/",
        )

        db.add(lululemon)
        db.flush()

        # --------------------------------------------------
        # 2. Store
        # --------------------------------------------------
        lululemon_ca = Store(
            brand_id=lululemon.id,
            country="CA",
            currency="CAD",
            name="Lululemon Canada",
            website="https://shop.lululemon.com/",
        )

        db.add(lululemon_ca)
        db.flush()

        # --------------------------------------------------
        # 3. Product
        # --------------------------------------------------
        product = Product(
            store_id=lululemon_ca.id,
            name="Align High-Rise Pant",
            description="Test product for Deal Radar MVP",
            product_url="https://shop.lululemon.com/",
            image_url="https://placehold.co/600x600",
            original_price=Decimal("128.00"),
            current_price=Decimal("89.00"),
            currency="CAD",
        )

        db.add(product)
        db.flush()

        # --------------------------------------------------
        # 4. Product Variants
        # --------------------------------------------------
        variants = [
            ProductVariant(
                product_id=product.id,
                color="Black",
                size="4",
                in_stock=True,
            ),
            ProductVariant(
                product_id=product.id,
                color="Black",
                size="6",
                in_stock=True,
            ),
            ProductVariant(
                product_id=product.id,
                color="Black",
                size="8",
                in_stock=False,
            ),
            ProductVariant(
                product_id=product.id,
                color="Navy",
                size="6",
                in_stock=True,
            ),
        ]

        db.add_all(variants)

        # --------------------------------------------------
        # 5. Price History
        # --------------------------------------------------
        price_history = [
            PriceHistory(
                product_id=product.id,
                price=Decimal("128.00"),
                currency="CAD",
            ),
            PriceHistory(
                product_id=product.id,
                price=Decimal("99.00"),
                currency="CAD",
            ),
            PriceHistory(
                product_id=product.id,
                price=Decimal("89.00"),
                currency="CAD",
            ),
            PriceHistory(
                product_id=product.id,
                price=Decimal("79.00"),
                currency="CAD",
            ),
        ]

        db.add_all(price_history)

        # --------------------------------------------------
        # Save everything
        # --------------------------------------------------
        db.commit()

        print("Seed data inserted successfully!")
        print(f"Brand ID: {lululemon.id}")
        print(f"Store ID: {lululemon_ca.id}")
        print(f"Product ID: {product.id}")

    except Exception as e:
        db.rollback()
        print("Failed to insert seed data!")
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()