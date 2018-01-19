from .base import db, BaseMixin

__all__= ['Character']


class Character(BaseMixin, db.Model):

	__tablename__ = 'character'
	__tableplanet__ = 'character'

	name = db.Column(db.Unicode(255), nullable=False)
	planet = db.Column(db.Unicode(20))