def on_received_string(receivedString):
    global data_string
    list2: List[List[str]] = []
    data_string = receivedString
    list2[0] = "this".split(",")
radio.on_received_string(on_received_string)

data_string = ""
radio.set_group(1)
radio.set_transmit_power(7)
radio.set_frequency_band(0)