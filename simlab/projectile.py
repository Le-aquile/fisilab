import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ProjectileMotion:
    def __init__(self, v0=20, angle_deg=45, g=9.81, time_step=0.01):
        # Parametri del proiettile
        self.g = g  # Accelerazione gravitazionale (m/s^2)
        self.v0 = v0  # Velocità iniziale (m/s)
        self.angle_deg = angle_deg  # Angolo di lancio (gradi)
        self.angle_rad = np.radians(angle_deg)  # Angolo in radianti
        self.time_step = time_step  # Intervallo di tempo (s)

        # Calcoli iniziali
        self.v0x = self.v0 * np.cos(self.angle_rad)  # Componente x della velocità
        self.v0y = self.v0 * np.sin(self.angle_rad)  # Componente y della velocità
        self.t_max = 2 * self.v0y / self.g  # Tempo di volo totale
        self.x_max = self.v0x * self.t_max  # Distanza massima

        # Genera i dati della traiettoria
        self.t = np.arange(0, self.t_max, self.time_step)
        self.x = self.v0x * self.t
        self.y = self.v0y * self.t - 0.5 * self.g * self.t**2

    def init(self):
        # Funzione di inizializzazione per l'animazione
        self.point.set_data([], [])
        self.trajectory.set_data([], [])
        return self.point, self.trajectory

    def update(self, frame):
        # Funzione di aggiornamento per l'animazione
        if self.y[frame] < 0:
            return self.point, self.trajectory  # Non aggiorna più il punto e la traiettoria
        self.point.set_data([self.x[frame]], [self.y[frame]])  # Posizione del proiettile
        self.trajectory.set_data(self.x[:frame], self.y[:frame])  # Aggiorna la traiettoria
        return self.point, self.trajectory

    def animate(self):
        # Configura l'animazione
        fig, ax = plt.subplots(figsize=(8, 6))  # Imposta una dimensione fissa per il grafico (in pollici)
        fig.set_size_inches(8, 6)  # Imposta la dimensione fissa della figura in pollici
        ax.set_xlim(0, 45)
        ax.set_ylim(0, 30)
        ax.set_xlabel('Distanza (m)')
        ax.set_ylabel('Altezza (m)')
        ax.set_title('Simulazione del moto di un proiettile')

        # Oggetto per il punto animato e la traiettoria
        self.point, = ax.plot([], [], 'ro', label='Proiettile')
        self.trajectory, = ax.plot([], [], 'b-', lw=0.5, label='Traiettoria')

        # Crea l'animazione
        frames = len(self.t)
        ani = FuncAnimation(fig, self.update, frames=frames, init_func=self.init, blit=True, interval=20, repeat=False)

        plt.legend()
        plt.show()

# Esegui l'animazione
projectile = ProjectileMotion(v0=20, angle_deg=45)
projectile.animate()
