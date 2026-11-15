full_dot = '●'
empty_dot = '○'


def create_character(character, strength, intelligence, charisma):
    stats = [strength, intelligence, charisma]

    # Name checks
    if not isinstance(character, str):
        return "The character name should be a string"
    if character == "":
        return "The character should have a name"
    if len(character) > 10:
        return "The character name is too long"
    if " " in character:
        return "The character name should not contain spaces"

    # Stats type and range check
    for stat in stats:
        if not isinstance(stat, int):
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat > 30:
            return "All stats should be no more than 30"

    # Total points check
    if sum(stats) > 27:
        return "The character should start with 7 points"

    # Build character display
    result = character
    result += "\nSTR " + full_dot * strength + empty_dot * (10 - strength)
    result += "\nINT " + full_dot * intelligence + empty_dot * (10 - intelligence)
    result += "\nCHA " + full_dot * charisma + empty_dot * (10 - charisma)

    return result


print(create_character('Tay', 8, 9, 10))
