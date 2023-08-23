from app import app, Skills, db

sample_skills = [
        {"name": "Strength", "level": 1, "description": "Strength represents your physical power."},
        {"name": "Defence", "level": 1, "description": "Defence represents your ability to protect yourself either by fighting or discussing."},
        {"name": "Prayer", "level": 1, "description": "Prayer represents your practice of communicating with a higher power seeking guidance, blessings, or inner peace."},
        {"name": "Construction", "level": 1, "description": "Construction represents the art and science of building structures and infrastructures."},
        {"name": "Heart", "level": 1, "description": "Heart represents your cardiovascular endurance and the efficiency of your circulatory system during physical activities."},
        {"name": "Agility", "level": 1, "description": "Agility represents your ability to move quickly and easily, showcasing physical dexterity or adaptability."},
        {"name": "Farming", "level": 1, "description": "Farming represents the cultivation of plants and rearing of animals to produce food and other products."},
        {"name": "Gaming", "level": 1, "description": "Gaming represents the act of playing games, ranging from video games to board games."},
        {"name": "Knowledge", "level": 1, "description": "Knowledge represents the accumulation of facts, information, and skills acquired through experience or education."},
        {"name": "Cooking", "level": 1, "description": "Cooking represents the art and technique of preparing food by combining and heating ingredients."},
        {"name": "Creativity", "level": 1, "description": "Creativity represents the ability to produce original and imaginative ideas or art."},
        {"name": "Coding", "level": 1, "description": "Coding represents the practice of writing computer programs using programming languages."},
    ]

with app.app_context():
    for skill_data in sample_skills:
        skills = Skills(name=skill_data["name"], level=skill_data["level"], description=skill_data["description"])
        db.session.add(skills)
    db.session.commit()