#/usr/bin/python3

import sys
import pyshark
import argparse
import time

# Inorder to run this module please have following things running
# 1. python3 ==> Python3 should be installed
# 2. tshark  ==> tshark should be installed on the Device
# 3. pyshark ===> pyshark package should be installed on python3 interpretor 
# 4. argparse ===> argparse package should be installed on python3 interpretor



class flow_analyzer():

  def __init__(self):
    """ Flow Analyzer constructor.
      
    This construtor will instantiate argparser class and reads all options provided as command line arguments. 
    """
    self.parser=argparse.ArgumentParser()
    self.parser.add_argument("-i", "--interface", type=str, help="Specify the name of the interface to capture flow", required=True)
    self.parser.add_argument("-c", "--count", type=int, help="Specify the number of packets to capture")
    self.parser.add_argument("-t", "--timeout", type=int, help="Specify the duration in seconds to capture and Enter 0 to sniff continuously", default=30)
    self.parser.add_argument("-s", "--src", help="Specify the source IP of the flow")
    self.parser.add_argument("-d", "--dst", help="Specify the Destination IP of the flow")
    self.parser.add_argument("-S", "--sport", help="Specify the source port of the flow")
    self.parser.add_argument("-P", "--dport", help="Specify the destination port of the flow")
    self.parser.add_argument("-p", "--protocol", help="Specify the protocol of the flow")
    self.args = self.parser.parse_args()

  def start_sniff(self):
    """ Flow Sniffer module.
      
    This module will LiveCapture class and starts to capture packets. If timeout value is 0 then module will sniff continuously. 
    """

    print("\nStarting packet capture:\n")
    self.packets = pyshark.LiveCapture(interface = self.args.interface)
    try: 
      if self.args.timeout != 0 :
        self.packets.sniff(timeout=self.args.timeout)
        if len(self.packets) is 0:
          print("\nFails to capture packets")
          raise Exception('No Packets received on the sniffing interface') 
      else :
        self.packets.sniff_continuously(packet_count=self.args.count) 
   
    except Exception as error:
      print("\nCaught exception {}".format(error))


  def show_capture(self, packet_index=0):

    try : 
      if len(self.packets) is 0:
        print("\nFails to capture packets")
        raise Exception('No Packets received on the sniffing interface') 
      print("\nCaptured packets are : \n")
      if self.args.timeout != 0 :
        self.packets[packet_index].show()
      else :
        print(str(self.packets[packet_index]))

    except Exception as error :
      print("\nCaught exception {}".format(error))

#  def save_flow_info_to_db(self):

     
  
#  def read_flow_info_from_db(self):


if __name__ == '__main__' :
  """ Flow Analyzer Main block.
      
  Entire module flow defined in this block. 
  """

  print("\nSniffing interface is : %s" % (sys.argv[1]))
  print("\nStarted at  : %s" % (str(time.localtime())))
  
  # Instantiating flow_analyzer class 
  fs = flow_analyzer()
  # Starts sniffing on the given interface for given interval
  fs.start_sniff()
  # Displays captured packets
  fs.show_capture()
  print("\n10th packet is:\n")
  fs.show_capture(5)
  print("\nStopped at  : %s" % (str(time.localtime())))
 
 


