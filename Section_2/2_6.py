# 序列模式匹配
def InvalidCommend(message):
    return message


class Robot(object):

    def beep(self, times, frequency):
        pass

    def rotate_neck(self, angle):
        pass

    def leds(self, ident):
        pass

    def handle_command(self, message):
        match message:
            case ['BEEPER', frequency, times]:
                self.beep(times, frequency)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds(ident)
            case ['LED', ident, red, green, blue]:
                self.leds(ident)
            case _:
                raise InvalidCommend(message)


metro_areas = [
    ('Tokyo', 'JP', 36.933, (25.1223, 139.23432)),
    ('Mexico City', 'MX', 20.142, (19.2433242, -99.234243))
]


def main():
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon < 0:
                print(f"{name} {lat} {lon}")


if __name__ == '__main__':
    main()
