from sqlalchemy import create_engine, Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func 


# DB 연결 설정 (예: mariadb+pymysql 사용)
DATABASE_URL = "mariadb+mariadbconnector://root:burdle@localhost:3306/sample"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

class Product(Base):
    __tablename__ = "제품"

    제품번호 = Column(Integer, primary_key=True)
    제품이름 = Column(String(20))
    제품설명 = Column(Text)
    가격 = Column(Integer)
    재고수량 = Column(Integer)

class OrderDetail(Base):
    __tablename__ = "주문상세"

    주문상세번호 = Column(Integer, primary_key=True)
    주문번호 = Column(Integer)  # 실제 Order 테이블이 있다면 ForeignKey 지정 가능
    제품번호 = Column(Integer, ForeignKey("제품.제품번호"))
    수량 = Column(Integer)
    판매가격 = Column(Integer)

    
SessionLocal = sessionmaker(bind=engine)

# 세션 생성
session = SessionLocal()

# 조회할 고객번호
target_customer_id = 1001

# INNER JOIN 쿼리
results = session.query(Product.제품번호, Product.제품이름, OrderDetail.주문번호).join(OrderDetail, Product.제품번호 == OrderDetail.제품번호).all()

print ("query().join() >>>>>>>>>")

for 번호, 이름, 주문 in results :
    print (번호, 이름, 주문)


# OUTER JOIN 쿼리
results = session.query(Product.제품번호, Product.제품이름, OrderDetail.주문번호).outerjoin(OrderDetail, Product.제품번호 == OrderDetail.제품번호).all()

print ("query().outerjoin() >>>>>>>>>")

for 번호, 이름, 주문 in results :
    print (번호, 이름, 주문)