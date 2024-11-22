from manim import *

class MotoArmonicoCircolare(Scene):
    def construct(self):
        # Impostazioni iniziali
        radius = 2  # Raggio del cerchio
        omega = 2 * PI  # Velocità angolare

        # Definizione del cerchio e dei punti
        circle = Circle(radius=radius, color=BLUE)
        center = Dot(ORIGIN, color=WHITE)
        moving_dot = Dot(color=RED)
        projection_dot = Dot(color=GREEN)

        # Linee di collegamento
        radius_line = always_redraw(lambda: Line(center.get_center(), moving_dot.get_center(), color=YELLOW))
        vertical_line = always_redraw(lambda: Line(
            moving_dot.get_center(),
            [moving_dot.get_center()[0], 0, 0],
            color=WHITE, stroke_opacity=0.5
        ))

        # Linea del moto armonico
        motion_line = NumberLine(x_range=[-4, 4, 1], length=8, include_numbers=True, color=WHITE)
        motion_line.shift(DOWN * 3)

        # Testo
        title = Text("Moto Circolare e Moto Armonico", font_size=28).to_edge(UP)

        # Posizionamento iniziale
        moving_dot.move_to([radius, 0, 0])
        projection_dot.move_to([radius, -3, 0])

        # Tracciato della proiezione (trail)
        projection_trail = TracedPath(projection_dot.get_center, stroke_color=GREEN, stroke_width=2)

        # Tracker del tempo
        time_tracker = ValueTracker(0)

        # Aggiorna posizione del punto in moto circolare
        def update_moving_dot(mob):
            angle = omega * time_tracker.get_value()
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            mob.move_to([x, y, 0])

        moving_dot.add_updater(update_moving_dot)

        # Aggiorna posizione del punto proiettato
        def update_projection_dot(mob):
            mob.move_to([moving_dot.get_center()[0], -3, 0])

        projection_dot.add_updater(update_projection_dot)

        # Aggiungi oggetti alla scena
        self.play(Create(circle), Create(center), Write(title))
        self.add(moving_dot, projection_dot, radius_line, vertical_line, motion_line, projection_trail)

        # Anima il tracker del tempo
        self.play(time_tracker.animate.set_value(10), run_time=10, rate_func=linear)

        # Fine della scena
        self.wait()
