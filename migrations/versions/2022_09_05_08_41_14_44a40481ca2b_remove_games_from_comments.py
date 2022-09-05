"""remove games from comments

Revision ID: 44a40481ca2b
Revises: c217c608d86c
Create Date: 2022-09-05 08:41:14.982682+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44a40481ca2b'
down_revision = 'c217c608d86c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'slots_result')
    op.drop_column('comments', 'blackjack_result')
    op.drop_column('comments', 'wordle_result')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('wordle_result', sa.VARCHAR(length=115), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('blackjack_result', sa.VARCHAR(length=860), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('slots_result', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
