import sys
import os
from time import sleep

sys.path.insert(0, os.path.abspath('.'))

from lib.interface import Interface
from config import DOBOT_SERIAL_PORT

bot = Interface(DOBOT_SERIAL_PORT)

# Configurações iniciais de velocidade
bot.set_jog_joint_params([20, 20, 20, 30], [100, 100, 100, 100])
bot.set_jog_coordinate_params([20, 20, 20, 30], [100, 100, 100, 100])
bot.set_jog_common_params(100, 100)

#print('Bot status:', 'connected' if bot.connected() else 'not connected')

# Etapa 1: aproxima-se do objeto
print('Movendo para frente até o objeto')
bot.set_jog_command(1, 3)
sleep(2)
bot.set_jog_command(1, 0)
sleep(0.5)

print('Descendo até o objeto')
bot.set_jog_command(1, 5)
sleep(2)
bot.set_jog_command(1, 0)
sleep(0.5)

# Etapa 2: fecha a garra para pegar
print('Fechando a garra (pegando objeto)')
bot.set_end_effector_gripper(True, True)
sleep(1)

# Etapa 3: levanta o objeto
print('Levantando o objeto')
bot.set_jog_command(1, 6)
sleep(2)
bot.set_jog_command(1, 0)
sleep(0.5)

# Etapa 4: move para novo local
print('Movendo para a direita')
bot.set_jog_command(1, 2)
sleep(2)
bot.set_jog_command(1, 0)
sleep(0.5)

# Etapa 5: desce e solta o objeto
print('Descendo para soltar o objeto')
bot.set_jog_command(1, 5)
sleep(2)
bot.set_jog_command(1, 0)
sleep(0.5)

print('Abrindo a garra (soltando objeto)')
bot.set_end_effector_gripper(True, False)
sleep(1)

# Etapa 6: sobe e retorna
print('Subindo após soltar')
bot.set_jog_command(1, 6)
sleep(2)
bot.set_jog_command(1, 0)
sleep(0.5)

print('Movendo de volta para posição inicial')
bot.set_jog_command(1, 1)
sleep(2)
bot.set_jog_command(1, 0)
sleep(0.5)

# Desativa a garra
print('Desligando a garra')
bot.set_end_effector_gripper(False, False)

print('Sequência finalizada.')