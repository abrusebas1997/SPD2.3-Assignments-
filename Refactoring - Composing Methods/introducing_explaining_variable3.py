# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    cooking_state = time * temperature * pressure * COOKED_CONSTANT
    if desired_state in ['well-done', 'medium'] and (cooking_state >= WELL_DONE or cooking_state >= MEDIUM):
        return True
    return False