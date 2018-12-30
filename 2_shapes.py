from big_ol_pile_of_manim_imports import *
 
class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))
        words1=TextMobject("Hello World!")
        words2=TextMobject("Let's make some fun!")
        self.add(line)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))#morph any two objects
        self.play(ReplacementTransform(triangle,words1))
        self.clear()
        self.wait()

        #this is cool!
        self.play(Transform(words1,words2.set_color_by_gradient(YELLOW,GREEN,BLUE)))
        self.wait()

        # Scene.play will show the animations
        # Scene.add will appear things without animations 