from big_ol_pile_of_manim_imports import *

'''
10.1
creating a moving charge first
'''

# #####
# Based on the E-field created by the positive point
# charge in previous sections, we will animate the 
# movement of a positive point charge under this field.
#
# The computed values of velocity, acceleration, etc. 
# are not accurate since we didn't include many constant
# terms. However, the animation can approximate the process.
# #####
class MovingCharges(Scene):
    CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B,
            "x_unit_size": 0.5,
            "y_unit_size": 0.5,
            },
        "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)
         
        field = VGroup(*[self.calc_field(x*0.5*RIGHT+y*0.5*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
        ])
        self.field=field # stored to be used in self.moving_charge()

        source_charge = Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()
     
    def calc_field(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3

        return Vector(0.1*efield).shift(point)
     
    def moving_charge(self):
        # Just get ONE random point to start moving.
        # Try different number of points (but they don't react
        # to each other).
        numb_charges = 1
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(*[
            Positron().move_to(point)
            for point in points
        ])

        for particle in particles:
            particle.velocity = np.array((0,0,0))
     
        self.play(FadeIn(particles))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True

        # continual_update() only runs when there're animation
        # elements like play() or wait().
        self.wait(15)
     
    def field_at_point(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return efield
    
    # #####
    # 1) This method will update the screen for each frame during
    # the *entire scene*. This is different from various trans-
    # formation that rely on play() to animate because they only 
    # last for a short time interval. 
    #
    # 2) self.play(ApplyMethod(...)) is similar but hard for timing.
    #
    # 3) continual_update() is called each frame.

    def continual_update(self, *args, **kwargs):
        if hasattr(self, "moving_particles"):   # True only after
                                                # the starting
                                                # point chosen.
            dt = self.frame_duration
            for p in self.moving_particles:
                # a = Eq/m, but here we ignore the constant term
                accel = self.field_at_point(p.get_center())
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


'''
10.2
updating the E-field of a moving charge
'''
class FieldOfMovingCharge(Scene):
    CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B
            },
        "point_charge_start_loc" : 5.5*LEFT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)
         
        field = VGroup(*[self.create_vect_field(self.point_charge_start_loc,x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.field = field
        self.source_charge = Positron().move_to(self.point_charge_start_loc)
        self.source_charge.velocity = np.array((1,0,0)) # source charge's initial velocity
        self.play(FadeIn(self.source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()
     
    def create_vect_field(self,source_charge,observation_point):
        return Vector(self.calc_field(source_charge,observation_point)).shift(observation_point)

    def calc_field(self,source_point,observation_point):
        x,y,z = observation_point
        Rx,Ry,Rz = source_point
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z-Rz)**2)
        if r < 0.0000001: # Prevent being divided by zero
            efield = np.array((0,0,0))
        else:
            efield = (observation_point - source_point)/r**3
        return efield  # Not a Vector object since we don't display
                        # it on the screen directly. Instead, we need
                        # to add them up to determine the total field.

    def moving_charge(self):
        numb_charges = 3
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)

        # add the source_charge to the particles list
        particles = VGroup(self.source_charge, *[
            Positron().move_to(point)
            for point in points
            ])

        for particle in particles[1:]:  # not including the source
                                        # charge 
            particle.velocity = np.array((0,0,0))

        self.play(FadeIn(particles[1:]))# not including the source
                                        # charge 
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)

    def continual_update(self, *args, **kwargs):
        # Scene.continual_update(self, *args, **kwargs)
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
         
            for v in self.field:
                field_vect = np.zeros(3)# First set all to zero,
                                        # then add up fields from
                                        # all charges
                for p in self.moving_particles:
                    field_vect = field_vect + self.calc_field(p.get_center(), v.get_start())

                # re-scale vectors' lengths
                v.put_start_and_end_on(v.get_start(), (field_vect+v.get_start())) # 0.5 to scale
             
            for p in self.moving_particles:
                # get total field first
                total_field = np.zeros(3)
                for o_p in self.moving_particles:
                    if o_p != p:    # other particles
                        total_field = total_field + self.calc_field(o_p.get_center(), p.get_center())

                accel = total_field
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)
 
'''
helper class
'''
# Positron is used rather than proton because proton is roughly
# 2000 times more massive.
class Positron(Circle):
    CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
    }
    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        plus = TexMobject("+")
        plus.scale(0.7)
        plus.move_to(self)
        self.add(plus)