#!/home/pi/ledStrip/flask/bin/python3
# -*- coding: utf-8 -*-
# @Author: David Leimroth
# @Date:   2017-02-26 19:28:09
# @Last Modified by:   David Leimroth
# @Last Modified time: 2017-02-26 21:30:08

from flask import Flask, jsonify, make_response
import wpApp as wp
'''

Mode 1 Regular

0 - 0 | * 20
1 - 20 | * 20
2 - 40 | * 20
3 - 60 | * 20
4 - 80 | * 20
5 - 100 | * 20

Mode 2 Blinking

0 - 0
1 - 10 | * 10
2 - 30 | * 15
3 - 50 | * 16,6
4 - 70 | * 17,5
5 - 90 | * 18


'''


def routes():
    @app.route('/set/red/', methods=['GET', 'POST'])
    @app.route('/set/red/<value>', methods=['GET', 'POST'])
    def red(value=0):
        wp.setRed(value)
        return 'Set red to {}'.format(value)

    @app.route('/set/green/', methods=['GET', 'POST'])
    @app.route('/set/green/<value>', methods=['GET', 'POST'])
    def green(value=0):
        wp.setGreen(value)
        return 'Set green to {}'.format(value)

    @app.route('/set/blue/', methods=['GET', 'POST'])
    @app.route('/set/blue/<value>', methods=['GET', 'POST'])
    def blue(value=0):
        wp.setBlue(value)
        return 'Set blue to {}'.format(value)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    try:
        wp.setup()
        app = Flask(__name__)
        routes()
        app.run(host='0.0.0.0')
    except KeyboardInterrupt:
        wp.turn_off()
        print('Bye bye')
        raise KeyboardInterrupt
    except Exception as e:
        print(str(e))
