"""added vendor contact name

Revision ID: 1d6540fc6279
Revises: 3790aed42558
Create Date: 2013-10-31 01:30:12.489026

"""

# revision identifiers, used by Alembic.
revision = '1d6540fc6279'
down_revision = '3790aed42558'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vendor', sa.Column('contact_name', sa.String(length=120), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vendor', 'contact_name')
    ### end Alembic commands ###
