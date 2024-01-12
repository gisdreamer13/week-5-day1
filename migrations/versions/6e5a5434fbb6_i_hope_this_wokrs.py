"""i hope this wokrs

Revision ID: 6e5a5434fbb6
Revises: 3109af85a4c4
Create Date: 2024-01-10 15:15:43.248211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e5a5434fbb6'
down_revision = '3109af85a4c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('specs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hp', sa.String(), nullable=False),
    sa.Column('timestamp', sa.String(), nullable=True),
    sa.Column('specs_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['specs_id'], ['specs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('specs')
    # ### end Alembic commands ###
