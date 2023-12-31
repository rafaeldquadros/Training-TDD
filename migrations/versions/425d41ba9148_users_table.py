"""users table

Revision ID: 425d41ba9148
Revises: 454a84153241
Create Date: 2023-07-04 13:56:40.119121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '425d41ba9148'
down_revision = '454a84153241'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
