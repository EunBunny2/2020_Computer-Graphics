# 2020_Computer-Graphics
2020 2학기 컴퓨터 그래픽스

<h2>Lab02</h2>
<h4>Goal : 노이즈가 있는 이미지의 노이즈 제거 및 시간 측정</h4>
<h5>def my_filtering</h5>
첫 번째 for문은 pad_img의 열을 돌고, 두 번째 for문은 pad_img의 행을 돈다. 세 번째 for문은 filter의 열을 돌고, 네 번째 for문은 filter의 행을 돈다. cut_img는 pad_img
에서 필터의 크기만큼 잘라온 이미지이다. cut_img와 filter를 convolution 연산해서 새로운 이미지 dst를 만들어낸다.
<br>
<h5>def my_average_filter</h5>
필터의 행 수(h)와 열 수(w)를 곱해 필터의 픽셀 개수를 구하고 픽셀 개수로 1을 나눈 값으로 필터를 채운다.
<br>
<h5>def my_get_Gaussian_filter</h5>
2차 가우시안 수식을 각 축에 대해 분리한 수식을 이용한다. 분리된 수식을 각각 gaus_x, gaus_y로 만들고 둘을 곱한다. 이때, 필터의 행의 수가 1이면 gaus_y를 1로, 열의 수가 1이면 gaus_x를 1로 만들어주어 곱했을 때 값에 영향을 주지 않도록 한다.
<h5>Output</h5>
