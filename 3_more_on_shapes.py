from big_ol_pile_of_manim_imports import *

class MoreShapes(Scene):
    #A few more simple shapes
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT) # defined in constants.py

        # Buffur factor to determine the scaling between 
        # the surrounding object and the surrouneded one.
        circle.surround(square,buffer_factor=2) 

        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        
        # curvedarrow starts from (1,0,0), ends at (5,0,0)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)

        arrow = Arrow(LEFT,UP)

        # buff determines how far
        arrow.next_to(circle,DOWN+LEFT,buff=0)
        rectangle.next_to(arrow,DOWN+LEFT,buff=0)

        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)
        self.add(pointer)
        self.play(FadeIn(square))

        # runtime to determine the duration of an animation
        self.play(Rotating(square,runtime=3),FadeIn(circle))

        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))
        self.wait(2)
        self.clear()

        words=TextMobject("Let's draw a pentagram")
        self.play(Write(words))
        self.play(FadeOut(words))

        r_pentagon = RegularPolygon(n=5,color=RED)

        vertices = r_pentagon.get_points_defining_boundary()
        print("before rotation:")
        print(vertices)
        self.play(ShowCreation(r_pentagon))
        self.play(Rotate(r_pentagon, angle=np.pi*(180-360/5-360/10)/360/2))
        
        new_vertices = r_pentagon.get_points_defining_boundary()
        print('after rotation:')
        print(new_vertices)

        self.wait()


        def mark_vertices(vertices):
            for point in vertices:
                self.add(Dot(point,radius=0.03,color=RED))

        # connect two vertices of any polygon that are not adjacent
        # vertices given should be in order
        lines_to_draw = []
        def conn_vertices(vertices):
            n = len(vertices)
            for i in range(n-2):
                for j in range(i+2, i+2 + n-3): #(n-3) lines
                    if j > n - 1:
                        break
                    new_line = Line(vertices[i],vertices[j],color=RED)
                    lines_to_draw.append(new_line)
            return VGroup(*lines_to_draw)   # The asterisk is to
                                            # unpack the list. 

        mark_vertices(new_vertices[:-1])# there is a repeated point
        self.wait()
        self.play(FadeOut(r_pentagon))
        self.play(ShowCreation(conn_vertices(new_vertices[:-1]))) 
        self.wait(2)


        
