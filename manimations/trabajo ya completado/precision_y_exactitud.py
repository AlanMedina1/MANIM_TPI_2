from manim import *
import random
#Clase base
class TargetScene(Scene):
    def _draw_target(self): #Esto DEBERIA dibujar los circulos
        circles = VGroup (
            Circle(radius = 1.5, color=BLUE),
            Circle(radius = 1, color=BLUE),
            Circle(radius = 0.5, color=BLUE)
        )
        return circles.move_to(ORIGIN)
    
    def _create_shot(self, x, y):
        """Crea un disparo (cruz roja)."""
        return Cross(scale_factor=0.15, color=RED).move_to([x, y, 0])

    def _place_shots(self, coords):
        """Crea todos los disparos a partir de una lista de coordenadas."""
        return VGroup(*[self._create_shot(x, y) for x, y in coords])

    def _show_text(self, text, position=UP*3, color=YELLOW):
        """Muestra un texto en pantalla."""
        label = Text(text, font_size=36, color=color).move_to(position)
        self.play(Write(label))
        return label


#Escena 1 Baja Precisión y Baja Exactitud
class BajaPrecisionBajaExactitud(TargetScene):
    def construct(self):
        self._show_text("Baja Precisión y Baja Exactitud")
        target = self._draw_target()
        self.play(Create(target))

        # Disparos alejados y dispersos
        shots = [(random.uniform(1, 2)*random.choice([-1, 1]),
                  random.uniform(1, 2)*random.choice([-1, 1])) for _ in range(5)]
        dots = self._place_shots(shots)
        self.play(FadeIn(dots))

        explain = Text("Los disparos están lejos entre sí y del centro.", font_size=28)
        explain.next_to(target, DOWN*2)
        self.play(Write(explain))
        self.wait(3)


#Escena 2 Alta Precisión y Baja Exactitud
class AltaPrecisionBajaExactitud(TargetScene):
    def construct(self):
        self._show_text("Alta Precisión y Baja Exactitud")
        target = self._draw_target()
        self.play(Create(target))

        # Disparos juntos, pero lejos del centro
        shots = [(random.uniform(0.1, 0.3)+1, random.uniform(0.1, 0.3)) for _ in range(5)]
        dots = self._place_shots(shots)
        self.play(FadeIn(dots))

        explain = Text("Los disparos están agrupados, pero lejos del centro.", font_size=28)
        explain.next_to(target, DOWN*2)
        self.play(Write(explain))
        self.wait(3)


#Escena 3 Baja Precisión y Alta Exactitud
class BajaPrecisionAltaExactitud(TargetScene):
    def construct(self):
        self._show_text("Baja Precisión y Alta Exactitud")
        target = self._draw_target()
        self.play(Create(target))

        # Disparos centrados pero dispersos
        shots = [(random.uniform(-0.6, 0.6), random.uniform(-0.6, 0.6)) for _ in range(5)]
        dots = self._place_shots(shots)
        self.play(FadeIn(dots))

        explain = Text("Los disparos rodean el centro, pero no están juntos.", font_size=28)
        explain.next_to(target, DOWN*2)
        self.play(Write(explain))
        self.wait(3)


#Escena 4 Alta Precisión y Alta Exactitud
class AltaPrecisionAltaExactitud(TargetScene):
    def construct(self):
        self._show_text("Alta Precisión y Alta Exactitud")
        target = self._draw_target()
        self.play(Create(target))

        # Disparos centrados y agrupados
        shots = [(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)) for _ in range(5)]
        dots = self._place_shots(shots)
        self.play(FadeIn(dots))

        explain = Text("Los disparos están juntos y cerca del centro.", font_size=28)
        explain.next_to(target, DOWN*2)
        self.play(Write(explain))
        self.wait(3)