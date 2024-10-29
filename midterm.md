# Biomedical Image Processing Midterm Examples  
2022094093 Kim Dohoon

--- 
## Enhancement in Spatial Domain
All codes are implemented in `BDIP03.ipynb`.
### Base Image
![02_base](/img/03_base.png)

### Log transformation  
[0, 255]에서 정의되고, 최솟값이 0, 최댓값이 255인 함수를 각 픽셀에 적용하여, 전체적인 밝기를 조절하는 방법

![02_func](/img/03_func.png)
![02_log](/img/03_log.png)

### Histogram Equalization
이미지의 각 픽셀이 고루 분포하도록 픽셀을 변환하는 기법. 모든 픽셀에 대한 CDF를 구하고, Scaling을 통해 범위 조절. `BDIP02.ipynb` 참고

### Low Pass Filter in Spatial Domain
Spatial domain에서 LPF와 컨볼루션을 수행하면 고주파 성분을 일부 제거할 수 있다. 사용한 필터는 다음과 같은 Gaussian Filter이다. 

![02_LPF](/img/03_LPF.png)
![02_Low_freq](/img/03_Low_freq.png)
LPF를 적용한 결과, 고주파 성분이 일부 감소하고, 결과 뿌옇게 흐려진 이미지가 만들어진다.

### Sharpening
이미지 $F$와 LPF $H$에 대해, 고주파 성분을 $F - F * H = F * (e-H)$ 로같이 추출할 수 있다.

이를 $\alpha$의 가중치를 통해 강조하면 다음과 같은 결과를 얻을 수 있다.

![02_sharpening](/img/03_sharpening.png)

## Enhancement in Frequency Domain
All codes are implemented in `BDIP05.ipynb`.
![](/img/05.png)

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
![](/img/07_dilation.png)

### Erosion
![](/img/07_erosion.png)

### Summary
![](/img/07_de.png)

### Opening, Closing
![](/img/07_oc.png)

### Boundary
![](/img/07_boundary.png)