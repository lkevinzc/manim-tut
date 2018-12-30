from big_ol_pile_of_manim_imports import *

'''
4.1
Creating text
'''
class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        # add to screen immediately
        # Write() will show the process
        self.add(my_first_text, second_line)    
                                                
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)           # shift immediately
                                            # shift with animation
        self.play(ApplyMethod(my_first_text.shift,3*UP)) 

'''
4.2
Changing
text
'''
class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge",
            color=RED)
        # quote.set_color(RED)
        quote.to_edge(UP)

        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)

        author = TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
         
        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(
            Transform(quote,quote2),
            ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT)
            )

        self.play(ApplyMethod(author.match_color,quote2))

        # Transform(A, B) is to give all properties of B
        # to A, while the entity of A still remains.
        # Thus, FadeOut refers to quote instead of quote2.
        self.play(FadeOut(quote))

        self.play(ApplyMethod(author.move_to, ORIGIN))
        self.play(ApplyMethod(author.scale,2))  # double its size

'''
4.3
Rotating and highlighting
text
'''
class RotateAndHighlight(Scene):
    #Rotation of text and highlighting with surrounding geometries
    def construct(self):
        # filled with yellow, and its edge is red
        square=Square(side_length=5,fill_color=YELLOW, color=RED, fill_opacity=1)
        
        label=TextMobject("Text at an angle")
        label.add_background_rectangle(opacity=1, color=BLUE)
        label.rotate(TAU/8)

        label2=TextMobject("Boxed text",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=GREEN,fill_color=RED, fill_opacity=.5)
        # VGroup: order matters; try swap
        # 1. Higher level grouping; the original mobjects are 
        # not destroyed; you could still change its properties
        # and use it.
        # 2. The first mobject is placed under the second
        label2_group=VGroup(label2.bg,label2)
        label2_group.next_to(label,DOWN)


        
        label3=TextMobject("Rainbow")
        label3.scale(2)
        # Put in any number of colors
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)
         
        self.add(square)
        self.play(FadeIn(label))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        # Below shows the background is separated from the grouped
        self.play(Rotating(label2.bg, runtime=3, about_point=ORIGIN))


            