"""empty message

Revision ID: 50780a4c6441
Revises: 2090450068bc
Create Date: 2021-01-30 14:45:21.663453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50780a4c6441'
down_revision = '2090450068bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('tweet_id', sa.BigInteger(), nullable=False),
    sa.Column('tweet', sa.String(), nullable=True),
    sa.Column('tweet_sentiment', sa.Integer(), nullable=True),
    sa.Column('tweet_name', sa.String(), nullable=True),
    sa.Column('tweet_username', sa.String(), nullable=True),
    sa.Column('tweet_likes', sa.Integer(), nullable=True),
    sa.Column('tweet_datestamp', sa.Date(), nullable=True),
    sa.Column('day1Price', sa.Float(), nullable=True),
    sa.Column('day2Price', sa.Float(), nullable=True),
    sa.Column('day3Price', sa.Float(), nullable=True),
    sa.Column('day4Price', sa.Float(), nullable=True),
    sa.Column('day5Price', sa.Float(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('numOfTweets', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('tweet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweets')
    # ### end Alembic commands ###
