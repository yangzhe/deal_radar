from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    Boolean,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Brand(Base):
    __tablename__ = "brands"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    website: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )


class Store(Base):
    __tablename__ = "stores"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    brand_id: Mapped[int] = mapped_column(
        ForeignKey("brands.id"),
        nullable=False
    )

    country: Mapped[str] = mapped_column(
        String(2),
        nullable=False
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    website: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    store_id: Mapped[int] = mapped_column(
        ForeignKey("stores.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    product_url: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    image_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    original_price: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    current_price: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    color: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    size: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    in_stock: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )


class PriceHistory(Base):
    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False
    )

    recorded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )