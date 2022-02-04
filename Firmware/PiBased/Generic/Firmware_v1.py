import sys
if sys.platform.startswith('win'):
    print('Windows environment - imports adapted')
    from Firmware.PiBased.Generic.SJ_helpers.SJ_Generic_Firmware import SJ_Controller
    from Firmware.PiBased.Generic.DeviceSpecific.DeviceSpecific import DeviceSpecificFunctions
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin') or sys.platform.startswith('darwin'):
    print('Linux environment - imports adapted')
    sys.path.append('../')
    from SJ_helpers.SJ_Generic_Firmware import SJ_Controller
    from DeviceSpecific.DeviceSpecific import DeviceSpecificFunctions


DEBUG = True
controller = SJ_Controller(DEBUG=DEBUG)

#------------function mapping----------------------------
deviceHandler = DeviceSpecificFunctions(DEBUG)
controller.SJ_ActionLED_function = deviceHandler.ActionLED_function
controller.SJ_BlinkLED_function = deviceHandler.BlinkLED_function
controller.SJ_BlinkLEDSTOP_function = deviceHandler.BlinkLEDSTOP_function
#--------------------------------------------------------

#start the controller
controller.start()

