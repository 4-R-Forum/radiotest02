def on_received_string(receivedString):
    global data_string, comma_at, temp, light2
    data_string = receivedString
    comma_at = data_string.index_of(",")
    temp = parse_float(data_string.substr(0, comma_at - 1))
    light2 = parse_float(data_string.substr(comma_at + 1, len(data_string) - (comma_at + 1)))
    datalogger.log(datalogger.create_cv("0", temp),
        datalogger.create_cv("1", light2))
radio.on_received_string(on_received_string)

light2 = 0
temp = 0
comma_at = 0
data_string = ""
radio.set_group(1)
radio.set_transmit_power(7)
radio.set_frequency_band(0)

def on_every_interval():
    global data_string, comma_at, temp, light2
    data_string = "" + convert_to_text(input.temperature()) + "," + convert_to_text(input.light_level())
    comma_at = data_string.index_of(",")
    temp = parse_float(data_string.substr(0, comma_at - 0))
    light2 = parse_float(data_string.substr(comma_at + 1, len(data_string) - (comma_at + 1)))
    datalogger.log(datalogger.create_cv("Temp", temp),
        datalogger.create_cv("Light", light2))
loops.every_interval(1000, on_every_interval)
