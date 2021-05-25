# 2020_Computer-Graphics
2020 2학기 컴퓨터 그래픽스<br>
<b>자세한 코드 설명은 폴더 내 pdf 유형의 보고서를 확인해주세요.</b>

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

![image](https://user-images.githubusercontent.com/44043468/119547663-5a412c80-bdd0-11eb-9b94-90b69c740130.png)

7x7 average filter

![image](https://user-images.githubusercontent.com/44043468/119547696-6200d100-bdd0-11eb-87fa-c65325bebe48.png)

3x3 gaussian filter

![image](https://user-images.githubusercontent.com/44043468/119547717-67f6b200-bdd0-11eb-9433-4b67b18202d1.png)

7x7 gaussian filter

![image](https://user-images.githubusercontent.com/44043468/119547910-a2f8e580-bdd0-11eb-8319-99a980addee6.png)


<h2>Lab03</h2>
<h4>Goal : Canny edge detection 구현</h4>

![image](https://user-images.githubusercontent.com/44043468/119548452-303c3a00-bdd1-11eb-8876-83d60a60aa2e.png)

![image](https://user-images.githubusercontent.com/44043468/119548537-4518cd80-bdd1-11eb-9327-f3cf268977b1.png)

![image](https://user-images.githubusercontent.com/44043468/119548582-5235bc80-bdd1-11eb-9f98-55f9f30705f7.png)


<h5>Output</h5>

![image](https://user-images.githubusercontent.com/44043468/119548617-5c57bb00-bdd1-11eb-8fec-307907755d38.png)


<h2>Lab04</h2>
<h4>Goal : Harris Corner Detection 구현</h4>

![image](https://user-images.githubusercontent.com/44043468/119548760-814c2e00-bdd1-11eb-882a-6f58b246c419.png)

<h5>Output</h5>

![image](https://user-images.githubusercontent.com/44043468/119548780-88733c00-bdd1-11eb-81c7-cad55c7fa0fc.png)


<h2>Lab05</h2>
<h4>Goal : Harris Corner Detection 구현(Integral image 사용)</h4>

![image](https://user-images.githubusercontent.com/44043468/119548999-c1abac00-bdd1-11eb-8f08-87146bd82461.png)

![image](https://user-images.githubusercontent.com/44043468/119549025-c83a2380-bdd1-11eb-880b-e049578ab25a.png)

![image](https://user-images.githubusercontent.com/44043468/119549051-cf613180-bdd1-11eb-9a5b-c7b74783d4a5.png)

![image](https://user-images.githubusercontent.com/44043468/119549103-da1bc680-bdd1-11eb-901c-f6a2d1cbe5af.png)

<h5>Output</h5>

![image](https://user-images.githubusercontent.com/44043468/119549181-edc72d00-bdd1-11eb-949f-64884ecf751e.png)

![image](https://user-images.githubusercontent.com/44043468/119549202-f3bd0e00-bdd1-11eb-9a56-74ceb324ead7.png)


<h2>Lab06</h2>
<h4>Goal : Forward/Backward 방식으로 이미지 변환</h4>

![image](https://user-images.githubusercontent.com/44043468/119549516-439bd500-bdd2-11eb-9105-95033d72d3e6.png)

<h5>Input</h5>

![image](https://user-images.githubusercontent.com/44043468/119550916-f456a400-bdd3-11eb-8d7c-ba76d71e0e91.png)


<h5>Output</h5>

![image](https://user-images.githubusercontent.com/44043468/119550961-046e8380-bdd4-11eb-861d-115e7a92f1eb.png)

<h2>Lab07</h2>
<h4>Goal : Forward/Backward 방식으로 이미지 2배 키운 후 점 찍기</h4>

<h5>Input</h5>

![image](https://user-images.githubusercontent.com/44043468/119552026-3af8ce00-bdd5-11eb-97d1-8d54acbf3ad3.png)

<h5>Output</h5>

![image](https://user-images.githubusercontent.com/44043468/119551991-30d6cf80-bdd5-11eb-8162-0341c3e9aeb4.png)


<h2>Lab10</h2>
<h4>Goal : ResNet50 네트워크 학습</h4>

![image](https://user-images.githubusercontent.com/44043468/119552424-8f03b280-bdd5-11eb-946f-9d4615373af0.png)

![image](https://user-images.githubusercontent.com/44043468/119552524-96c35700-bdd5-11eb-8d6a-f30e33add718.png)

![image](https://user-images.githubusercontent.com/44043468/119552576-a5117300-bdd5-11eb-9dd5-b5bb5f972fb6.png)

![image](https://user-images.githubusercontent.com/44043468/119552606-acd11780-bdd5-11eb-8376-778458bcbd28.png)

<h5>Output</h5>

![image](https://user-images.githubusercontent.com/44043468/119552678-beb2ba80-bdd5-11eb-86d6-abbadc412f18.png)


<h2>Lab11</h2>
<h4>Goal : ResNet50 네트워크 학습</h4>

![image](https://user-images.githubusercontent.com/44043468/119552835-f02b8600-bdd5-11eb-9946-f4aa15b67e2d.png)

![image](https://user-images.githubusercontent.com/44043468/119552869-f7529400-bdd5-11eb-8025-2d656336885a.png)

![image](https://user-images.githubusercontent.com/44043468/119552892-fd487500-bdd5-11eb-9390-bd22ab09c2e2.png)

![image](https://user-images.githubusercontent.com/44043468/119552912-03d6ec80-bdd6-11eb-8400-f957b77c7a80.png)

![image](https://user-images.githubusercontent.com/44043468/119552944-0df8eb00-bdd6-11eb-9523-7205d7881e5e.png)

<h5>Output</h5>

![image](https://user-images.githubusercontent.com/44043468/119552994-1bae7080-bdd6-11eb-999e-470ab7a62674.png)







