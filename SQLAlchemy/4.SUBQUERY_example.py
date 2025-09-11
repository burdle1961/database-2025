from sqlalchemy import create_engine, Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from sqlalchemy.orm import aliased


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

# 각 제품별 총 판매 수량 계산
subq = session.query(OrderDetail.제품번호,func.sum(OrderDetail.수량).label("총판매수량")).group_by(OrderDetail.제품번호).subquery() 

# 서브쿼리 alias
sub = aliased(subq, name="o")

query = session.query(Product, sub.c.총판매수량).join(sub, Product.제품번호 == sub.c.제품번호).filter(sub.c.총판매수량 >= 5)

results = query.all()

for product, total_qty in results:
    print(f"{product.제품이름} : 총 판매 수량: {total_qty}")


print ("\n\n생성된 QUERY 문 >>>>>> ")
print (str(query.statement))
