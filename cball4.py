# cball4.py
from projectile import Projectile

# Prompting user for values
def get_inputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (m/s): "))
    h = float(input("Enter the initial height (m): "))
    t = float(input("Enter the time interval b/n position calculations: "))
    return a, v, h, t

# Calling main function
def main():

    angle, vel, h0, time = get_inputs()
    cball = Projectile(angle, vel, h0)

    while (cball.get_y() >= 0):
        cball.update(time)

    print("\nDistance traveled: {0:0.1f} meters.".format(cball.get_x()))

if __name__ == '__main__':
    main()
