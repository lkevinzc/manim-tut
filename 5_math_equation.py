from big_ol_pile_of_manim_imports import *

'''
5.1
writing equations
'''
class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        # ######
        # 1. An extra backslash must be included in 
        # front of all LaTeX commands in manim due
        # to how it parses the text.
        #
        # 2. Use curly brackets to enclose the part
        # you want to group together.
        #
        # 3. The main difference between TextMobject() 
        # and TexMobject is the text math object assumes 
        # everything is plain text unless you specify an 
        # equation with dollar signs while the Tex math 
        # object assumes everything is an equation unless 
        # you specify something is plain text using \\text{}
        # ######

        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject("\\vec{F}_{net} = \\sum_i \\vec{F}_i")
        eq2.shift(2*DOWN)

        # Write is a subclass of DrawBorderThenFill and 
        # needs to be put inside of play() to animate it.
        self.play(Write(eq1))
        self.play(Write(eq2))

'''
5.2
coloring equations
'''
class ColoringEquations(Scene):
    #Grouping and coloring parts of equations
    def construct(self):
        # #####
        # 1. set_color_by_tex takes individual string and the color,
        # while set_color_by_tex_to_color_map takes a dictionary.
        #
        # 2. Both set_color methods utilize get_parts_by_tex methods,
        # which means that all parts that contain specified string will
        # be colored (e.g. #1, #3 below).
        #
        # 3. Since we are using TexMobject, plain texts are enclosed
        # by \\text{}. (try out what will happen if you don't)
        # [The equation environment doesn't recognize spaces, uses
        # different fonts and spaces letters differently...]
        # #####

        line1=TexMobject(
            "\\text{The vector }", "\\vec{F}_{net}", 
            "\\text{ is the net force on object of mass }"
            )
        # --------------------------------------------------------- #
        # Try leaving only one of the following line uncommented    #
        # and commenting all others to see the effects.             #
        line1.set_color_by_tex("the", BLUE, case_sensitive=False)#1 #
        # line1.set_color_by_tex("F", BLUE)#2                       #
        # line1.set_color_by_tex("n", BLUE)#3                       #
        # line1.set_color_by_tex("force", BLUE)#4                   #
        # --------------------------------------------------------- #
        
        line2=TexMobject(
            "m", "\\text{ and acceleration }",
            "\\vec{a}", ". "
            )
        line2.set_color_by_tex_to_color_map({
        "m": YELLOW,
        "{a}": RED
        })

        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))

