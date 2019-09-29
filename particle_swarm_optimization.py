import random as random

# Function to be maximized
def function(x):
    return (1 + 3*x - x*x)

# Number of particles = 5
particles = 5

# Number of iterations = 10
iterations = 10

# Inertia weight (random)
w = 0.7

# Cognitive and social parameters (random)
c1 = 0.2
c2 = 0.6

# Random numbers
r1 = []
r2 = []

# Initial particle position, particle velocity
particle_postion = []
particle_velocity = []

# Local and global best
pbest_fitness = []
pbest_location = []
gbest = 0
gbest_value = -1000 

# Initializing with random values
for i in range(particles):
    particle_postion.append(random.uniform(-1.0, 1.0))
    particle_velocity.append(random.uniform(-1.0, 1.0))
    r1.append(random.uniform(0.0, 1.0))
    r2.append(random.uniform(0.0, 1.0))

# Initial values
pbest_location = particle_postion

for i in range(particles):
    pbest_fitness.append(function(particle_postion[i]))
    if(function(particle_postion[i]) > gbest_value):
        gbest_value = function(particle_postion[i])
        gbest = particle_postion[i]

# Iterations
for i in range(iterations):
    temp_position = []
    temp_velocity = []
    temp_fitness = []

    # Velocity calculation
    val = 0.0    
    for j in range(particles):
        val = (w*particle_velocity[j] + c1*r1[j]*(pbest_location[j]-particle_postion[j]) + c2*r2[j]*(gbest-particle_postion[j]))
        temp_velocity.append(val)

    particle_velocity = temp_velocity

    # Position
    for j in range(particles):
        temp_position.append(particle_velocity[j] + particle_postion[j])

    particle_postion = temp_position

    # Fitness
    for j in range(particles):
        temp_fitness.append(function(particle_postion[j]))
        if(temp_fitness[j] > pbest_fitness[j]):
            pbest_fitness[j] = temp_fitness[j]
            pbest_location[j] = particle_postion[j]
    
    # Global best
    for j in range(particles):
        if(temp_fitness[j] > gbest_value):
            gbest = particle_postion[j]
            gbest_value = temp_fitness[j]

print(gbest_value)