from sqlflask import db, Puppy


# creates all tables
db.create_all()


sam = Puppy('Sammy', 3)
joe = Puppy('Joe', 2)

# should return none but wait for the lower lines!
print(sam.id)


# adding to db (can be add_all([sam, joe])
db.session.add(sam)
db.session.add(joe)

db.session.commit()

print(sam.id)