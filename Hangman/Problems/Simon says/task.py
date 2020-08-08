def what_to_do(instructions):

    no_simon = "Simon says"
    if instructions.startswith(no_simon):
        instructions = instructions.lstrip(no_simon)
        return f'I {instructions}'
    elif instructions.endswith(no_simon):
        instructions = instructions.rstrip(no_simon)
        return f'I {instructions}'
    else:
        return "I won't do it!"
