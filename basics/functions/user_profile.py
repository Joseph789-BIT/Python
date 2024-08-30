def build_profile(first, last, **user_info):
    """Build a dictionary containing everything"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('cid', 'kelvin',
                             location='london',
                             field='physics')
print(user_profile)