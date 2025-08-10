from app.db.database import engine, Base

try:
    # Try connecting to the database
    with engine.connect() as connection:
        print("✅ Database connection successful!")
except Exception as e:
    print("❌ Database connection failed!")
    print(e)