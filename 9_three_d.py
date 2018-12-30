from big_ol_pile_of_manim_imports import *

'''
9.1
creating 3-d version of previous efield
'''

# #####
# Differences made:
# 1) Inherited from ThreeDScene class;
#
# 2) self.set_camera_orientation() to set the camera's initial
# position and orientation, and it is pointing towards the origin.
# This is an abrupt jump to that location and orientation.
#
# 3) self.move_camera() is smoother compared to the previous 
# method to move the camera to a specified location and orientation.
#
# 4) self.begin_ambient_camera_rotation() moves the camera smoothly.
# #####
class ExampleThreeD(ThreeDScene):
    CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B,
            "x_unit_size": 0.5,
            "y_unit_size": 0.5,
            },
        "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        self.set_camera_orientation(0, -np.pi/2)

        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        # point_charge = PointCloudDot(self.point_charge_loc, color=BLUE)
         
        field2D = VGroup(*[self.calc_field2D(x*0.5*RIGHT+y*0.5*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
        ])

        # self.play(ShowCreation(point_charge)) 
        self.play(ShowCreation(field2D))
        self.wait()

        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()

        self.wait(6)
     
    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3

        return Vector(0.1*efield).shift(point)

'''
9.2
plotting 3-d vector field 
'''
class EFieldInThreeD(ThreeDScene):
    CONFIG = {
        "plane_kwargs" : {
            "color" : RED_B,
            "x_unit_size": 0.5,
            "y_unit_size": 0.5,
            },
        "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        self.set_camera_orientation(0.1, -np.pi/2)
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)
         
        # field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
        # for x in np.arange(-9,9,1)
        # for y in np.arange(-5,5,1)
        # ])
        
        # point_charge = PointCloudDot(self.point_charge_loc, color=BLUE)

        field3D = VGroup(*[self.calc_field3D(x*0.5*RIGHT+y*0.5*UP+z*0.5*OUT)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            for z in np.arange(-5,5,1)
        ])
        
        # self.play(ShowCreation(point_charge)) 
        self.play(ShowCreation(field3D))
        self.wait()
        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(6)
     
    # def calc_field2D(self,point):
    #     x,y = point[:2]
    #     Rx,Ry = self.point_charge_loc[:2]
    #     r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
    #     efield = (point - self.point_charge_loc)/r**3
    #     return Vector(efield).shift(point)
     
    def calc_field3D(self,point):
        x,y,z = point
        Rx,Ry,Rz = self.point_charge_loc
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2+(z-Rz)**2)
        efield = (point - self.point_charge_loc)/r**3
        # Try out:
        # efield = np.array((-y,x,z))/math.sqrt(x**2+y**2+z**2)

        return Vector(0.1*efield).shift(point)