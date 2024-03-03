import tobii_research as tr
import time
import main

found_eyetrackers = tr.find_all_eyetrackers()
my_eyetracker = found_eyetrackers[0]
print("Address : " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name: "+ my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

#track gaze data
def gaze_data_callback(gaze_data):
     #print("Left eye: ({gaze_le}) \t Right eye: ({gaze_re})".format(
      #   gaze_le = gaze_data['left_gaze_point_on_display_area'],
      #   gaze_re = gaze_data['right_gaze_point_on_display_area']
    # ))
    #print(gaze_data['left_gaze_point_on_display_area'], gaze_data['right_gaze_point_on_display_area'])
    main.main(x = round(gaze_data['left_gaze_point_on_display_area'], 4), y = round(gaze_data['right_gaze_point_on_display_area'], 4))


my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary = True) #start tracking
time.sleep(10) #5 seconds of tracking
my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback) #stop tracking
