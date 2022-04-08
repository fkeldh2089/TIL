1. `if request.method == 'POST':` 에 걸리고,  유효성 검사`if form.is_valid():` 에 들어가지 못한 경우등 모든 경우에 대하여  context가 정의되어 오류가 나지 않는다.
2. 다른 method를 먼저 쓰는 경우 반복을 해야하므로, 반복을 피하기 위하여 POST를 먼저 쓴다.