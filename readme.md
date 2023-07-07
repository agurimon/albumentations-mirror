# Albumentations Mirror

## Usage
```
transform = A.Compose([
    VerticalMirrorUp(p=1),
    HorizontalMirrorUp(p=1),
    A.Rotate(limit=90, p=1),
])

output = transform(image=image, mask=mask)
```

## Results

![Vertical Mirror Up](./data/VerticalMirrorUp.png)
![Vertical Mirror Down](./data/VerticalMirrorDown.png)
![Horizontal Mirror Up](./data/HorizontalMirrorUp.png)
![Horizontal Mirror Down](./data/HorizontalMirrorDown.png)
![mix](./data/mix.png)