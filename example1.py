import random

# Objective function
def func(x):
    return x**2

# Initialize particles
particles = [random.uniform(-10, 10) for _ in range(5)]
velocities = [0 for _ in range(5)]
pbest = particles[:]
gbest = min(particles, key=func)

for _ in range(10):
    for i in range(len(particles)):
        velocities[i] = (0.5 * velocities[i] +
                         random.random() * (pbest[i] - particles[i]) +
                         random.random() * (gbest - particles[i]))
        particles[i] += velocities[i]

        if func(particles[i]) < func(pbest[i]):
            pbest[i] = particles[i]

    gbest = min(pbest, key=func)

print("Best solution:", gbest)
