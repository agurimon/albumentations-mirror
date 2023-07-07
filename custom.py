import cv2
import numpy as np
from albumentations.core.transforms_interface import DualTransform

def vmirrorup(img: np.ndarray) -> np.ndarray:
    axis = img.shape[1] // 2
    half = img[:axis, :, ...]
    half_flip = cv2.flip(half, 0)
    
    return np.concatenate((half, half_flip), axis=0)

def vmirrordown(img: np.ndarray) -> np.ndarray:
    axis = img.shape[1] // 2
    half = img[axis:, :, ...]
    half_flip = cv2.flip(half, 0)
    
    return np.concatenate((half_flip, half), axis=0)
    
def hmirrorup(img: np.ndarray) -> np.ndarray:
    axis = img.shape[0] // 2
    half = img[:, :axis, ...]
    half_flip = cv2.flip(half, 1)

    return np.concatenate((half, half_flip), axis=1)

def hmirrordown(img: np.ndarray) -> np.ndarray:
    axis = img.shape[0] // 2
    half = img[:, axis:, ...]
    half_flip = cv2.flip(half, 1)

    return np.concatenate((half_flip, half), axis=1)

class VerticalMirrorUp(DualTransform):
    def apply(self, img: np.ndarray, **params) -> np.ndarray:
        return vmirrorup(img)
        
    def get_transform_init_args_names(self):
        return ()

class VerticalMirrorDown(DualTransform):
    def apply(self, img: np.ndarray, **params) -> np.ndarray:
        return vmirrordown(img)
        
    def get_transform_init_args_names(self):
        return ()

class HorizontalMirrorUp(DualTransform):
    def apply(self, img: np.ndarray, **params) -> np.ndarray:
        return hmirrorup(img)
    
    def get_transform_init_args_names(self):
        return ()
    
class HorizontalMirrorDown(DualTransform):
    def apply(self, img: np.ndarray, **params) -> np.ndarray:
        return hmirrordown(img)
    
    def get_transform_init_args_names(self):
        return ()