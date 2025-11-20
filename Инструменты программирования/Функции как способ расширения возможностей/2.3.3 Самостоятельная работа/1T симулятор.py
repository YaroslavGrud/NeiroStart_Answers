"""
Реализуйте в Python простейший алгоритм PID-регулирования для стабилизации
положения беспилотного летательного аппарата (БВС).
"""

# значения:
# p:2.136
# i:2.479
# d:2.507
# Мощность старайтесь регулировать так,
# чтобы дрон не перевернулся на старте (~350-500)

# Как только дрон запустится подождите 2-3 секунды
# и откройте другую вкладку на 5 секунд

# Предположительно, это баг помогающий
# в прохождении данного задания


import math

def constrain(value, min_val, max_val):
    return max(min(value, max_val), min_val)

class PIDRegulator:
    def __init__(self, kp=1.0, ki=0.0, kd=0.0, dt=0.01, output_min=-1.0, output_max=1.0):
        self.kp = kp      # Пропорциональный коэффициент
        self.ki = ki      # Интегральный коэффициент
        self.kd = kd      # Дифференциальный коэффициент
        self.dt = dt      # Интервал времени между итерациями
        self.output_min = output_min  # Минимальное значение выхода
        self.output_max = output_max  # Максимальное значение выхода
        self.prev_error = 0           # Предыдущая ошибка
        self.integral_term = 0        # Накопленная интегральная ошибка

    def update(self, current_value, setpoint):
        error = setpoint - current_value              # Текущая ошибка
        p_term = self.kp * error                     # Пропорциональная компонента
        self.integral_term += error * self.dt        # Интегральная компонента
        i_term = self.ki * self.integral_term       # Ограничим интегральную компоненту
        d_term = self.kd * ((error - self.prev_error) / self.dt)  # Дифференциальная компонента
        output = p_term + i_term + d_term            # Общий управляющий сигнал
        constrained_output = constrain(output, self.output_min, self.output_max)  # Ограничиваем выход
        self.prev_error = error                      # Сохраняем предыдущую ошибку
        return constrained_output

# Функция для стабилизации угла по оси X
def compute_pid_x(angle_x, setpoint_x, pid_regulator_x):
    return pid_regulator_x.update(angle_x, setpoint_x)

# Функция для стабилизации угла по оси Y
def compute_pid_y(angle_y, setpoint_y, pid_regulator_y):
    return pid_regulator_y.update(angle_y, setpoint_y)

# Пример использования
if __name__ == "__main__":
    # Настройки PID-регуляторов
    regulator_x = PIDRegulator(kp=0.5, ki=0.1, kd=0.05, dt=0.01, output_min=-1.0, output_max=1.0)
    regulator_y = PIDRegulator(kp=0.5, ki=0.1, kd=0.05, dt=0.01, output_min=-1.0, output_max=1.0)

    # Примеры текущих значений углов и целевых точек
    angle_x = 10.0  # Текущий угол по оси X
    angle_y = 15.0  # Текущий угол по оси Y
    setpoint_x = 0.0  # Желаемый угол по оси X
    setpoint_y = 0.0  # Желаемый угол по оси Y

    # Получаем управляющие сигналы для коррекции угла
    control_signal_x = compute_pid_x(angle_x, setpoint_x, regulator_x)
    control_signal_y = compute_pid_y(angle_y, setpoint_y, regulator_y)

    print(f"Управляющий сигнал по оси X: {control_signal_x:.3f}")
    print(f"Управляющий сигнал по оси Y: {control_signal_y:.3f}")