# creates entreis into the tables

from models_sql import Puppy, Toy, Owner, db


rufus = Puppy('Rufus')
fido = Puppy('Fido')

#addin items to db
# db.session.add_all([rufus, fido])
# db.session.commit()

#checking
print(Puppy.query.all())

#geting dog from DB
dog = Puppy.query.filter_by(name='Rufus').first()
print(dog)
#creating owner wiht id of rufus
jose = Owner('Jose', dog.id)
#creating toy for the dog
lamp = Toy('Lamp', dog.id)
ball = Toy('ball', dog.id)

# db.session.add_all([jose, lamp, ball])
# db.session.commit()


#getting dog agian
dog = Puppy.query.filter_by(name="Rufus")
print(dog)
print(dog.Toy)