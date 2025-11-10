from app.presentation.composers.database.database_composer import DatabaseComposer


def create_database():
    database = DatabaseComposer.compose()
    database.create_database()