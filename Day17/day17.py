import itertools

x_min = 248
x_max = 285
y_min = -85
y_max = -56

x_initial_max = 2000
y_initial_max = 4000
max_steps = 4000

def get_distance(initial_velocity, step, is_x = False):
    if is_x and initial_velocity < step:
        return (initial_velocity + 1) *initial_velocity /2
    return (2 * initial_velocity + 1 - step) * step / 2

y_velocity = []
total_pairs = set()

for step in range(1, max_steps):
    found_x_velocity = False
    x_velocity_per_step = []
    y_velocity_per_step = []

    for vx in range (1, x_initial_max):
        x_distance = get_distance(vx, step, True)
        if x_min <= x_distance <= x_max:
            #print(vx)
            found_x_velocity = True
            x_velocity_per_step.append(vx)
    
    if found_x_velocity:
        for vy in range(-100, min(step, y_initial_max)):
            y_distance = get_distance(vy, step)
            if y_min <= y_distance <= y_max:
                #print(vy)
                y_velocity.append(vy)
                y_velocity_per_step.append(vy)
    
    for pair in itertools.product(x_velocity_per_step, y_velocity_per_step):
        total_pairs.add(pair)

print(max(y_velocity))
print(len(total_pairs))
