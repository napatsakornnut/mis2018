"""added learning outcome and assessment assoc table

Revision ID: c981a763d55d
Revises: 54af149c2ba6
Create Date: 2023-08-30 13:41:52.138651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c981a763d55d'
down_revision = '54af149c2ba6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eduqa_learning_activity_assessment_assoc',
    sa.Column('learning_activity_id', sa.Integer(), nullable=True),
    sa.Column('learning_assessment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['learning_activity_id'], ['eduqa_course_learning_activities.id'], ),
    sa.ForeignKeyConstraint(['learning_assessment_id'], ['eduqa_course_learning_activity_assessments.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('eduqa_learning_activity_assessment_assoc')
    # ### end Alembic commands ###
