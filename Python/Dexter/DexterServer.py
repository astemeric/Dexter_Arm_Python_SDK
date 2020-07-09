from Dexter import Dexter
import grpc
import robot_arm_pb2
import robot_arm_pb2_grpc
import dexter_update_pb2
import dexter_update_pb2_grpc


class DexterServer(dexter_update_pb2_grpc.DexterUpdateServicer):

    def __init__(self):
        self.dexter = Dexter()
        self.dexter.connect()

    def SendUpdate(self, request, context):
        jointData = self.dexter.update()

        JointMessage = robot_arm_pb2.dexterConfiguration()
        JointMessage.j1.currentAngle = jointData[0]
        JointMessage.j1.goalAngle = jointData[1]
        JointMessage.j2.currentAngle = jointData[2]
        JointMessage.j2.goalAngle = jointData[3]
        JointMessage.j3.currentAngle = jointData[4]
        JointMessage.j3.goalAngle = jointData[5]
        JointMessage.j4.currentAngle = jointData[6]
        JointMessage.j4.goalAngle = jointData[7]
        JointMessage.j5.currentAngle = jointData[8]
        JointMessage.j5.goalAngle = jointData[9]

        return JointMessage

    def Move5(self, request, context):

        angle1 = request.j1
        angle2 = request.j2
        angle3 = request.j3
        angle4 = request.j4
        angle5 = request.j5

        if request.commandType == robot_arm_pb2.P_MOVE:
            sendSuccess = self.dexter.move_P5(angle1, angle2, angle3, angle4, angle5)
        elif request.commandType == robot_arm_pb2.A_MOVE:
            sendSuccess = self.dexter.move_a5(angle1, angle2, angle3, angle4, angle5)
        else:
            sendSuccess = -1

        robotStatus = robot_arm_pb2.dexterStatus()
        robotStatus.status = sendSuccess
        return robotStatus

    def Move7(self, request, context):

        angle1 = request.j1
        angle2 = request.j2
        angle3 = request.j3
        angle4 = request.j4
        angle5 = request.j5
        angle6 = request.j6
        angle7 = request.j7

        if request.MoveType == P_MOVE:
            sendSuccess = self.dexter.move_P7(angle1, angle2, angle3, angle4, angle5, angle6, angle7)
        elif request.MoveType == A_MOVE:
            sendSuccess = self.dexter.move_a7(angle1, angle2, angle3, angle4, angle5, angle6, angle7)
        else:
            sendSuccess = -1

        robotStatus = dexterStatus()
        robotStatus.status = sendSuccess
        return robotStatus
