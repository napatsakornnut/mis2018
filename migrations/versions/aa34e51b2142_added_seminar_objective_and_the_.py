"""added seminar objective and the association table

Revision ID: aa34e51b2142
Revises: fc3ce95b4420
Create Date: 2022-09-15 09:15:49.462275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa34e51b2142'
down_revision = 'fc3ce95b4420'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('staff_seminar_objectives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objective', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff_seminar_objective_assoc',
    sa.Column('seminar_attend_id', sa.Integer(), nullable=True),
    sa.Column('seminar_objective_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seminar_attend_id'], ['staff_seminar_attends.id'], ),
    sa.ForeignKeyConstraint(['seminar_objective_id'], ['staff_seminar_objectives.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('staff_seminar_objective_assoc')
    op.drop_table('staff_seminar_objectives')
    # ### end Alembic commands ###
