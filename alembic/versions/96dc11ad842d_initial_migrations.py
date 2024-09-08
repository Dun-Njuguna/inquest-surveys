"""Initial migrations

Revision ID: 96dc11ad842d
Revises: 
Create Date: 2024-09-08 23:41:57.458760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96dc11ad842d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('surveys',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_surveys_id'), 'surveys', ['id'], unique=False)
    op.create_table('forms',
    sa.Column('survey_id', sa.Integer(), nullable=False),
    sa.Column('form_data', sa.JSON(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['surveys.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_forms_id'), 'forms', ['id'], unique=False)
    op.create_table('user_surveys',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('survey_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['surveys.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'survey_id', 'id')
    )
    op.create_index(op.f('ix_user_surveys_id'), 'user_surveys', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_surveys_id'), table_name='user_surveys')
    op.drop_table('user_surveys')
    op.drop_index(op.f('ix_forms_id'), table_name='forms')
    op.drop_table('forms')
    op.drop_index(op.f('ix_surveys_id'), table_name='surveys')
    op.drop_table('surveys')
    # ### end Alembic commands ###
