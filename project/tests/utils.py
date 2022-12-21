from faker import Faker

fake = Faker()


def generate_user_data():
    simple_profile = fake.simple_profile()
    name = fake.pystr(min_chars=3, max_chars=10)
    surname = fake.pystr(min_chars=3, max_chars=10)
    username = fake.pystr(min_chars=6, max_chars=16)
    email = simple_profile['mail']
    password = fake.password()
    middle_name = fake.pystr(min_chars=None, max_chars=10)
    access = 1
    active = 1
    start_active_time = None
    return name, surname, username, email, password, middle_name, access, active, start_active_time
