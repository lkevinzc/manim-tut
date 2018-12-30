from big_ol_pile_of_manim_imports import *

'''
7.1
plotting functions
'''
class PlotFunctions(GraphScene):
    # Before newer versions are released, try to set x_min, x_max
    # and y_min, y_max to be multiples of 0.5 to avoid non-symmetric tick
    # markings.
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN ,
        "function_color": RED ,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10,12,2),
    }
    # The CONFIG is to set some properties of the graph,
    # including axis width (height), range, tick, color,
    # and so forth. 
    #
    # The values defined in our class have priority over
    # the default values defined in the source file. But
    # for those we haven't define, they take default 
    # values listed in the following section.
    # 
    # -------------------------------------------
    # The default CONFIG of GraphScene is:
    #     CONFIG = {
    #     "x_min": -1,
    #     "x_max": 10,
    #     "x_axis_width": 9,
    #     "x_tick_frequency": 1,
    #     "x_leftmost_tick": None,  # Change if different from x_min
    #     "x_labeled_nums": None,
    #     "x_axis_label": "$x$",
    #     "y_min": -1,
    #     "y_max": 10,
    #     "y_axis_height": 6,
    #     "y_tick_frequency": 1,
    #     "y_bottom_tick": None,  # Change if different from y_min
    #     "y_labeled_nums": None,
    #     "y_axis_label": "$y$",
    #     "axes_color": GREY,
    #     "graph_origin": 2.5 * DOWN + 4 * LEFT,
    #     "exclude_zero_label": True,
    #     "num_graph_anchor_points": 25,
    #     "default_graph_colors": [BLUE, GREEN, YELLOW],
    #     "default_derivative_color": GREEN,
    #     "default_input_color": YELLOW,
    #     "default_riemann_start_color": BLUE,
    #     "default_riemann_end_color": GREEN,
    #     "area_opacity": 0.8,
    #     "num_rects": 50,
    # }
    # -------------------------------------------

    def construct(self):
        # 1. Set up the axes
        # setting animate to be True shows fancy drawing process
        self.setup_axes(animate=True)
        
        # 2. Define functions
        # get_graph() receives argument that is a point to a function;
        #
        # if you don't specify color, get_graph() will cycle through
        # [BLUE, GREEN, YELLOW] for successive graphs.
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        # func_graph2=self.get_graph(lambda x: np.sin(x))#alternative

        # 3. Add a vertical line
        # input 1)the x-axis, 2)the graph the line is drawn to
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)

        # 4. Label graphs
        # you only get the label's texmobject and need to draw it
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2= self.get_graph_label(func_graph2,label = "sin(x)", x_val=-10, direction=UP/2)

        # 5. Place a remark
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)
         
        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),Write(two_pi))
     
    def func_to_graph(self,x):
        return np.cos(x)
     
    def func_to_graph2(self,x):
        return np.sin(x)

'''
7.2
a more complex plotting demostrating Taylor Series
'''
class Approximation(GraphScene):
    CONFIG = {
        "function": lambda x : np.cos(x),
        "taylor": [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
        lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point": 0,
        "approximation_color": GREEN,
        "x_min": -10,
        "x_max": 10,
        "y_min": -1,
        "y_max": 1,
        "graph_origin": ORIGIN ,
        "x_labeled_nums": range(-10,12,2),
    }
    def construct(self):
        self.setup_axes(animate=False)

        func_graph = self.get_graph(self.function)

        # list comprehension (search to learn more)
        # https://www.datacamp.com/community/tutorials/python-list-comprehension
        approx_graphs = [
        self.get_graph(f, self.approximation_color) 
        for f in self.taylor
        ]

        term_num = [
        TexMobject("n = " + str(n), aligned_edge=TOP)
        for n in range(0,8)]

        [t.to_edge(BOTTOM, buff=SMALL_BUFF) for t in term_num]

        term = TexMobject("")
        term.to_edge(BOTTOM,buff=SMALL_BUFF)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
            )

        self.play(ShowCreation(func_graph))

        for n,graph in enumerate(approx_graphs):
            self.play(
            Transform(approx_graph, graph, run_time = 2),
            Transform(term,term_num[n])
            )
            self.wait()