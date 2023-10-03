from basic import app, db, Puppy

# 모델 클래스를 테이블로 생성
with app.app_context():
    db.create_all()
# 데이터베이스 작업 수행
with app.app_context():
    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie', 4)

    # None
    print(sam.id)
    print(frank.id)

    db.session.add_all([sam, frank])

    db.session.commit()

    print(sam.id)
    print(frank.id)
