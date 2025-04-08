from pymongo import MongoClient

def initialize_database():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")

    # Create or switch to the octofit_db database
    db = client["octofit_db"]

    # Create collections
    db.create_collection("users")
    db.create_collection("teams")
    db.create_collection("activity")
    db.create_collection("leaderboard")
    db.create_collection("workouts")

    # Ensure unique index on the email field in the users collection
    db["users"].create_index("email", unique=True)

    print("Database and collections initialized successfully.")

def list_collections():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["octofit_db"]
    collections = db.list_collection_names()
    print("Collections in octofit_db:", collections)

if __name__ == "__main__":
    initialize_database()
    list_collections()
