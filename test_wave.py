import wave
import test_function

dt = 0.003
dx = 0.1
t_end = 20.
x_end = 6.

W = wave.Wave(dt, dx, t_end, x_end, 5.0, [0., 0.], function_t0 = test_function.sin_t0)

W.wave_solve()

W.show()

