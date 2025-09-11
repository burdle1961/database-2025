from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy.exc import SQLAlchemyError


# DB 연결 설정 (예: mariadb+pymysql 사용)
DATABASE_URL = "mariadb+mariadbconnector://root:burdle@localhost:3306/sample"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

# 제품 테이블 매핑
class Product(Base):
    __tablename__ = "제품"

    제품번호 = Column(Integer, primary_key=True)
    제품이름 = Column(String(20))
    제품설명 = Column(Text)
    가격 = Column(Integer)
    재고수량 = Column(Integer)

# 테이블 생성 (이미 존재하면 무시)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

# 세션 생성
session = SessionLocal()

# 1. Create (제품 추가)
def create_product(번호, 이름, 설명, 가격, 수량):
    new_product = Product(
        제품번호=번호,
        제품이름=이름,
        제품설명=설명,
        가격=가격,
        재고수량=수량
    )
    try :
        session.add(new_product)
        session.commit()
        print(f"제품 추가 완료: {new_product.제품번호}")
    except SQLAlchemyError as e:
        session.rollback()
        print("제품 추가 실패", e)
    
# 2. Read (제품 조회)
def get_products():
    products = session.query(Product).all()
    # for p in products:
    #     print(p.제품번호, p.제품이름, p.가격, p.재고수량)
    return products

def get_product_by_id(제품번호):
    product = session.query(Product).filter(Product.제품번호 == 제품번호).first()
    return product

# 3. Update (제품 수정)
def update_product(제품번호, 새로운가격=None, 새로운수량=None):
    product = session.query(Product).filter(Product.제품번호 == 제품번호).first()
    if product:
        if 새로운가격 is not None:
            product.가격 = 새로운가격
        if 새로운수량 is not None:
            product.재고수량 = 새로운수량
        session.commit()
        print(f"제품 수정 완료: {제품번호}")
    else:
        print("제품을 찾을 수 없습니다.")

# 4. Delete (제품 삭제)
def delete_product(제품번호):
    product = session.query(Product).filter(Product.제품번호 == 제품번호).first()
    if product:
        session.delete(product)
        session.commit()
        print(f"제품 삭제 완료: {제품번호}")
    else:
        print("제품을 찾을 수 없습니다.")

if __name__ == "__main__":
    # 제품 추가
    # create_product(2001, "노트북", "15인치 고성능 노트북", 1200000, 10)
    # create_product(2002, "마우스", "무선 블루투스 마우스", 25000, 50)

    # 전체 제품 조회
    p = get_products()
    print ("전체 제품 목록 조회")
    for one in p :
        print (one.제품번호, one.제품이름, one.가격)

    # 특정 제품 조회
    p = get_product_by_id(1)
    if p : 
        print("조회 결과:", p.제품이름, p.가격)
    else :
        print ("해당 제품이 없습니다.")

    # 제품 수정
    update_product(1001, 새로운가격=1100000, 새로운수량=8)

    # 제품 삭제
    delete_product(1010)
