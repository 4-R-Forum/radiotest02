radio.onReceivedString(function (receivedString) {
    data_string = receivedString
    comma_at = data_string.indexOf(",")
    temp = parseFloat(data_string.substr(0, comma_at - 1))
    light2 = parseFloat(data_string.substr(comma_at + 1, data_string.length - (comma_at + 1)))
    datalogger.log(
    datalogger.createCV("0", temp),
    datalogger.createCV("1", light2)
    )
})
let light2 = 0
let temp = 0
let comma_at = 0
let data_string = ""
radio.setGroup(1)
radio.setTransmitPower(7)
radio.setFrequencyBand(0)
