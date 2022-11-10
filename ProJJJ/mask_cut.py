def mask(image):
    height = image.shape[0]
    poly = np.array([(800, height//1.7), (1920-800, height//1.7), (1800, 900),(0, 900)])
    mask = np.zeros_like(image)
    cv.fillPoly(mask, np.array([poly], dtype=np.int64), 1024)
    masked_image = cv.birwise_and(image, mask)
    return  masked_image