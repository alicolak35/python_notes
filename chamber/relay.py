

#GPIO'yu hazir et-BCM, BOARD

#flask'tan request metodu ile pin durumlarini getir
#gelen durumlari varolan role durumu ile kiyasla ve fark olanlari degistir(roleler yuksekteyken kapanir)

"""
3 mod var: el ile tetikleme, otomatik ve ikisinin secilmedigi
eger;
    ikisi secilmediyse roleler kapanir
    el ile yonetim secilmediyse(otomatik veya ikisinin secilmedigi durumsa) 2 saniye bekler, devam eder 

    
print("True" if False == 0 else "False")

RELAY_PINS = [4, 17, 27, 22, 5, 6, 13, 19]
RELAY_NAME_TO_INDEX = {
    "power_supply_1": 0,
    "power_supply_2": 1,
    "power_supply_3": 2,
    "humidifier": 3,
    "valve_1": 4,
    "valve_2": 5,
    "empty_relay_1": 6,
    "empty_relay_2": 7,
}

# Local mirror of relay states
relay_states = {name: False for name in RELAY_NAME_TO_INDEX}

new_states = {
    "power_supply_1": 0,
    "power_supply_2": 1,
    "power_supply_3": 1,
    "humidifier": 0,
    "valve_1": 0,
    "valve_2": 1,
    "empty_relay_1": 1,
    "empty_relay_2": 0,
}


for name, state in relay_states.items():
    pin_index = RELAY_NAME_TO_INDEX[name]
    gpio_state = GPIO.LOW if state else GPIO.HIGH  # Active LOW
    print(f"  {name}: {'ON' if gpio_state == GPIO.LOW else 'OFF'} (Pin {RELAY_PINS[pin_index]})")
"""

import threading
mode = "arti"
# break terminates the Thread
def fonk():
    while True:
        mode = input()
        if mode == "arti":
            continue

        if mode != "arti":
            break

threading.Thread(target=fonk, daemon=False).start()



