##############
### import ###
##############

from flask import Flask, redirect, url_for, render_template, session, g, request, flash, Blueprint, abort
from crewmen import app, login_required, power_required
from .form import AddMemberForm, DeleteMemberForm
from models import *

##############
### config ###
##############

member_blueprint = Blueprint(
    'member', __name__,
    template_folder='templates'
)

@member_blueprint.route('/member_profile')
@login_required
def member_profile():
    member = User.query.filter_by(username=session['login_username']).first().member
    return render_template('member_profile.html', member=member)

@member_blueprint.route('/allmember_profile')
@login_required
@power_required
def allmember_profile():
    all_members = Member.query.all()

    return render_template('allmember_profile.html', all_members=all_members)

@member_blueprint.route('/add_member', methods=['GET', 'POST'])
@login_required
@power_required
def add_member():
    form = AddMemberForm()

    if form.validate_on_submit():
        newMember = Member()
        newMember.name = form.name.data
        newMember.sex = form.sex.data
        newMember.enter_club = form.enter_club.data
        newMember.ID = form.ID.data
        db.session.add(newMember)
        db.session.commit()
        flash("You have added a new user!")
        return render_template('add_member.html', form=form)

    #if request.method == 'GET':
    return render_template('add_member.html', form=form)

@member_blueprint.route('/delete_member', methods=['GET', 'POST'])
@login_required
@power_required
def delete_member():
    form = DeleteMemberForm()

    if form.validate_on_submit():
        ID = form.ID.data

        flash('You have deleted member with ID: ' + str(ID) + ' from the system')
        return render_template('delete_member.html', form=form)

    return render_template('delete_member.html', form=form)
