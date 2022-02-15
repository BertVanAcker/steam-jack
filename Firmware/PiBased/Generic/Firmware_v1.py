import sys
if sys.platform.startswith('win'):
    print('Windows environment - imports adapted')
    from Firmware.PiBased.Generic.SJ_helpers.SJ_Generic_Firmware import SJ_Controller
    from Firmware.PiBased.Generic.DeviceSpecific.DeviceSpecific import DeviceSpecificFunctions
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin') or sys.platform.startswith('darwin'):
    print('Linux environment - imports adapted')
    sys.path.append('../')
    from SJ_helpers.SJ_Generic_Firmware import SJ_Controller
    from SJ_helpers.SJ_Generic_Firmware import SJ_Constants
    from DeviceSpecific.DeviceSpecific import DeviceSpecificFunctions


DEBUG = True
controller = SJ_Controller(DEBUG=DEBUG)

#------------function mapping----------------------------
deviceHandler = DeviceSpecificFunctions(DEBUG)
controller.attach(cmd=SJ_Constants.SJ_ActionLED,function=deviceHandler.ActionLED_function)
controller.attach(cmd=SJ_Constants.SJ_BlinkLED,function=deviceHandler.BlinkLED_function)
controller.attach(cmd=SJ_Constants.SJ_BlinkLEDSTOP,function=deviceHandler.BlinkLEDSTOP_function)
controller.attach(cmd=SJ_Constants.SJ_FetchTemperature,function=deviceHandler.FetchTemperature_function)
#--------------------------------------------------------



#start the controller
controller.start()

