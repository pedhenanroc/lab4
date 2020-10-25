import rospy
from std_msgs.msg import String

rospy.init_node('PrimNo')

def matricCallBack(msg):
    soma = msg.data
    print (soma)
    
def timerCallBack(event):
    msg = String()
    msg.data = '2017003638'
    pub.publish(msg)

pub = rospy.Publisher('/topico1', String, queue_size=1)
rospy.Timer(rospy.Duration(1), timerCallBack)
rospy.Subscriber('/topico2', String, matricCallBack)    

rospy.spin()