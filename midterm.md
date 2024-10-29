# Biomedical Image Processing Midterm Examples  
2022094093 Kim Dohoon

--- 
## Enhancement in Spatial Domain
All codes are implemented in `BDIP03.ipynb`.
### Base Image
![02_base](/img/03_base.png)

### Log transformation  
[0, 255]에서 정의되고, 최솟값이 0, 최댓값이 255인 함수를 각 픽셀에 적용하여, 전체적인 밝기를 조절하는 방법. log 함수를 사용하면 다음과 같이 변환됨

![02_func](/img/03_func.png)
![02_log](/img/03_log.png)

### Histogram Equalization
이미지의 각 픽셀이 고루 분포하도록 픽셀을 변환하는 기법. 모든 픽셀에 대한 CDF를 구하고, Scaling을 통해 범위 조절.
![](/img/03_hist_eq.png)

### Low Pass Filter in Spatial Domain
Spatial domain에서 LPF와 컨볼루션을 수행하면 고주파 성분을 일부 제거할 수 있다. 사용한 필터는 다음과 같은 Gaussian Filter이다. 

![02_LPF](/img/03_LPF.png)
![02_Low_freq](/img/03_Low_freq.png)
LPF를 적용한 결과, 고주파 성분이 일부 감소하고, 결과 뿌옇게 흐려진 이미지가 만들어진다.

### Sharpening
이미지 $F$와 LPF $H$에 대해, 고주파 성분을 $F - F * H = F * (e-H)$ 로 추출할 수 있다.
또는$\nabla^2$ operator를 사용해도 되는데, 수업 자료 참고하기.
이를 $\alpha$의 가중치를 통해 강조하면 다음과 같은 결과를 얻을 수 있다.

![02_sharpening](/img/03_sharpening.png)

## Enhancement in Frequency Domain
All codes are implemented in `BDIP05.ipynb`.  

LPF는 Spatial domain에서 컨볼루션을 수행하거나, Frequency domain에서 element-wise로 곱하는 것으로 이미지에 적용할 수 있다.
![](/img/05.png)  
Ideal LPF를 사용했으므로, sinc함수에 의한 ringing effect를 확인할 수 있다. Ringing Effect 감소를 위해 Butterworth filter 또는 Gaussian filter를 사용할 수 있다.

## Binary Operation
All codes are implemented in `BDIP06.ipynb`.

### Connected Component Labeling
![](/img/06_CCL.png)

### Chamfer Distance  
다음의 행렬을 사용해 거리를 측정한다.
![](/img/06_chamfer.png)

> When changing padding value...   

![](/img/06_chamfer_pad.png)

1. Padding value는 타겟 내부의 픽셀에는 영향을 주지 못함
2. 가장자리에 맞닿은 픽셀의 경우 일부 영향을 받음

## Morphology
### Dilation    
타켓의 모든 픽셀을 SE로 팽창하는 연산
![](/img/07_dilation.png)

### Erosion  
타겟의 모든 픽셀을 순회하며, SE가 딱 들어맞는 픽셀만 남김
![](/img/07_erosion.png)

### Summary
![](/img/07_de.png)

### Opening, Closing
![](/img/07_oc.png)

### Hit-or-Miss Transformation
##### Structuring Element
![](/img/07_SE.png)

##### Result
![](/img/07_HoM.png)