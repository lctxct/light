from manim import *
from math import sin, asin 

"""
Scenes: 
[1] ReflectionRayDiagram 
[2] MirrorWithWall
[3] ReflectionDemo 

"""

"""
How to draw a ray diagram of a reflection in a mirror (demo)
"""
class ReflectionRayDiagram(Scene): 
    def construct(self): 
        # Creating object 
        dots = [
            Dot(color=RED), 
            Dot(color=BLUE),
            Dot(point=(-1.5,1.5,0), radius=0.05, color=GREEN)
        ]
        dots[0].shift(LEFT)
        dots[1].shift(RIGHT)

        eye = Text("Eye", font_size=15).next_to(dots[2], UP)
        object = Text("Object", font_size=15).next_to(dots[0], LEFT)

        # Creating mirror 
        mirror = VGroup(*[Line((0,(-10+i)*0.2,0),(0.2,(-9+i)*0.2,0)) for i in range(20)], Line((0,2,0),(0,-2.05,0)))
        
        dist = DashedLine(dots[0].get_center(), (0,0,0))

        def get_eqn(x1, x2, y1, y2): 
            m = (y2-y1)/(x2-x1)
            c = y1 - m * x1 
            return m, c

        def get_y(m, c, x): 
            return m * x + c

        x1, x2 = dots[1].get_center()[0], dots[2].get_center()[0]
        y1, y2 = dots[1].get_center()[1], dots[2].get_center()[1]
        m, c = get_eqn(x1, x2, y1, y2)

        # Creating reflection lines 
        reflection = [
            Line((0, get_y(m, c, 0), 0), dots[2].get_center(), color=YELLOW, fill_opacity=0.2, stroke_width=3),
            Line(dots[0].get_center(), (0, get_y(m, c, 0), 0), color=YELLOW, fill_opacity=0.2, stroke_width=3),
            DashedLine(dots[1], dots[2]), 
            Arrow((0, get_y(m, c, 0), 0), dots[2].get_center(), color=YELLOW, tip_length=0.1, stroke_width=3),
            Arrow(dots[0].get_center(), (0, get_y(m, c, 0), 0), color=YELLOW, tip_length=0.1, stroke_width=3)
        ]


        self.add(mirror, dots[0], dots[2], eye, object)

        # Step 1 
        self.play(FadeIn(dist))
        self.wait()  

        self.play(dist.animate.move_to((0.5,0,0)))
        self.wait()

        self.play(FadeIn(dots[1]))
        self.wait() 

        self.play(FadeOut(dist))        
        self.play(Create(reflection[2]))
        self.wait() 

        self.play(Create(reflection[1]))
        self.play(Create(reflection[0]))
        self.play(Create(reflection[4]))
        self.play(Create(reflection[3]))
        self.play(Uncreate(reflection[2]))
        self.wait()


class MirrorWithWall(Scene): 
    def construct(self): 
        header = Text("Mirror with wall", font="Consolas").shift(UP*3+0.5)
        numberplane = NumberPlane(x_range=(- 7.111111111111111, 7.111111111111111, 0.5), y_range=(- 4.0, 4.0, 0.5))
        mirror = VGroup(*[Line(((3+i)*0.2,0,0),((4+i)*0.2,0.2,0)) for i in range(30)])

        objects = [
            Dot((1,-1,0), color=RED), 
            Dot((5,-1.5,0), color=BLUE), 
        ]

        images = [
            Dot((1,-objects[0].get_center()[1],0), color=RED), 
            Dot((5,-objects[1].get_center()[1],0), color=BLUE)
        ]

        eye = Dot((-3.5,-3,0), color=GREEN)

        wall = Rectangle(height=1.0, width=7.0).shift(LEFT*3)
        wall_label = Text("Wall", font="Consolas", font_size=15).next_to(wall, UP)

        lines = [
            DashedLine(images[0].get_center(), eye.get_center()), 
            DashedLine(images[1].get_center(), eye.get_center())
        ]
        

        self.add(header, numberplane, VGroup(*objects), eye, wall, wall_label, mirror, VGroup(*images), VGroup(*lines))



class ReflectionDemo(Scene): 
    def construct(self): 
        dot = Dot((-2, -2, 0), color=RED).shift(LEFT).shift(DOWN)
        mirror = VGroup(*[Line((0,(-20+i)*0.2,0),(0.2,(-19+i)*0.2,0)) for i in range(40)], Line((0,5,0),(0,-5,0)))

        reflections = VGroup(*[Line(dot.get_center(), (0, (-3+i)*0.3, 0), color=YELLOW) for i in range(10)])

        def get_eqn(x1, x2, y1, y2): 
            m = (y2-y1)/(x2-x1)
            c = y1 - m * x1 
            return m, c

        def get_y(m, c, x): 
            return m * x + c

        x1 = dot.get_center()[0]
        y1 = dot.get_center()[1]
        x2 = 0

        for i in range(10): 
            y2 = (-3+i)*0.3
            m, c = get_eqn(x1, x2, y1, y2)
            
            reflections += Line((0, (-3+i)*0.3, 0), (-1, get_y(-m, c, -1), 0), color=YELLOW)
            reflections += Dot((-1, get_y(-m, c, -1), 0), color=GREEN)


        self.add(dot, mirror, reflections)

class RefractionDemo(Scene): 
    def construct(self): 
        def snell(n1, n2, theta1): 
            return asin((n1/n2)*sin(theta1))

        boundary = Line()

        self.add(boundary)
