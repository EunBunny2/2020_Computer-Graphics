import cv2
import numpy as np
import time
import math

def my_padding(src, filter):
    (h, w) = src.shape
    (h_pad, w_pad) = filter.shape
    h_pad = h_pad // 2
    w_pad = w_pad // 2
    padding_img = np.zeros((h+h_pad*2, w+w_pad*2))
    padding_img[h_pad:h+h_pad, w_pad:w+w_pad] = src
    return padding_img

def my_filtering(src, filter):
    (h, w) = src.shape
    (f_h, f_w) = filter.shape
    pad_img = my_padding(src, filter)
    dst = np.zeros((h, w))

    #################################################
    # TODO                                          #
    # filtering 구현                                 #
    # 4중 for문을 이용해 구현할것!                      #
    #################################################

    for i in range(h):
        for j in range(w):
            cut_img = pad_img[i:i+f_h, j:j+f_w]
            val = 0;
            for p in range(f_h):
                for q in range(f_w):
                    val = (cut_img[p, q] * filter[p, q]) + val
                    if p == f_h-1 and q == f_w-1:
                        dst[i, j] = val
    return dst

def my_average_filter(src, fshape, verbose=False):
    #(h, w) = src.shape
    h, w = fshape
    if verbose:
        print('average filtering')

    #################################################
    # TODO                                          #
    # average filter 생성                            #
    #################################################

    filter = np.full(fshape, 1/(h*w))

    if verbose:
        print('<average filter> - shape:', fshape)
        print(filter)

    dst = my_filtering(src, filter)
    return dst

def my_get_Gaussian_filter(fshape, sigma=1):
    (f_h, f_w) = fshape
    '''
    # hint!
    y, x = np.mgrid[-1:2, -1:2]
    y => [[-1,-1,-1],
          [ 0, 0, 0],
          [ 1, 1, 1]]
    x => [[-1, 0, 1],
          [-1, 0, 1],
          [-1, 0, 1]]
    '''

    #################################################
    # TODO                                          #
    # gaussian filter 생성                           #
    #################################################

    y, x = np.mgrid[-(f_h//2):(f_h//2)+1, -(f_w//2):(f_w//2)+1]
    gaus_x = (1/(math.sqrt(2*math.pi)*sigma))*np.exp(-(x**2)/(2*(sigma**2)))
    gaus_y = (1/(math.sqrt(2*math.pi)*sigma))*np.exp(-(y**2)/(2*(sigma**2)))
    if f_w == 1 and f_h != 1:
        gaus_x = 1
    elif f_h == 1 and f_w != 1:
        gaus_y = 1
    filter_gaus = gaus_x * gaus_y
    filter_gaus = filter_gaus/np.sum(filter_gaus)

    return filter_gaus

def my_gaussian_filter(src, fshape, sigma=1, verbose=False):
    (h, w) = src.shape
    if verbose:
        print('Gaussian filtering')

    filter = my_get_Gaussian_filter(fshape, sigma=sigma)

    if verbose:
        print('<Gaussian filter> - shape:', fshape, '-sigma:', sigma)
        print(filter)

    dst = my_filtering(src, filter)
    return dst


if __name__ == '__main__':
    #경로 설정은 알아서...
    src = cv2.imread('baby_SnPnoise.png', cv2.IMREAD_GRAYSCALE).astype(np.float32)

    #사용중인 필터를 확인하고 싶으면 True로 변경, 보기 싫으면 False로 변경
    verbose = False
    filter_size = 7

    print('<average filter>')
    start = time.perf_counter()  # 시간 측정 시작
    dst_average_1D = my_average_filter(src, (filter_size, 1), verbose=verbose)
    dst_average_1D = my_average_filter(dst_average_1D, (1, filter_size), verbose=verbose)
    end = time.perf_counter()  # 시간 측정 끝
    dst_average_1D = dst_average_1D.astype(np.uint8)
    print('average 1D filter time : ', end-start)

    start = time.perf_counter()  # 시간 측정 시작
    dst_average_2D = my_average_filter(src, (filter_size, filter_size), verbose=verbose)
    end = time.perf_counter()  # 시간 측정 끝
    dst_average_2D = dst_average_2D.astype(np.uint8)
    print('average 2D filter time : ', end-start)

    print('<Gaussian filter>')
    start = time.perf_counter()  # 시간 측정 시작
    dst_gaussian_1D = my_gaussian_filter(src, (filter_size, 1), verbose=verbose)
    dst_gaussian_1D = my_gaussian_filter(dst_gaussian_1D, (1, filter_size), verbose=verbose)
    end = time.perf_counter()  # 시간 측정 끝
    dst_gaussian_1D = (dst_gaussian_1D+0.5).astype(np.uint8)
    print('Gaussian 1D filter time : ', end-start)

    start = time.perf_counter()  # 시간 측정 시작
    dst_gaussian_2D = my_gaussian_filter(src, (filter_size, filter_size), verbose=verbose)
    end = time.perf_counter()  # 시간 측정 끝
    dst_gaussian_2D = (dst_gaussian_2D+0.5).astype(np.uint8)
    print('Gaussian 2D filter time : ', end-start)

    cv2.imshow('noise original', src.astype(np.uint8))
    cv2.imshow('average 1D', dst_average_1D)
    cv2.imshow('average 2D', dst_average_2D)
    cv2.imshow('Gaussian 1D', dst_gaussian_1D)
    cv2.imshow('Gaussian 2D', dst_gaussian_2D)

    #리포트용 결과 저장
    # cv2.imwrite('dst_average_1D_7f.png', dst_average_1D)
    # cv2.imwrite('dst_average_2D_7f.png', dst_average_2D)
    # cv2.imwrite('dst_gaussian_1D_7f.png', dst_gaussian_1D)
    # cv2.imwrite('dst_gaussian_2D_7f.png', dst_gaussian_2D)


    cv2.waitKey()
    cv2.destroyAllWindows()
