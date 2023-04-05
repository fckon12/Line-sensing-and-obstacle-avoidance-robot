from ir_receiver import *; 
ir_rx.start();

//change lights on robot with red or green option
while True:
  if ir_rx.get_code() == IR_REMOTE_A:
    led_onboard.show(1, hex_to_rgb('#ff0000'))
    led_onboard.show(2, hex_to_rgb('#ff0000'))
  if ir_rx.get_code() == IR_REMOTE_B:
    led_onboard.show(1, hex_to_rgb('#00ff00'))
    led_onboard.show(2, hex_to_rgb('#00ff00'))
  ir_rx.clear_code()
  time.sleep(0.1)
