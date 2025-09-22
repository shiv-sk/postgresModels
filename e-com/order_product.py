from sqlmodel import SQLModel , Field

class OrderProduct(SQLModel , table = True):
    order_id:int = Field(foreign_key="order.id" , primary_key=True)
    product_id:int = Field(foreign_key="product.id" , primary_key=True)
    price: float = Field(nullable=False)