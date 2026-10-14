from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Orders Service")


# ---------- Data shapes ----------


class OrderCreate(BaseModel):
    """What a customer sends when placing an order."""

    product: str = Field(min_length=1)
    quantity: int = Field(gt=0)


class Order(BaseModel):
    """What an order looks like once it's stored."""

    id: int
    product: str
    quantity: int
    status: str


# Temporary storage. In step 1.4 this moves into PostgreSQL.
ORDERS: list[Order] = [
    Order(id=1, product="keyboard", quantity=2, status="paid"),
    Order(id=2, product="mouse", quantity=1, status="pending"),
]


# ---------- Endpoints ----------


@app.get("/health")
def health() -> dict[str, str]:
    """Tells monitoring tools the service is alive."""
    return {"status": "ok"}


@app.get("/orders")
def list_orders() -> list[Order]:
    """Returns all orders."""
    return ORDERS


@app.get("/orders/{order_id}")
def get_order(order_id: int) -> Order:
    """Returns one order by its ID, or 404 if it doesn't exist."""
    for order in ORDERS:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


@app.post("/orders", status_code=201)
def create_order(order_in: OrderCreate) -> Order:
    """Creates a new order with status 'pending'."""
    new_id = max((o.id for o in ORDERS), default=0) + 1
    order = Order(
        id=new_id,
        product=order_in.product,
        quantity=order_in.quantity,
        status="pending",
    )
    ORDERS.append(order)
    return order
