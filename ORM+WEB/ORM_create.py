from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# DB 연결 설정 (예: mariadb+pymysql 사용)
DATABASE_URL = "mariadb+mariadbconnector://root:burdle@localhost:3306/sample"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

# 제품 테이블 매핑
class Product(Base):
    __tablename__ = "Products"

    ProductID = Column(Integer, primary_key=True)
    ProductName = Column(String(20))
    Description = Column(Text)
    Price = Column(Integer)
    Quantity = Column(Integer)

# 테이블 생성 (이미 존재하면 무시)
Base.metadata.create_all(engine)
