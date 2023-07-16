# step by step 
"""
    - đọc ảnh chụp bên trái, bên phải dưới dạng ảnh grayscale(ảnh mức xám) đồng thời ép kiểu ảnh về float32
    - khởi tạo biến height, width có chiều cao chiều rộng với ảnh bên trái
    - khởi tạo một ma trận không-zero với chiều cao, rộng là height, width 
    - với các pixel duyệt các phần tử từ trái qua phải, từ trên xuống dưới 
      -> tính cost L1 hoặc L2 giữa các cặp pixel left[h,w] và right[h, w-d] với d thuộc [0,disparity_range]. Nếu (w-d)<0 thì gán giá trị cost = max_cost(max_cost=255) nếu dingf 
        L1 hoặc 255 bình phương nếu dùng L2.
      -> với danh sách cost tính được, chọn giá trị d(doptional) mà ở đó cho giá trị cost là nhỏ nhất.
      -> gán deth[h,w]=doptional x scale. Trong đó scale= 255/disparity_range. ở đây scale có thể gán là 16
"""
import cv2 
import numpy as np 

def distance(x,y):
    return abs(x-y)

def pixel_wise_matching_l1(left_img, right_img, disparity_range,save_result=True):
    #read anh
    left=cv2.imread(left_img,0)
    right=cv2.imread(right_img,0)
    # tranfer float 32 
    left = left.astype(np.float32)
    right = right.astype(np.float32)

    height, left = left.shape[:2]
    #create blank disparity map
    depth =np.zeros((height,width),np.unit8)
    scale =16
    max_value =256

    for y in range(height):
        for x in range(width):
            #find j where cost has minimun value 
            disparity =0
            cost_min = max_value
            for j in range(disparity_range):
                cost = max_value if (x<y) <0 else distance(int(left[x,y])), int(right[y,x-j])
                if cost < cost_min:
                    cost_min = cost
                    disparity = j
            depth[y,x]=disparity*scale
    if save_result==True:
        print("Saving result...")
        cv2.imwrite(f'pixel wise l1.pnp', depth)
        cv2.imwrite(f'pixel wise l1 color.pnp', cv2.applyColorMap(depth,cv2.COLORMAP_JET))
    print("Done....")
    return depth

def pixel_wise_matching_l2():
    pass

if __name__ == '__main__':
    left_img_path='/data/tsukuba/left.png'
    right_img_path='/data/tsukuba/right.png'
    disparity_range =16 
    pixel_wise_matching_l1(left_img_path,right_img_path,disparity_range,save_result=1)
    main()
    
