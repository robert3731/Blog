"""Add Post table

Revision ID: cff0d9127f82
Revises: 
Create Date: 2021-02-01 14:57:15.141370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cff0d9127f82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entry')
    # ### end Alembic commands ###
