from sqlflask import db, Puppy


# Create
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read
all_puppies = Puppy.query.all()  # list of puppie objects in table
print(all_puppies)
# getting an object 1 in db
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# searching by filtring
frankie_puppy = Puppy.query.filter_by(name='Joe')
print(frankie_puppy.all())


# Update db
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# delete in db
sec_puppy = Puppy.query.get(2)
db.session.delete(sec_puppy)
db.session.commit()



####
all_puppies = Puppy.query.all()
print(all_puppies)



