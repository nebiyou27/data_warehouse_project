from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:neba@localhost:5432/telegram_data")
with engine.connect() as connection:
    print("✅ Connected to PostgreSQL successfully!")