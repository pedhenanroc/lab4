import rospy
from std_msgs.msg import String

rospy.init_node('SegNo')

def indiceCallBack(matric):
    global num
    num = matric.data

def timerCallBack(event):
    soma = 0
    for i in num:
        soma = soma + int(i)
    msg = String()
    msg.data = str(soma)
    pub.publish(msg)

pub = rospy.Publisher('/topico2', String, queue_size=1)
rospy.Timer(rospy.Duration(1), timerCallBack)
rospy.Subscriber('/topico1', String, indiceCallBack) 

rospy.spin()