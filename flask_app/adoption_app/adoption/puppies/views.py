from flask import Blueprint, render_template, redirect, url_for
from adoption import db
from adoption.models import Puppy
from adoption.puppies.forms import AddForm, DelForm


puppies_blueprints = Blueprint('puppies',
                              __name__,
                              template_folder='templates/puppies')


@puppies_blueprints.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('puppies.list_pup'))
    return render_template('add.html', form=form)


@puppies_blueprints.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@puppies_blueprints.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
    return render_template('delete.html', form=form)