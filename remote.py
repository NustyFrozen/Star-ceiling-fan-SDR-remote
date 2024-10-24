#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: v3.9.2.0-85-g08bb05c1

from ast import Or
from distutils.version import StrictVersion
from imaplib import Commands

import gnuradio
import gnuradio.eng_option
import serial
from sympy import false

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
from gnuradio.eng_option import eng_option
import sip
from optparse import OptionParser, OptionGroup
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import string
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import soapy



from gnuradio import qtgui


class ASK(gr.top_block, Qt.QWidget):

    def __init__(self,hexCommand):
        gr.top_block.__init__(self, "Simple ASK", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Simple ASK")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ASK")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 1900
        self.samp_rate = samp_rate = 4e6
        self.center_freq = center_freq = 433.92e6

        ##################################################
        # Blocks
        ##################################################

        self.soapy_hackrf_sink_2 = None
        dev = 'driver=hackrf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_hackrf_sink_2 = soapy.sink(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_hackrf_sink_2.set_sample_rate(0, samp_rate)
        self.soapy_hackrf_sink_2.set_bandwidth(0, 0)
        self.soapy_hackrf_sink_2.set_frequency(0, center_freq)
        self.soapy_hackrf_sink_2.set_gain(0, 'AMP', True)
        self.soapy_hackrf_sink_2.set_gain(0, 'VGA', min(max(26, 0.0), 47.0))
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "test", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.1)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        message = []
        integer = int(hexCommand, 16)
        bin = format(integer, '0>74b')  #a command has 74 bit of binary
        for c in bin:
            message.append(int(c)) #appending the binary format to 1 and 0s for the vector message
        
        #requires delay for each command send so delay = 1900 * 4
        for i in range(0,8):
            message.append(0)
        print("built vector " + str(message))
        self.blocks_vector_source_x_0 = blocks.vector_source_c(message, True, 1, [])
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, sps)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 22.102355957e3, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.soapy_hackrf_sink_2, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ASK")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.blocks_repeat_0.set_interpolation(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.soapy_hackrf_sink_2.set_sample_rate(0, self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.soapy_hackrf_sink_2.set_frequency(0, self.center_freq)


        




if __name__ == '__main__':
    
    Command = ['PAIR', 'ON', 'OFF', 'FAN-3', 'FAN-2','FAN-1','FAN-OFF']
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-s", "--serial", dest="serial", type="str", default='96d965b6db6d',
                      help="The paired serial/ the serial you want to pair must be 12-Digit Hex Value")
    parser.add_option("-c", "--command", dest="command", default='ON',
                      type='choice', choices=Command,
                      help="The command you want to send to the celling fan"
                           "'PAIR' - Pair with the serial "
                           "'ON' - Turn on the light "
                           "'OFF' - Turn off the light "
                           "'FAN-X' - Turn on the fan at speed X (X = 3,2,1) "
                           "'FAN-OFF' Turn off the fan")
    options, _ = parser.parse_args()
    if(all(c in string.hexdigits for c in options.serial) == False | len(options.serial) != 12):
        parser.error('invalid 12 digit hex serial at ' + options.serial)
    #messageProtocol = serial
    messageProtocol = str(options.serial)

    #messageProtocol = serial + command
    if(options.command == 'PAIR'):
        messageProtocol = (messageProtocol) + ('92c')
    elif(options.command == 'ON'):
        messageProtocol = (messageProtocol) + ('b6c')
    elif(options.command == 'OFF'):
        messageProtocol = (messageProtocol) + ('925')
    elif(options.command == 'FAN-3'):
        messageProtocol = (messageProtocol) + ('96d')
    elif(options.command == 'FAN-2'):
        messageProtocol = (messageProtocol) + ('b2d')
    elif(options.command == 'FAN-1'):
        messageProtocol = (messageProtocol) + ('92d')
    elif(options.command == 'FAN-OFF'):
        messageProtocol = (messageProtocol) + ('96c')
    
    #messageProtocol = serial + command + protocol-version
    messageProtocol = str(messageProtocol) + ('b6d8')
    print('sending Protocol message -->' + messageProtocol)
    if(True):
        if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            style = gr.prefs().get_string('qtgui', 'style', 'raster')
            Qt.QApplication.setGraphicsSystem(style)
        qapp = Qt.QApplication(sys.argv)

        tb = ASK(hexCommand=messageProtocol)

        tb.start()

        tb.show()

        def sig_handler(sig=None, frame=None):
            tb.stop()
            Qt.QApplication.quit()

        signal.signal(signal.SIGINT, sig_handler)
        signal.signal(signal.SIGTERM, sig_handler)

        timer = Qt.QTimer()
        timer.start(500)
        timer.timeout.connect(lambda: None)

        qapp.exec_()
