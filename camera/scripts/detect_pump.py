#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
#known pump geometry
class class_camera_detector:
    def __init__(self):
        rospy.init_node('detect_pump')
        rospy.loginfo('detect_pump node started')
        self.sb = rospy.Subscriber("image", Image, self.process_image)
        rospy.spin()
    
    def showImage(self, img):
        cv2.imshow('image', img)
        key = cv2.waitKey(1)
        return key
    def process_image(self, msg):
        try:
            # convert sensor_msgs/Image to OpenCV Image
            bridge = CvBridge()
            orig = bridge.imgmsg_to_cv2(msg, "bgr8")
            # resize image (half-size) for easier processing
            resized = cv2.resize(orig, None, fx=0.5, fy=0.5)
            drawImg = resized

            # show results
            key = self.showImage(drawImg)
            if(key == 27):
                self.sb.unregister()
                cv2.destroyAllWindows()
        except Exception as err:
            print err
        
if __name__ == '__main__':
    try:
        detetor= class_camera_detector()
    except rospy.ROSInterruptException:
        pass