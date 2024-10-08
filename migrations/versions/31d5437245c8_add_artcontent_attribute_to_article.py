"""Add artContent attribute to Article

Revision ID: 31d5437245c8
Revises: 8c7ffc987749
Create Date: 2024-08-05 10:40:58.939963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31d5437245c8'
down_revision = '8c7ffc987749'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('artContent', sa.Text(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('artContent')

    # ### end Alembic commands ###
