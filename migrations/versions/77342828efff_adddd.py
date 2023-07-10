"""adddd

Revision ID: 77342828efff
Revises: e95477699154
Create Date: 2023-07-04 23:44:55.479898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77342828efff'
down_revision = 'e95477699154'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token_expires', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'token_expires')
    # ### end Alembic commands ###