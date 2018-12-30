from big_ol_pile_of_manim_imports import *

'''
6.1 (or 4.4; organize later)
aligning texts and using braces (less concise implementation)
'''
class UsingBraces(Scene):
    #Using braces to group text together
    def construct(self):
        eq1A = TextMobject("$4x + 3y$")
        eq1B = TextMobject("$=$")
        eq1C = TextMobject("$0$")
        eq2A = TextMobject("$5x - 2y$")
        eq2B = TextMobject("$=$")
        eq2C = TextMobject("$3$")

        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)

        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)

        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)
         
        eq_group=VGroup(eq1A,eq2A)
        braces=Brace(eq_group,LEFT)
        # get_text is to set the location of the text relative
        # to the braces, but it doesn't put it to the screen.
        eq_text = braces.get_text("A pair of equations")
         
        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))

'''
6.2
improved version
'''
class UsingBracesConcise(Scene):
    #A more concise block of code with all columns aligned
    def construct(self):
        # #####
        # 1. The equation is de-composited into
        # pieces that are stored in a list; the
        # for loop will align each element in 
        # both equations vertically.
        #
        # 2. The asterisk is a Python command to 
        # unpack the list and treat the argument
        # as a comma-separated strings.
        # [TexMobject(*eq1_text) is identical to
        #  TexMobject("4","x","+","3","y","=","0")]
        #
        # #####
        eq1_text=["4","x","+","3","y","=","0"]
        eq2_text=["5","x","-","2","y","=","3"]

        eq1_mob=TexMobject(*eq1_text)
        eq2_mob=TexMobject(*eq2_text)
        
        eq1_mob.set_color_by_tex_to_color_map({
        "x":RED_B,
        "y":GREEN_C
        })
        eq2_mob.set_color_by_tex_to_color_map({
        "x":RED_B,
        "y":GREEN_C
        })
        
        # actually for this example the effects are not so obvious
        for i,item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i], alignment_vect = RIGHT)

        eq1=VGroup(*eq1_mob)
        eq2=VGroup(*eq2_mob)

        eq2.shift(DOWN)

        eq_group=VGroup(eq1,eq2)

        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")
         
        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))
