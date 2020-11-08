import rospy
from std_msgs.msg import Int32

def listener():
    
    rospy.init_node('listener',anonymous=True)
    while True:
        rospy.Subscriber("bruh1",Int32,call1)
        rospy.Subscriber("bruh2",Int32,call2)
def call1(data):
    global var1
    var1 = data
    callback1()
def call2(data):
    global var2
    var2 = data
    callback1()

def callback1():
    if var1 != 0 and var2 != 0:
        pub = rospy.Publisher("result",Int32,queue_size = 10)
        print(var1.data + var2.data)
        pub.publish(var1.data + var2.data)
        
listener()
