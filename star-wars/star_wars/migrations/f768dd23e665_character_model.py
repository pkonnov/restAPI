"""character model

Revision ID: f768dd23e665
Revises: e2e5fdaa9088
Create Date: 2017-12-05 05:18:38.462336

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f768dd23e665'
down_revision = 'e2e5fdaa9088'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('planet', sa.Unicode(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('character', 'planet')
    # ### end Alembic commands ###