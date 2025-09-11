from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# DB 연결 설정 (예: mariadb+pymysql 사용)
DATABASE_URL = "mariadb+mariadbconnector://root:burdle@localhost:3306/sample"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

# ----------------------------
# 고객 테이블
# ----------------------------
class Customer(Base):
    __tablename__ = "고객"
    
    고객번호 = Column(Integer, primary_key=True, autoincrement=True)
    고객명 = Column(String(20))
    이메일 = Column(String(30))
    전화번호 = Column(String(20))
    주소 = Column(String(30))
    도시 = Column(String(20))
    우편번호 = Column(String(20))
    국가 = Column(String(50))
    담당영업 = Column(Integer)
    
    # ORM 관계: 고객 -> 주문 (1:N)
    orders = relationship("Order", back_populates="customer")     # 양쪽 모두 지정해야 함.
    # orders = relationship("Order")                # 필요한 쪽에서만 지정 가능

# ----------------------------
# 주문 테이블
# ----------------------------
class Order(Base):
    __tablename__ = "주문"
    
    주문번호 = Column(Integer, primary_key=True, autoincrement=True)
    고객번호 = Column(Integer, ForeignKey("고객.고객번호"))  # 외래키
    주문날짜 = Column(Date)
    배송날짜 = Column(Date)
    상태 = Column(String(10))
    
    # ORM 관계: 주문 -> 고객 (N:1)
    customer = relationship("Customer", back_populates="orders")
    # customers = relationship("Customer")
    # customer = relationship("Customer", backref="orders")     # 자동으로 양쪽이 지정됨.


SessionLocal = sessionmaker(bind=engine)

# 세션 생성
session = SessionLocal()

# 조회할 고객번호
target_customer_id = 1001

# INNER JOIN 쿼리
results = session.query(Order, Customer).join(Customer, Order.고객번호 == Customer.고객번호).filter(Customer.고객번호 == target_customer_id).all()

print ("query().join() >>>>>>>>>")
for order, customer in results:
    print(f"주문번호: {order.주문번호}, 주문날짜: {order.주문날짜}, 배송날짜: {order.배송날짜}, 상태: {order.상태}, 고객명: {customer.고객명}")

# relationship()을 이용하여 join 없이 처리. Order 테이블이 Customer Table의 속성 처럼 처리됨.
print ("customer.orders >>>>>>>>")
customer = session.get(Customer, target_customer_id)
if customer:
    for order in customer.orders:
        print(f"주문번호: {order.주문번호}, 주문날짜: {order.주문날짜}, 배송날짜: {order.배송날짜}, 상태: {order.상태}, 고객명: {customer.고객명}")

print ("orders.customer >>>>>>>>")
target_order_id = 2001
order = session.get(Order, target_order_id)

if order :
    print(f"주문번호: {order.주문번호}, 주문날짜: {order.주문날짜}, 배송날짜: {order.배송날짜}, 상태: {order.상태}, 고객명: {order.customer.고객명}")