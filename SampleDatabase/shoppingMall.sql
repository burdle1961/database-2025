DROP database if exists Sample;
create database sample;
use sample;

-- 제품 테이블 (products)
DROP TABLE IF EXISTS 제품;
CREATE TABLE 제품 (
    제품번호 INT PRIMARY KEY,
    제품이름 VARCHAR(20),
    제품설명 TEXT,
    가격 INT,
    재고수량 INT
);


-- 사무실 테이블 (부서)
DROP TABLE IF EXISTS 부서;
CREATE TABLE 부서 (
    부서코드 INT PRIMARY KEY,
    부서명 VARCHAR(20),
    도시 VARCHAR(10),
    우편번호 VARCHAR(20),
    국가 VARCHAR(50),
    안내번호 VARCHAR(20)
);

-- 직원 테이블 (employees)
DROP TABLE IF EXISTS 직원;
CREATE TABLE 직원 (
    직원번호 INT PRIMARY KEY,
    이름 VARCHAR(20),
    직책 VARCHAR(10),
    이메일 VARCHAR(20),
    전화번호 VARCHAR(10),
    관리자 INT,  -- NULL 가능하도록
    부서코드 INT,
    FOREIGN KEY (부서코드) REFERENCES 부서(부서코드),
    FOREIGN KEY (관리자) REFERENCES 직원(직원번호)  -- 자기 자신을 참조
);


-- 고객 테이블 (customers)
DROP TABLE IF EXISTS 고객;
CREATE TABLE 고객 (
    고객번호 INT PRIMARY KEY,
    고객명 VARCHAR(20),
    이메일 VARCHAR(30),
    전화번호 VARCHAR(20),
    주소 VARCHAR(30),
    도시 VARCHAR(20),
    우편번호 VARCHAR(20),
    국가 VARCHAR(50),
    담당영업 INT,
    FOREIGN KEY (담당영업) REFERENCES 직원(직원번호)
);


-- 주문 테이블 (orders)
DROP TABLE IF EXISTS 주문;
CREATE TABLE 주문 (
    주문번호 INT PRIMARY KEY,
    고객번호 INT,
    주문날짜 DATE,
    배송날짜 DATE,
    상태 VARCHAR(10),
    FOREIGN KEY (고객번호) REFERENCES 고객(고객번호)
);

-- 주문 상세 테이블 (orderdetails)
DROP TABLE IF EXISTS 주문상세;
CREATE TABLE 주문상세 (
    주문상세번호 INT PRIMARY KEY,
    주문번호 INT,
    제품번호 INT,
    수량 INT,
    판매가격 INT,
    FOREIGN KEY (주문번호) REFERENCES 주문(주문번호)
);

-- 결제 테이블 (payments)
DROP TABLE IF EXISTS 결제;
CREATE TABLE 결제 (
    결제번호 INT PRIMARY KEY,
    주문번호 INT,
    결제날짜 DATE,
    결제금액 INT,
    FOREIGN KEY (주문번호) REFERENCES 주문 (주문번호)
);
