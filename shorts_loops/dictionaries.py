def main():
    spacecraft = {'name': 'Voyager 1', 'distance': '163'}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
========= REPORT ========

Name: {spacecraft['name']}
Distance: {spacecraft['distance']} AU

=========================
"""


main()


def main():
    spacecraft2 = {'name': 'James Webb Space Telescope'}
    spacecraft2['distance'] = 0.01
    print(create_report(spacecraft2))


def create_report(spacecraft2):
    return f"""
========= REPORT ========

Name: {spacecraft2['name']}
Distance: {spacecraft2['distance']} AU

=========================
"""


main()


def main():
    spacecraft2 = {'name': 'James Webb Space Telescope'}
    print(create_report(spacecraft2))


def create_report(spacecraft2):
    return f"""
========= REPORT ========

Name: {spacecraft2.get('name', 'Unkonwn')}
Distance: {spacecraft2.get('distance', 'Unknown')} AU

=========================
"""


main()