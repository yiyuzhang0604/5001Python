# Name: Yiyu Zhang
# Github: https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-YiyuZhang

from laserbeam import LaserBeam
from asteroid import Asteroid
from spaceship import Spaceship


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.fadeout = fadeout
        # when hit an asteroid
        self.spaceship_hit = False
        self.asteroid_destroyed = False
        self.asteroids = [Asteroid(self.SPACE)]
        self.laser_beams = []
        self.spaceship = Spaceship(self.SPACE)

    def update(self):
        """Updates game state on every frame"""
        self.do_intersections()

        for asteroid in self.asteroids:
            asteroid.display()

        # ======================================================
        # TODO: Problem 3, Part 2: Laser beam handler
        # Your code will replace (or augment) the next several
        # lines. Laser beam objects should remain in the scene
        # as many frames as their lifespan allows.
        # Begin problem 3 code changes

        for i in range(len(self.laser_beams)):
            if self.laser_beams[i].count < 100:
                self.laser_beams[i].display()

        # End problem 3, part 2 code changes
        # =======================================================

        self.spaceship.display()

        # Carries out necessary actions if game over
        if self.spaceship_hit:
            # if spaceship hit an asteroid
            if self.fadeout <= 0:
                fill(1)
                textSize(30)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/2 - 165, self.SPACE['h']/2)
            else:
                self.fadeout -= 1

        if self.asteroid_destroyed:
            fill(1)
            textSize(30)
            text("YOU DESTROYED THE ASTEROIDS!!!",
                 self.SPACE['w']/2 - 250, self.SPACE['h']/2)

    def fire_laser(self, x, y, rot):
        """Add a laser beam to the game"""
        x_vel = sin(radians(rot))
        y_vel = -cos(radians(rot))
        count = 0
        self.laser_beams.append(
            LaserBeam(self.SPACE, x, y, x_vel, y_vel, count)
            )

    def handle_keypress(self, key, keycode=None):
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def handle_keyup(self):
        if self.spaceship.intact:
            # updated the above line of code to if instead of if not
            self.spaceship.control('keyup')

    def do_intersections(self):
        # ======================================================
        # TODO: Problem 4, Part 1: Intersections
        # Here's where you'll probably want to check for intersections
        # between asteroids and laser beams. Laser beams should be removed
        # from the scene if they hit an asteroid, and the asteroid should
        # blow up (the blow_up_asteroid method also must be written. It's
        # been started for you below).
        #
        # The intersection logic below between the spaceship
        # and asteroids should give a hint as to how this will work.
        # Begin code changes for Problem 3, Part 1: Intersections

        hit_asteroid = []
        hit_laser_beam = []

        for i in range(len(self.asteroids)):
            for j in range(len(self.laser_beams)):
                if(
                    abs(self.asteroids[i].x - self.laser_beams[j].x)
                    < max(self.asteroids[i].radius,
                          self.laser_beams[j].radius)
                    and
                    abs(self.asteroids[i].y - self.laser_beams[j].y)
                    < max(self.asteroids[i].radius,
                          self.laser_beams[j].radius)):
                    # We've shoot an asteroid
                    hit_asteroid.append((i, j))
                    hit_laser_beam.append(j)
        for (i, j) in hit_asteroid:
            self.blow_up_asteroid(i, j)

        for j in sorted(hit_laser_beam):
            del self.laser_beams[j]

        # End of code changes for Problem 4, Part 1: Intersections
        # ======================================================
        # If the space ship still hasn't been blown up
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                if (
                    abs(self.spaceship.x - self.asteroids[i].x)
                    < max(self.asteroids[i].radius,
                          self.spaceship.radius)
                    and
                    abs(self.spaceship.y - self.asteroids[i].y)
                    < max(self.asteroids[i].radius,
                          self.spaceship.radius)):
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True

    def blow_up_asteroid(self, i, j):
        # ======================================================
        # TODO: Problem 4, Part 2: Asteroid blow-up

        # Here you'll write the code to blow up an asteroid.
        # The parameters represent the indexes for the list of
        # asteroids and the list of laser beams, indicating
        # which asteroid is hit by which laser beam.

        # You'll need to:
        # A) Remove the hit asteroid from the scene
        # B) Add appropriate smaller asteroids to the scene
        # C) Make sure that the smaller asteroids are positioned
        #    correctly and flying off in the correct directions

        # Specifically. If the large asteroid is hit, it should
        # break into two medium asteroids, which should fly off
        # perpendicularly to the direction of the laser beam.

        # If a medium asteroid is hit, it should break into three
        # small asteroids, two of which should fly off perpendicularly
        # to the direction of the laser beam, and the third
        # should fly off in the same direction that the laser
        # beam had been traveling.

        # If a small asteroid is hit, it disappears.

        # Begin code changes for Problem 4, Part 2: Asteroid blow-up
        # Check the asteroid size
        target = self.asteroids[i]
        velocity_change = [(self.laser_beams[j].y_vel,
                            -self.laser_beams[j].x_vel),
                           (-self.laser_beams[j].y_vel,
                            self.laser_beams[j].x_vel),
                           (self.laser_beams[j].x_vel,
                            self.laser_beams[j].y_vel)]

        if target.asize == 'Large':
            new_size = 'Med'
            pieces = 2

        elif target.asize == 'Med':
            new_size = 'Small'
            pieces = 3

        elif target.asize == 'Small':
            pieces = 0

        FACTOR = 5
        VEL_FACTOR = 2
        for p in range(pieces):
            new_x = target.x + velocity_change[p][0] * FACTOR
            new_y = target.y + velocity_change[p][1] * FACTOR
            new_x_vel = velocity_change[p][0]/VEL_FACTOR
            new_y_vel = velocity_change[p][1]/VEL_FACTOR

            new_asteroid = Asteroid(self.SPACE, asize=new_size,
                                    x=new_x, y=new_y,
                                    x_vel=new_x_vel, y_vel=new_y_vel,
                                    rot=0.0, rot_vel=0.0)
            self.asteroids.append(new_asteroid)

        del self.asteroids[i]
        if (len(self.asteroids) == 0):
            self.asteroid_destroyed = True
