import math

# New code

radius = float(input('Enter the radius of the circle: '))

circumference = calculate_circumference(radius)
area = calculate_area(radius)

with open('circle_results.txt', 'w') as f:
    f.write(f'Radius: {radius}\n')
    f.write(f'Circumference: {circumference}\n')
    f.write(f'Area: {area}\n')

print('Results written to circle_results.txt')
