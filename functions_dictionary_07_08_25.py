"""**user-profile es el empaquetado de variables arbitrarias que se pasaran dspues de las que estan definidas"""
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton', # clave = valor
                             field='physics')
print(user_profile)