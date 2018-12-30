from big_ol_pile_of_manim_imports import *

'''
8.1
drawing a number plane
'''

class DrawAnAxis(Scene):
    # The CONFIG contains attributes owned by this class,
    # and the plane_kwargs is sent to NumberPlane to
    # replace the default setting values.
    CONFIG = {
        "plane_kwargs" : {
            "x_line_frequency" : 2,
            "y_line_frequency" : 2
            }
        }
    
    def construct(self):
        # #####
        # First, set up a Cartesian axes using NumberPlane class
        # in coordinate_systems.py.
        # We will get two axes and an underlying grid.
        # #####

        # The double asterisk lets the class know that this is a
        # dictionary that needs to be unpack
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        
        self.play(ShowCreation(my_plane))
        self.wait()

'''
8.2
creating a constant vector field
'''
class SimpleField(Scene):
    CONFIG = {
        "plane_kwargs" : {
            "color" : RED
            },
    }

    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create number plane
        plane.add(plane.get_axis_labels()) #add x and y label
        self.add(plane) #Place grid on screen
         
        points = [x*RIGHT+y*UP
        for x in np.arange(-5,5,1)
        for y in np.arange(-5,5,1)
        ] #List of vectors pointing to each grid point

        vec_field = [] #Empty list to use in for loop
        for point in points:
            # here the filed is not of unit length, but it's ok
            field = 0.5*RIGHT + 0.5*UP #Constant field to upper right
            result = Vector(field).shift(point) #Create vector and shift it to grid point
            vec_field.append(result) #Append to list
         
        draw_field = VGroup(*vec_field) #Pass list of vectors to create a VGroup
        
        self.play(ShowCreation(draw_field)) #Draw VGroup on screen

'''
8.3
creating a variable vector field
'''
class StaticEField(Scene):
    CONFIG = {
        "plane_kwargs": {
            "color" : RED_B,
            "x_unit_size": 0.5,
            "y_unit_size": 0.5,},

        "point_charge_loc": 0.5*RIGHT-1.5*UP,

    }

    def construct(self):
        intro_text1 = TextMobject('Let\'s draw the electric field'
            ' for a positive point charge') 
        intro_text2 = TextMobject('located at $(0.5,-1.5)$ !')
        intro_text2.shift(DOWN)

        eq_text = TextMobject('Its field is described by')
        eq = TexMobject('\\vec{E} = \\frac{1}{4 \\pi \\epsilon_0} \\frac{q}{r^3} \\vec{r}')
        eq.shift(DOWN)

        eq_text2 = TextMobject('Ignoring the constant term, we evaluate')
        eq2 = TexMobject('\\vec{E} = \\frac{1}{r^3} \\vec{r}')
        eq2.shift(DOWN)

        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9) # so opacity is (1-0.9) = 0.1
        plane.add(plane.get_axis_labels())
         
        field = VGroup(*[self.calc_field(x*0.5*RIGHT+y*0.5*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
        ])
         
        # point_charge = PointCloudDot(self.point_charge_loc, color=BLUE)

        self.play(Write(intro_text1), Write(intro_text2))
        self.wait(3)
        self.play(FadeOut(intro_text1), FadeOut(intro_text2))
        
        self.play(Write(eq_text), Write(eq))
        self.wait(3)
        self.play(Transform(eq_text, eq_text2), Transform(eq, eq2))
        
        self.wait(2)
        self.play(FadeOut(eq_text), FadeOut(eq))

        self.play(ShowCreation(plane))
        # self.play(ShowCreation(point_charge))
        self.play(ShowCreation(field))
        self.wait(2)
     
    def calc_field(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)

        efield = (point - self.point_charge_loc)/r**3
        # Try out these two fields:
        # efield = np.array((-y,x,0))/math.sqrt(x**2+y**2)
        # efield = np.array(( -2*(y%2)+1 , -2*(x%2)+1 , 0 ))/3

        # scaled to 0.1 to avoid overlapping
        return Vector(0.1*efield).shift(point)  