"""
Create City & Company models

Revision ID: 9a2b51bf00df
Create Date: 2022-08-21 15:10:33.476916

"""
import sqlalchemy as sa
from alembic import op


revision = "9a2b51bf00df"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "city",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=60), nullable=False),
        sa.Column("abbreviation", sa.String(length=12), nullable=False),
        sa.Column("min_lat", sa.Numeric(precision=8, scale=6), nullable=False),
        sa.Column("min_lon", sa.Numeric(precision=9, scale=6), nullable=False),
        sa.Column("max_lat", sa.Numeric(precision=8, scale=6), nullable=False),
        sa.Column("max_lon", sa.Numeric(precision=9, scale=6), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "company",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=60), nullable=False),
        sa.Column("abbreviation", sa.String(length=12), nullable=False),
        sa.Column("lat", sa.Numeric(precision=8, scale=6), nullable=False),
        sa.Column("lon", sa.Numeric(precision=9, scale=6), nullable=False),
        sa.Column("city_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["city_id"],
            ["city.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("company")
    op.drop_table("city")
    # ### end Alembic commands ###