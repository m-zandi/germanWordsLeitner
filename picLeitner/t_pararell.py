import threading
from . import VidSet as VS
from . import test_VidSet as TVS
import numpy 
from cv2 import cv2
import pytest


def proc():
    name = threading.current_thread().getName()
    # print("processing : ",name,"\n") 
    print(name)

threading.Thread(target=proc,name="first").start()
threading.Thread(target=proc,name="second").start()


# def test_MyClass(self):
#     def threaded_test():
#         self.assertEqual(mc.get(),6)

#     mc = MyClass()
#     self.queue.put(1)
#     self.queue.put(2)
#     self.queue.put(3)
#     self.queue.put({'event_name':'call','val':threaded_test})
frameArr = []
@pytest.mark.parametrize("goingOneFrame,id",[
("goingOneFrame_1",12344),
("goingOneFrame_2",1245234),
("goingOneFrame_3",989758),
("goingOneFrame_4",9345765)
    ]) 
def outFrameArr(id,goingOneFrame,goingOneFrameValues,video,going,returning):



@pytest.mark.parametrize("goingOneFrame,id",[
("goingOneFrame_1",12344),
("goingOneFrame_2",1245234),
("goingOneFrame_3",989758),
("goingOneFrame_4",9345765)
    ]) 
def test_videoOutput(id,goingOneFrame,goingOneFrameValues,video,going,returning):    
    frame = TVS.TestVideo().test_MergeAllList_2(goingOneFrame,goingOneFrameValues,video,going,returning)
    # path=video.dRAdrs
    numpy_image,img,size,pathNFile,out = VS.Video().videoOutput(frame,id)
    print(f"{type(numpy_image) = }")
    assert isinstance(numpy_image,numpy.ndarray)
    # print(f"{type(img) = }")
    assert isinstance(img,numpy.ndarray)
    assert len(size)==2
    assert isinstance(size,tuple)
    # print(f"{type(out) = }")
    assert isinstance(out,cv2.VideoWriter)
    # print(f"{type(pathNFile) = }")
    assert isinstance(pathNFile,str)

# def videoOutput(frame_array,id):
#     pathNFile = VS.Video().dRAdrs+"\\"+f"dR_{id}.mp4"
#     fps = 10
#     for i in range(len(frame_array)):

#         #reading each files
#         numpy_image=np.array(frame_array[i]) 


#         # convert to a openCV2 image, notice the COLOR_RGB2BGR which means that 
#         # the color is converted from RGB to BGR format
#         img=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 

#         height, width, _ = img.shape
#         size = (width,height)
        
#         #inserting the frame into an image array
#         out = cv2.VideoWriter(pathNFile,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
#     for i in range(len(frame_array)):
#         # writing to a image array
#         numpy_image=np.array(frame_array[i]) 
#         img=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
#         out.write(img)
#     out.release()
#     return numpy_image,img,size,pathNFile,out